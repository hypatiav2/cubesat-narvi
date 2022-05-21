import cv2
import numpy as np

image = cv2.imread('2.jpg')
original = image.copy()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 1)
thresh = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)

ROI_number = 0
cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
for c in cnts:
    x,y,w,h = cv2.boundingRect(c)
    if w > 40 and h > 40:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0,0,255), 2)

cv2.imshow('image', image)
cv2.imshow('blur', blur)
cv2.imshow('Thresh',thresh)
cv2.waitKey()