import cv2
import numpy as np
from keras.models import model_from_json


#emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}
#emotion_dict = {0: "neutral", 1: "fear", 2: "disgust", 3: "sadness", 4: "happy", 5: "anger", 6: "sad", 7: "surprise"}
emotion_dict = {0: "angry", 1: "contempt", 2: "disgust", 3: "fear", 4: "happy", 5: "neutral", 6: "sad", 7: "surprise"}

# load json and create model
json_file = open('affect_model_200.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
emotion_model = model_from_json(loaded_model_json)

# load weights into new model
emotion_model.load_weights("affect_model_200.h5")
print("Loaded model from disk")

# start the webcam feed
cap = cv2.VideoCapture(0)

# pass here your video path
# you may download one from here : https://www.pexels.com/video/three-girls-laughing-5273028/
#cap = cv2.VideoCapture("C:\\JustDoIt\\ML\\Sample_videos\\emotion_sample6.mp4")

while True:
    # Find haar cascade to draw bounding box around face
    ret, frame = cap.read()
    frame = cv2.resize(frame, (1280, 720))
    if not ret:
        break
    #face_detector = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
    face_detector = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt.xml')
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect faces available on camera
    num_faces = face_detector.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

    # take each face available on the camera and Preprocess it
    for (x, y, w, h) in num_faces:
        cv2.rectangle(frame, (x, y-50), (x+w, y+h+10), (0, 255, 0), 4)
        roi_gray_frame = gray_frame[y:y + h, x:x + w]
        cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray_frame, (224, 224)), -1), 0)

        # predict the emotions
        emotion_prediction = emotion_model.predict(cropped_img)
        maxindex = int(np.argmax(emotion_prediction))
        print("Max :", maxindex)
        print(emotion_prediction)

        emotion = emotion_dict[maxindex]

        if emotion == "fear" or emotion == "angry" or emotion == "disgust":
            quadrant = "Q2"
        elif emotion == "sadness":
            quadrant == "Q3"
        elif emotion == "happy" or emotion == "surprise":
            quadrant = "Q1"
        elif emotion == "contempt":
            quadrant = "Q4"
        elif emotion == "neutral":
            quadrant = "QN"

        cv2.putText(frame, quadrant, (x+5, y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow('Emotion Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
