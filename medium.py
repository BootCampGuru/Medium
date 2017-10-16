#!/usr/bin/python

import RPi.GPIO as GPIO
import requests
import time
import json
import smtplib
from pprint import pprint
import requests
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from cap1 import Buzzer, BuzzerStop
from segmentfull import LCDMessage, LCDClear
from stepper import steploop, destroy


def send_email(user, pwd, recipient, subject, body):
    import smtplib

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = "Medium Medicine Alert"
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"

GPIO.setwarnings(False)
fixed_interval = 5
GPIO.setmode(GPIO.BOARD)
BeepPin = 13    # pin13
counter = 1
try:
    LCDClear()
    LCDMessage("Hello!\n Medium setup...")
    while True:
        LCDMessage("Take Medicine\n at 7:30 AM")
        counter = counter + 1
        if counter > 5:
            counter = 0
            steploop();
            send_email("ranjanbiswasgwu@gmail.com", "Sagat99!", "biswasrk@gwu.edu", "Medicine Alert", "Please take your medicine at 7:30 A.M. Please drink water with the medicine and wait 30 minutes prior to having your meal")
            LCDMessage("Drink Water\n Wait 30 minutes")
            time.sleep(50)
            Buzzer();
            
            
except KeyboardInterrupt:
    BuzzerStop()
    destroy()



