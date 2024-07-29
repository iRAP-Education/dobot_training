from ImageProc import arucoProjection
import cv2
import numpy as np

def nothing(x):
   pass

cam = arucoProjection(2)

cv2.namedWindow('thresholding')
cv2.createTrackbar('threshold','thresholding',255,255,nothing)

while True : 
    # raw_image = cam.get_image()
    projection_image ,marker_image = cam.get_projection_image()
    gray_image = cv2.cvtColor(projection_image, cv2.COLOR_BGR2GRAY ) 

    threshold_value = cv2.getTrackbarPos('threshold','thresholding')

    ret ,mask = cv2.threshold(gray_image,threshold_value,255,cv2.THRESH_BINARY)


    cv2.imshow('projection', projection_image) 
    cv2.imshow('thresholding', mask) 
    cv2.imshow('marker', marker_image) 

    key = cv2.waitKey(1) & 0xFF 

    if key == ord('q') : 
        break

cam.stop_camera() 
cv2.destroyAllWindows()
        
