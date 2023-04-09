import smtplib
import imghdr
from email.message import EmailMessage

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg["subject"] = subject
    msg["to"] = to
    
    user = "xxxxxxxxxxxxxx@gmail.com"
    msg["from"] = user
    password = "xxxxxxxxxxxxxxxxxxxxx"
    
    with open('fire_image.jpeg', 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = f.name
        msg.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
       
    server = smtplib.SMTP("smtp.gmail.com",port)
    server.starttls()
    server.login(user,password)
    
    server.send_message(msg)
    server.quit()
    
if __name__ == '__main__':
    email_alert("Test1","Fire Detected","xxxxxxxxxxxxxxxxxxxxxxxxxx")
