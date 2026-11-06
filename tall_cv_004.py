import cv2
model = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
cap =cv2.VideoCapture(0) #obtenemos acceso: Camara, video
while True:  #mientras la app se ejecuta
    ret, frame = cap.read()  #lectura de frames
    frame_gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #cambiamos a monocromatico
    faces = model.detectMultiScale(frame_gray, scaleFactor=1.3, minNeighbors=5) #deteccion de rostros
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('Camara', frame) #visualizamos el frame
    if cv2.waitKey(1) == ord('q'): #finalizamos la app con la tecla q
        break
cap.release() #libramos la lecturade camara
cv2.destroyAllWindows() #limpiamos las variables generadas por la app
