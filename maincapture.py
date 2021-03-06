#AUTHOR: MERYL MATHEW

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

"""
# function for uploading image to Github <- use at groundstation
def git_push():
    try:
        repo = Repo('/home/pi/FlatSatChallenge')
        repo.git.add('folder path')
        repo.index.commit('New Photo')
        print('made the commit')
        origin = repo.remote('origin')
        print('added remote')
        origin.push()
        print('pushed changes')
    except:
        print('Couldn\'t upload to git')
"""


#SET THRESHOLD
threshold = 1
repeat = "y"
#read acceleration
count = 0
while count<=10:
    print(".")
    print("Motion detected")
    name = "narvi"     #Last Name, First Initial  ex. FoxJ
    if name:
        t = time.strftime("_%H%M%S")      # current time string
        imgname = ('/home/pi/Desktop/cubesat-narvi/%s%s.jpg' % (name,t)) #change directory to your folder
        camera.capture(imgname)
    time.sleep(3)
    count+=1
