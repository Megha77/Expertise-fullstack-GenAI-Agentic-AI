# # Only Red color detection
# import cv2
# import numpy as np
# cap = cv2.VideoCapture(0)

# while True:
#     _, frame = cap.read()
#     hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
   
#     # Red color
#     low_red = np.array([161, 155, 84]) # lowest hue would be - 161,155,84( how do i found this i tested before and found this)
#     high_red = np.array([179, 255, 255])
#     #mask = cv2.inRange(hsv_frame, low_red, high_red)      
#     red_mask = cv2.inRange(hsv_frame, low_red, high_red) #we create maskk on hsv frame and then low red or high red
#     red = cv2.bitwise_and(frame, frame, mask=red_mask)
#     cv2.imshow("Frame", frame)
#     #cv2.imshow('Red mask', mask)
#     cv2.imshow('Red', red)
 
#     key = cv2.waitKey(1)
#     if key ==27:
#         break

# Only Red color detection
import cv2
import numpy as np

# Added cv2.CAP_DSHOW to fix the Windows/FFMPEG warning and open the camera reliably
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    
    # SAFETY CHECK: If the camera fails to read a frame, skip or exit instead of crashing
    if not ret or frame is None:
        print("Waiting for camera or unable to read frame...")
        continue

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
   
    # Red Color Mask 1: Upper range (Pinkish/Dark Red) - Your original values
    low_red1 = np.array([161, 155, 84])
    high_red1 = np.array([179, 255, 255])
    mask1 = cv2.inRange(hsv_frame, low_red1, high_red1)

    # Red Color Mask 2: Lower range (Bright/Orange Red) - Essential for true red detection
    low_red2 = np.array([0, 155, 84])
    high_red2 = np.array([10, 255, 255])
    mask2 = cv2.inRange(hsv_frame, low_red2, high_red2)

    # Combine both masks to get the complete range of red
    red_mask = cv2.bitwise_or(mask1, mask2)
    
    # Apply the combined mask
    red = cv2.bitwise_and(frame, frame, mask=red_mask)
    
    # Windows
    cv2.imshow("Frame", frame)
    cv2.imshow('Red mask', red_mask)
    cv2.imshow('Red Only', red)
 
    key = cv2.waitKey(1)
    if key == 27: # Press 'ESC' to exit
        break

cap.release()
cv2.destroyAllWindows()
