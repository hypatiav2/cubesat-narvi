import cv2
import numpy as np
from git import Repo

#import libraries
import time
import os

def detectObject(imgpath):
    detected = False

    image = cv2.imread(imgpath)
    original = image.copy()
    width, height, channel = image.shape
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

    if detected == True:
        cv2.imwrite(imgpath, image)
    else:
        os.remove(imgpath)
    return detected


# function for uploading image to Github
def git_push(imgpath):
    try:
        repo = Repo(r"\Desktop/cubesat-narvi/")
        repo.git.add(imgpath)
        repo.index.commit('New Photo')
        print('made the commit')
        origin = repo.remote('origin')
        print('added remote')
        origin.push()
        print('pushed changes')
    except:
        print("Couldn't upload to GitHub")


for filename in os.scandir(r"\Desktop/cubesat-narvi/"):
    if filename.is_file() and "narvi_" in filename.path :
        imgname = filename.path
        if detectObject(imgname) == True:
            print("Object detected...now sending to GitHub")
            git_push(imgname)
        else:
            print("No plastics detected.")