#pip install ultralytics

from ultralytics import YOLO
import numpy

# load a pretrained YOLOv8n model
model = YOLO("yolov8n.pt", "v8")  

# predict on an image
detection_output = model.predict(source=r"D:\MEGH@\AI_Engineer\Practice\Live Class Practice\AI\dog.jpg", conf=0.25, save=True) 

# Display tensor array
print(detection_output)

# Display numpy array
# print(detection_output[0].numpy())