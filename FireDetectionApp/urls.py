from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

app_name = 'FireDetectApp'

urlpatterns = [
    #Home page for the user
    path('', views.Homepage, name="homepage"),

    path('home/', views.Homepage_dummy, name="homepage_dummy"),

    # For Detections using a video
    path('videodetect/', views.VideoDetect, name="videodetectpage"),

    # For Detections using a image
    path('imagedetect/', views.ImageDetect, name="imagedetectpage"),

    # For Detections using a webcam
    path('webcamdetect/', views.WebCamDetect, name="webcamdetectpage"),
    
    path('video_feed/', views.video_feed, name="video_feed"),

    path('close_cap/', views.close_cap, name="close_cap"),

    path('services/', views.services, name="services"),

    path('contactus/', views.contactus, name="contactus"),

    path('userdashboard/', views.userdashboard, name="userdashboard"),

    path('useraccount/', views.useraccount, name="useraccount"),

    path('userfireinstance', views.fire_instance, name="fire_instance")
]