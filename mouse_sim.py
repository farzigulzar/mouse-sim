import mouse
import flipmatrix as fp
import cv2
import numpy as np
import centroid as ct

'''Initialisng the camera'''
cap=cv2.VideoCapture(0)

'''Initialising the lower and upper bounds for red color'''
lower=np.array([0,190,190])
higher=np.array([4,255,255])
while(1):
    ''' frame-> frame1-> hsv-> mask(hsv masked for red)-> Blurred image(Median Blur)->res(RGB masked for red)'''

    '''frame1 is camera read image '''
    ret, frame1=cap.read()

    '''frame is flipped because the frame image is flipped '''
    frame=fp.flip(frame1)
    cv2.imshow('Camera',frame)


    '''converting the frame to hsv because masking should be done on hsv images '''
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #cv2.imshow('original', hsv)


    '''Finally masking the hsv image obatained with lower and upper inbounds for red color(My marker was red color)
    this is binary image tho'''
    mask = cv2.inRange(hsv, lower, higher)
    #cv2.imshow('HSV_Masked', mask)


    '''Blur on masked image'''
    blur=cv2.medianBlur(mask,3)
    #cv2.imshow('Median blur', blur)

    '''using the bitwsie_and function to display the red color only'''
    res=cv2.bitwise_and(frame,frame, mask= mask)
    #cv2.imshow('Masked red color', res)


    '''Finding the centroid of all contours '''
    cx=ct.xlen(mask)
    cy=ct.ylen(mask)
    print(cx,' ',cy)


    '''Finally moving the mouse cursor to the given postion of centroid usign mouse dependency'''
    mouse.move(4*cx,3*cy)


    if(cv2.waitKey(1)==27):
        break


cap.release()
cv2.destroyAllWindows()
