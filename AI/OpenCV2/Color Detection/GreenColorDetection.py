import numpy as np
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #Blue color
    # low_blue = np. array([94, 80, 2])
    # high_blue = np.array([126, 255, 255])
    # blue_mask = cv2. inRange(hsv_frame, low_blue, high_blue)
    # blue = cv2.bitwise_and(frame, frame, mask=blue_mask)
    
    #Green color
    low_green = np. array([40, 100, 100])
    high_green = np.array([102, 255, 255])
    green_mask = cv2. inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)
    
    cv2. imshow("Frame", frame)
    #cv2. imshow('Blue', blue)
    cv2. imshow('Green', green)
    
    key = cv2.waitKey(1)
    if key == 27:
        break

