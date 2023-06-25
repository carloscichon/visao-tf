import mtcnn
import cv2
import numpy as np
from keras.models import model_from_json
import time

emotion_dict = {0: "angry", 1: "contempt", 2: "disgust", 3: "fear", 4: "happy", 5: "neutral", 6: "sad", 7: "surprise"}

# load json and create model
json_file = open('affect_model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
emotion_model = model_from_json(loaded_model_json)

# load weights into new model
emotion_model.load_weights("affect_model.h5")
print("Loaded model from disk")

cap = cv2.VideoCapture(0)

while True:
    time.sleep(0.5)
    ret, frame = cap.read()
    face_detector = mtcnn.MTCNN()
    face_roi = face_detector.detect_faces(frame)
    if len(face_roi) != 0:
        x,y,width,height = face_roi[0]['box']
        x1, y1 = x+width, y+height
        face = frame[y:y1, x:x1]

        face_gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        crop = np.expand_dims(np.expand_dims(cv2.resize(face_gray, (224, 224)), -1), 0)
        emotion_prediction = emotion_model.predict(crop)
        maxindex = int(np.argmax(emotion_prediction))
        cv2.putText(frame, emotion_dict[maxindex], (x+5, y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
        cv2.rectangle(frame, (x, y-50), (x+width, y+height+50), (0,0,255), 4)
    
    cv2.imshow('Face Dectection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
