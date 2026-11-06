import cv2
from ultralytics import YOLO

model= YOLO('yolov8n.pt')
cap= cv2.VideoCapture('corriendo.mp4')
posiciones={}
while True:
    ret, frame= cap.read()
    frame= cv2.resize(frame, (640,480))
    #---INICIO DETECCIÓN CON YOLO---
    resultados= model.track(frame, persist= True, classes=[0], verbose=False)[0]
    if resultados.boxes.id is not None:
    #---FIN DETECCIÓN YOLO---
    #FLUJO NORMAL DE TRABAJO CON VIDEOS
    cv2.imshow('Yolo', frame)
    if cv2.waitKey(50)==ord('q'):
        #print(resultados.boxes.id)
        break
cap.release()
cv2.destroyAllWindows() 