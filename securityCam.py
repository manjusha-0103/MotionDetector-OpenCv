#!/usr/bin/env python

import cv2

cam = cv2.VideoCapture('video.mp4')
x1 = cam.get(27)
print(x1)
while cam.isOpened():
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()
    diff = cv2.absdiff(frame1, frame2)
    if ret:
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        #blur = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=3)
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
        for c in contours:
            if cv2.contourArea(c) < 2500:
                continue
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
            print("\n***************Detected motion.***************")
           # winsound.PlaySound('alert.wav', winsound.SND_ASYNC)
        cv2.imshow('Security Cam', frame1)
   
    if cv2.waitKey(50) == 32 :
        cv2.waitKey()      
    
    if cv2.waitKey(10) == ord('q'):
        break
       
    
#cv2.release()
cv2.destroyAllWindows()
