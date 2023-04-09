from django.shortcuts import render, redirect
from django.http import StreamingHttpResponse
import cv2
from . import alert_mail
from . import alert_phone
from PIL import Image
import numpy as np
import datetime
from . import YOLOv8
from .models import FireInstance
import datetime


model_path = r"C:/Programming/College/Sem-VI MP-Fire Detection/Implementation/FireDetection/FireDetectionWeb/FireDetectionApp/models/best.onnx"
yolov8_detector = YOLOv8.YOLOv8class(model_path, conf_thres=0.5, iou_thres=0.5)

count = 0

# Create your views here.
def Homepage(request):
    return render(request, 'FireDetectionApp/index.html')

def VideoDetect(request):
    pass

def ImageDetect(request):
    pass

def WebCamDetect(request):
    return render(request, 'FireDetectionApp/webcamdetect.html')

def video_feed(request):
    # Set up video capture
    cap = cv2.VideoCapture(0)

    # Set video codec
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')

    # Set video dimensions
    width = 1880
    height = 720

    # Define generator function to capture frames
    def frame_generator():
        global count
        c=0
        intensity = ""
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()

            if not ret:
                break

            # Update object localizer
            boxes, scores, class_ids = yolov8_detector(frame)
                
            combined_img = yolov8_detector.draw_detections(frame)
            ret, jpeg = cv2.imencode('.jpg', combined_img)
            # cap.imshow("Detected Objects", combined_img)

            print(boxes, scores, len(class_ids))
            if len(scores) == 0:
                pass
            elif len(scores) > 0:
                if float(scores[0]) > 0.8:
                    intensity = "Danger"
                if float(scores[0]) > 0.7 and scores[0] < 0.8:
                    intensity = "Mild"
                if float(scores[0]) < 0.7:
                    intensity = "Low"

            if len(class_ids) == 1:
                c = c + 1
                print(c)
                
            if (c == 15):
                count += 1
                img = Image.fromarray(combined_img)
                # img.show()
                img.save("fire_image.jpeg")

                instance = FireInstance()
                instance.instance_no = count
                instance.instance_intensity = intensity
                instance.instance_time = str(datetime.datetime.now()).split(" ")[1]
                instance.instance_date = str(datetime.datetime.now()).split(" ")[0]
                instance.instance_address = "KJSIT, Ayurvihar, Sion"
                instance.save()
                
                c=0
                meassage = f""" Fire Detected
                At Adress : KJSIT, Ayurvihar, Sion
                date: {datetime.datetime.now()} """
                alert_mail.email_alert("FIRE DETECTED!!!!",meassage,"agradevu22@gmail.com")
                alert_phone.call_alert()

                # Encode the frame as jpeg
                ret, jpeg = cv2.imencode('.jpg', combined_img)
            
            # Yield the frame as bytes
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')

    # Set response headers
    response = StreamingHttpResponse(frame_generator(), content_type='multipart/x-mixed-replace; boundary=frame')

    return response
    
def close_cap(request):
    return render(request, 'FireDetectionApp/index.html')

def VideoDetect(request):
    pass

def services(request):
    return render(request, 'FireDetectionApp/service.html')

def contactus(request):
    return render(request, 'FireDetectionApp/contact.html')

def userdashboard(request):
    fire_instance = FireInstance.objects.all()
    instance_count = fire_instance.count()
    context = {
        'instance_count': instance_count
    }
    return render(request, 'FireDetectionApp/dashboard_dummy.html', context=context)

def useraccount(request):
    return render(request, 'FireDetectionApp/account_dummy.html')

def Homepage_dummy(request):
    return render(request, 'FireDetectionApp/dummy_index.html')

def fire_instance(request):
    fire_instance = FireInstance.objects.all()
    context = {
        'fire_instance': fire_instance
    }
    return render(request, 'FireDetectionApp/fire_instance.html', context=context)