import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret , frame = cap.read()
    # print(frame)
    if ret== True:
        # print (cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        # print (cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        frame = cv2.rectangle(frame, (212,132), (428,348),(255,255,255),1)
        frame = cv2.line(frame, (284,132),(284,348),(255,255,255),1)    #Vertical Line 1
        frame = cv2.line(frame, (356,132),(356,348),(255,255,255),1)    #Vertical Line 2
        frame = cv2.line(frame, (212,204),(428,204),(255,255,255),1)    #Horizontal Line 1
        frame = cv2.line(frame, (212,276),(428,276),(255,255,255),1)    #Horizontal Line 1
        frame2 = frame[132:348, 212:428]                                #crop image
        font = cv2.FONT_HERSHEY_SIMPLEX
        hsv = cv2.cvtColor(frame2, cv2.COLOR_BGR2HSV)
        lower_red = np.array([110,50,50]) 
        upper_red = np.array([130,255,255]) 
        mask = cv2.inRange(hsv, lower_red, upper_red) 
        res = cv2.bitwise_and(frame2,frame2, mask= mask) 
        cv2.imshow('image2',frame)
        cv2.imshow('hsv', hsv)
        cv2.imshow('res', res)
        k=cv2.waitKey(1)
        if k== ord('c') :
            cv2.imwrite('save.jpg',frame2)
            print('image captured')        
        elif k== ord('q'):
            break
    else:
        break    
cap.release()
cv2.destroyAllWindows()