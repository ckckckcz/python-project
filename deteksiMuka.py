import cv2
import numpy as np

deteksi_muka=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
deteksi_mata=cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while True:
    
    ret,img=cap.read()
    
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face=deteksi_muka.detectMultiScale(gray)
    
    for(x,y,w,h) in face:
        cv2.putText(img,'face',(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(200,255,255),2,cv2.LINE_AA)
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

        roi_gray=gray[y:y+h,x:x+w]
        roi_color=img[y:y+h,x:x+w]

        eyes=deteksi_mata.detectMultiScale(roi_gray)

        for(ex,ey,ew,eh) in eyes:
            cv2.putText(roi_color,'eye',(ex,ey),cv2.FONT_HERSHEY_SIMPLEX,0.5,(200,255,255),2,cv2.LINE_AA)
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
        
        cv2.imshow('Deteksi Muka dan Mata',img)
        
        if cv2.waitKey(1) & 0xFF==ord('w'):
            break

cap.release()
cv2.destroyAllWindows()