import cv2
import time
 #This code clicks a picture through webcam and saves it into desired path
cam=cv2.VideoCapture(0)
time.sleep(1)
_,img=cam.read()
cv2.imwrite("imagefrom camera.jpg",img)
cam.release()

#prakash tomar