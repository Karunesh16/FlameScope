import smtplib
import imghdr
from email.message import EmailMessage

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg["subject"] = subject
    msg["to"] = to
    
    user = "karuneshtest16@gmail.com"
    msg["from"] = user
    password = "qavubantzlxjqihb"
    
    with open('fire_image.jpeg', 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = f.name
        msg.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
       
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user,password)
    
    server.send_message(msg)
    server.quit()
    
if __name__ == '__main__':
    email_alert("Test1","Hello World","karunesh.b@somaiya.edu")