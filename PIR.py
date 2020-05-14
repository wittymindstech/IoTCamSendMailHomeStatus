from gpiozero import MotionSensor
from picamera import PiCamera
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import datetime
import smtplib
import time
import subprocess
# Email Addresses
#fromAddr = 'Address Sending Email'
#toAddr = 'Address Receiving Email'

#Motion Sensor and Camera Initialized
#PIRSensor = MotionSensor(4)
#camera = PiCamera()

# Variable to Exit while loop
Tripped = True

#wait five seconds
time.sleep(5)

while Tripped:
	if PIRSensor.motion_detected:
		print("Motion Detected")

		#Sent Tripped to False and capture picture
		Tripped = False
		#timeCaptured = '/home/pi/Desktop' + datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S') + '.png'
		#camera.rotation = 180
		#camera.capture(timeCaptured)
		subprocess.call('/home/pi/sendHomeStatus.sh', shell=True)
                #subprocess.call('/home/pi/ledblink.py', shell=True)
