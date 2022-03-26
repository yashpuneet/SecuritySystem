import cv2
import pyttsx3
import speech_recognition as sr

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

engine = pyttsx3.init()
voiceid = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)
engine.setProperty('voice', voiceid)

vid = cv2.VideoCapture(0)

state = 0
imgnum = 1

engine.say("Security System Activated")
engine.runAndWait()

while(True):
    ret, frame = vid.read()

    faces = face_cascade.detectMultiScale(
        frame,
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(20, 20)
    )

    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 4)

    cv2.imshow('frame', frame)

    if state == 0:
        if len(faces) > 0:
            state = 1
            engine.say("Human Presence Detected.")
            engine.runAndWait()
            cv2.imwrite('human_detected_' + str(imgnum) + '.png', frame)
            imgnum += 1
            
    else:
        if len(faces) == 0:
            state = 0
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
