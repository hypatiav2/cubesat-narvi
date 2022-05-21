import cv2
import numpy as np
from git import Repo


#import libraries
import time
import os
import busio
import board
import adafruit_bno055
#from git import Repo
from picamera import PiCamera
#setup imu and camera
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bno055.BNO055_I2C(i2c)
camera = PiCamera()



def detectObject(imgpath):
    detected = False

    image = cv2.imread(imgpath)
    original = image.copy()
    width, height, channel = image.shape()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 1)
    thresh = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)

    ROI_number = 0
    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for c in cnts:
        x,y,w,h = cv2.boundingRect(c)
        if w > 50 and h > 50 and w < width and h < height:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0,0,255), 2)
            detected = True

    return detected


# function for uploading image to Github
def git_push(imgpath):
    try:
        repo = Repo(imgpath)
        repo.git.add('folder path')
        repo.index.commit('New Photo')
        print('made the commit')
        origin = repo.remote('origin')
        print('added remote')
        origin.push()
        print('pushed changes')
    except:
        print('Couldn\'t upload to git')


while True:
    accelX, accelY, accelZ = sensor.acceleration
    if accelX > 1:

        name = "narvi"
        t = time.strftime("_%H%M%S")      # current time string
        imgname = ('/home/pi/Desktop/cubesat-narvi/%s%s.jpg' % (name,t)) #change directory to your folder
        camera.capture(imgname)

        if detectObject(imgname) == True:
            git_push(imgname)
