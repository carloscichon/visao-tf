import cv2
import numpy as np
from keras.models import model_from_json

json_file = open('affect_model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
emotion_model = model_from_json(loaded_model_json)

emotion_model.load_weights("affect_model.h5")
print("Loaded model from disk")

img = cv2.imread("/home/carlos/UFPR/tcc/tcc-carloscichon/affectnet_data_gray/surprise/9752.jpg", cv2.IMREAD_GRAYSCALE)
cropped_img = np.expand_dims(np.expand_dims(cv2.resize(img, (224, 224)), -1), 0)

output = emotion_model.predict(cropped_img)
print(output)