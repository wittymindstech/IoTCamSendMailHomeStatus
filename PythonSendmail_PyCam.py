import os
import smtplib
import picamera
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def SendMail(ImgFileName):
    img_data = open(ImgFileName, 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = 'home status'
    msg['From'] = 'raspberry_pi@home'
    msg['To'] = 'penguin.techlinux@gmail.com'

    text = MIMEText("test raspberry pi using python")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
    msg.attach(image)
    Server="smtp.gmail.com"
    Port="587"
    s = smtplib.SMTP(Server, Port)
    s.ehlo()
    s.starttls()
    s.ehlo()
    UserName="penguin.techlinux@gmail.com"
    UserPassword="xxxxxx123"
    From="raspberry_pi@home"
    To="penguin.techlinux@gmail.com"
    s.login(UserName, UserPassword)
    s.sendmail(From, To, msg.as_string())
    s.quit()



camera = picamera.PiCamera()
camera.start_preview()
camera.capture("snapshot.jpg")
camera.stop_preview()

SendMail("/home/pi/snapshot.jpg")
