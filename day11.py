import cv2
import matplotlib.pyplot as plt
vid = cv2.VideoCapture(0)
while True:
    flag, img = vid.read()
    if flag:
       # Processig Code
       img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
       th,img_bw = cv2.threshold(img_gray,100,255,cv2.THRESH_BINARY)
      

       ##
       cv2.imshow('Preview',img_bw)
       key = cv2.waitKey(1)
       if key == ord('q'):
        break
    else:
       break 
vid.release()    
cv2.destroyAllWindows()  