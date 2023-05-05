import cv2
import matplotlib.pyplot as plt
from time import sleep
import numpy as np

fd=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
vid=cv2.VideoCapture(0)
while True:
    flag,img=vid.read()
    if flag:
        # processing code
        #  img convert into gray image
        img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=fd.detectMultiScale(
                img_gray,
                scaleFactor = 1.1,
                minNeighbors = 5,
                minSize = (50,50)
        )
        np.random.seed(50)
        colors = np.random.randint(0,255, (len(faces),3)).tolist() 
        i=0

        # th,img_bw=cv2.threshold(img_gray,100,255,cv2.THRESH_BINARY)
        # print(type(img_gray))
        # break
        for x,y,w,h in faces:
            cv2.rectangle(
                img,pt1=(x,y),pt2=(x+w,y+h),color=colors[i],
                thickness=8
            )
            i += 1
        cv2.imshow('preview',img)
        key=cv2.waitKey(1)
        if key==ord('q'): ##for stop the camera ligth which is acquire by this program
           break
    else:
        print('No frames')
        break
    sleep(0.1)
vid.release()
cv2.destroyAllWindows()