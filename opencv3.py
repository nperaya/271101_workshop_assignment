#This code demonstrate how to show location of hand landmark
import cv2
import mediapipe as mp
import numpy as np
import math


    
    

Nfing = 5
cap = cv2.VideoCapture(0)

#Call hand pipe line module
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                
                if id == 4:
                    id4 = int(id)
                    cx4 = cx
                if id == 3:
                    id3 = int(id)
                    cx3 = cx
                if id == 8:
                    cy8 = cy
                if id == 7:
                    cy7 = cy
                if id == 12:
                    cy12 = cy
                if id == 11:
                    cy11 = cy
                if id == 16:
                    cy16 = cy
                if id == 15:
                    cy15 = cy
                if id == 20:
                    cy20 = cy
                if id == 19:
                    cy19 = cy
                if id == 5:
                    cx5 = cx
                if id == 17:
                    cx17 = cx 

            if cx4 > cx3 and cx5 > cx17: 
                cv2.putText(img, "niw phong", (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (183, 226, 234), 3)
            if cx4 < cx3 and cx5 < cx17: 
                cv2.putText(img, "niw phong", (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (183, 226, 234), 3)

            if cy7 > cy8:
                cv2.putText(img, "niw chee", (10, 120), cv2.FONT_HERSHEY_PLAIN, 3,
                (73, 191, 252), 3)
            
            if cy11 > cy12:
                cv2.putText(img, "niw glang", (10, 170), cv2.FONT_HERSHEY_PLAIN, 3,
                (0, 127, 247), 3)

            if cy15 > cy16:
                cv2.putText(img, "niw nang", (10, 220), cv2.FONT_HERSHEY_PLAIN, 3,
                (40, 40, 214), 3)

            if cy19 > cy20:
                cv2.putText(img, "niw goy", (10, 270), cv2.FONT_HERSHEY_PLAIN, 3,
                (73, 48, 0), 3)
            
            else:
                Nfing = 5
                    
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    
    
    cv2.imshow("Image", img)
    k =cv2.waitKey(1)
    if k == ord('q'):
        break

    
#Closeing all open windows
#cv2.destroyAllWindows()