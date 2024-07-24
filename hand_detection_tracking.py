import cv2
import mediapipe as mp

#initialize landmarks
mp_drawing= mp.solutions.drawing_utils

#initialize connection between landmarks
mp_drawing_styles=mp.solutions.drawing_styles

#initialize hand tracking and hand solution
mphands=mp.solutions.hands

#opens front cam
cap=cv2.VideoCapture(0)

#is a ready model for hand detection along with tracking from previous to be deployed on any image
hands=mphands.Hands()

#runs image continously till ctrl + c is typed in cmd prompt
while True:

    #data is boolean reads if data is received or not and image captures the image 
    data,image=cap.read()

    #flips the image c
    image=cv2.cvtColor(cv2.flip(image,1),cv2.COLOR_RGB2BGR)

    #hand detetcion and tracking used in the image data recievd from cap
    results=hands.process(image)

    #converts color from rgb to bgr since image is flipped
    image=cv2.cvtColor(image,cv2.COLOR_RGB2BGR)

    #checks if there are landmarks
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks( image, hand_landmarks, mphands.HAND_CONNECTIONS)
    cv2.imshow('Handtracker',image)
    cv2.waitKey(1)
