import numpy as np
import cv2
import argparse
import base64
from playsound import playsound

from PIL import Image
from PIL import ImageDraw

face_cascade = cv2.CascadeClassifier('classifiers/haar-face.xml')
eye_cascade = cv2.CascadeClassifier('classifiers/haar-eyes.xml')

cap = cv2.VideoCapture(0)
i = 0

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #detect faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        print eyes
        print "eyes not detected or closed"
        for (ex,ey,ew,eh) in eyes:
            print "eyes detected"
            # determine how to calculate when a long closed eye occurs vs loss of eye detection
            i = i + 1
            if (i == 10):
                p = playsound("sounds/yes-5.wav")
                i = 0    
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    # Display the resulting frame
    #cv2.imshow('frame',gray)
    cv2.imshow('frame',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()