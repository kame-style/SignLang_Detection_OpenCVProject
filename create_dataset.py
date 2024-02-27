import os
import pickle

import mediapipe as mp
import cv2
import matplotlib.pyplot as plt


mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

DATA_DIR = './data/asl_alphabet_train/asl_alphabet_train/'

count = 0
data = []
labels = []
for dir_ in os.listdir(DATA_DIR):
    for img_path in os.listdir(os.path.join(DATA_DIR, dir_)):
        if(count==10):
            count=0
            break
        count+=1
        data_aux = []

        x_ = []
        y_ = []

        img = cv2.imread(os.path.join(DATA_DIR, dir_, img_path))
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        results = hands.process(img_rgb)                                     ##Detects all the landmarks

        ## Storing all the landmarks in list to train
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y

                    x_.append(x)
                    y_.append(y)

                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_aux.append(x - min(x_))
                    data_aux.append(y - min(y_))
            
            data.append(data_aux)    ## data for training containing all the landmark points (x,y)
            labels.append(dir_)      ## list containing all the labels for each class(alphabet)

##testing
def print_shape(lst):
    for item in lst:
        print("len: ", len(item))
        print(item)


print(len(data))
print(len(labels))
print_shape(data)
print_shape(labels)

##

d = open('data.pickle', 'wb')
pickle.dump(data, d)
d.close()
l = open('lables.pickle', 'wb')
pickle.dump(labels, l)
l.close()
