from ImageProc import arucoProjection
from DobotDriver import DobotDriver
import cv2
import numpy as np

cam = arucoProjection(2)
dobot_arm = DobotDriver()

threshold_value = 154

kernel = np.ones((5,5),dtype=np.uint8)
# dobot_arm.move_on_marker_coordinate(0.1025,0.09,0.0,0.0,wait=True)
dobot_arm.suction_off(wait=True)
dobot_arm.move_on_robot_coordinate(0.205,0.0,0.15,0.0,wait=True)

cam.wait_camera_open()

projection_image ,marker_image = cam.get_projection_image()
gray_image = cv2.cvtColor(projection_image, cv2.COLOR_BGR2GRAY ) 

ret ,mask = cv2.threshold(projection_image,threshold_value,255,cv2.THRESH_BINARY_INV)
mask = cv2.erode(mask,kernel,iterations=1)
mask = cv2.dilate(mask,kernel,iterations=1)
contours ,hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

object_pts ,object_areas = cam.computeContours(contours)
print(object_pts)

cv2.imshow('projection', projection_image) 
cv2.imshow('blue_mask', mask) 
cv2.imshow('marker', marker_image) 

key = cv2.waitKey(0) & 0xFF 

for i,pt in enumerate(object_pts) :  

    # print(blue_areas[i])

    if object_areas[i] >= 8000 : 
        print("Plate")
        dobot_arm.move_on_marker_coordinate(object_pts[i][0],object_pts[i][1],-0.06,0.0,wait=True)
        dobot_arm.move_on_marker_coordinate(object_pts[i][0],object_pts[i][1],-0.07,0.0,wait=True)
        dobot_arm.suction_on(wait=True)
        dobot_arm.move_on_marker_coordinate(object_pts[i][0],object_pts[i][1],-0.06,0.0,wait=True)

        # PLACE ZONE
        dobot_arm.move_on_robot_coordinate(0.205,0.0,0.15,0.0,wait=True)
        dobot_arm.move_on_robot_coordinate(0.14,0.1,-0.03,0.0,wait=True)
        dobot_arm.move_on_robot_coordinate(0.14,0.1,-0.04,0.0,wait=True)
    
    else :
        print("Cube")
        dobot_arm.move_on_marker_coordinate(object_pts[i][0]-0.005,object_pts[i][1]-0.02,-0.04,0.0,wait=True)
        dobot_arm.move_on_marker_coordinate(object_pts[i][0]-0.005,object_pts[i][1]-0.02,-0.05,0.0,wait=True)
        dobot_arm.suction_on(wait=True)
        dobot_arm.move_on_marker_coordinate(object_pts[i][0]-0.005,object_pts[i][1]-0.02,-0.04,0.0,wait=True)

        # QR CODE
        dobot_arm.move_on_robot_coordinate(0.205,0.0,0.15,0.0,wait=True)
        dobot_arm.move_on_robot_coordinate(0.24,0.1,-0.03,0.0,wait=True)
        dobot_arm.move_on_robot_coordinate(0.24,0.1,-0.04,0.0,wait=True)

    dobot_arm.suction_off(wait=True)

    dobot_arm.move_on_robot_coordinate(0.205,0.0,0.15,0.0,wait=True)

cam.stop_camera() 
cv2.destroyAllWindows()
        
