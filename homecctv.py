import cv2,time
from datetime import datetime
import argparse
import os

face_cascade=cv2.CascadeClassifier("")

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    if frame is not None:
        gray = cv2.cvtcolor(frame,cv2.COLOR_BGR2GRAY)
        face = face_cascade.detectMultiScale(gray,scale=1.1, minNeighbours=10)

        from x,y,w,h in faces:
             img = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
             exact_time= datetime.now().strftime('%Y-%b-%d-%H-%S-%f')
             cv2.imwrite("face detected" + str(exact_time)+".jpg",img)

        cv2.imshow("home surv", frame)
        key = cv2.waitkey(1)

        if key ==ord('q'):
            ap = argparse.ArgumentParser()
            ap.add_argument("-ext", "--extension", required=False,default='jpg')
            ap.add_argument("-o","--output", required=False,default='output.mp4')
            args =vars(ap.parse_args())





