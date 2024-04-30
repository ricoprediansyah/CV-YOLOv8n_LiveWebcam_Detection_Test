from ultralytics import YOLO
import cv2
model=YOLO('../YOLO-Weights/qutions.pt')
results=model('../Images/11.jpg', show=True)

cv2.waitKey(0)