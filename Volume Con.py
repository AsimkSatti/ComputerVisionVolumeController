import cv2
import numpy as np

import argparse
import random
import time

import time
from pythonosc import osc_message_builder
from pythonosc import udp_client
import pynput
import time
from pynput.mouse import Button, Controller
mouse = Controller()



 
 

#Identifies Face
face_cascade =cv2.CascadeClassifier('haarcascade_closedhand.xml')
#Identifies Eyes
#eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')

# When Testing leave camera on
#But remember no two applications can use the simultaneously camera,
cap=cv2.VideoCapture(0)

 
        
#Class as we may want to send data about multiple faces     
class hand:
    def __init__(self):
        #Ultimately want to find the center
        self.width_center=0
        self.height_center=0
        
   
    
    def FindHand(self):
        arr=[]
        while True:
            #Convert to gray scale
            ret, img= cap.read()
            gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            #Size of detection
            faces=face_cascade.detectMultiScale(gray, 1.2,5)

            for(x,y,w,h) in faces:
                #Visual
                cv2.rectangle(img, (x,y), (x+w, y+h), (255,120,0),2)
                roi_gray=gray[y:y+h, x:x+w]
                roi_color=img[y:y+h , x:x+w]

                print(y)
                arr.append(y)
                while len(arr)>=30:
                    averageOne=(arr[0]+arr[5]+arr[7])/3
                    averageTwo=(arr[10]+arr[15]+arr[18])/3
                    if(averageOne-averageTwo>20):
                        mouse.position=(233,760)
                        time.sleep(1)
                        mouse.click(Button.right,1)
                        
                        for i in range(0,13):
                            time.sleep(0.1)
                            mouse.move(0,-7)
                             
                        mouse.press(Button.left)
                        for clicker in range(0,5):
                           
                            time.sleep(0.5)
                            mouse.move(0,-3)
                            print('f')
                        

                        mouse.release(Button.left)
                    if len(arr)>=30:
                        arr=[]

                        

    
  
               
            #Output
            cv2.imshow('img', img)
            breaker=cv2.waitKey(30) &0xff
            #Destroy program with space key
            if breaker==32:
                break
        cap.release()
        cv2.destroyAllWindows


        
 


        
if __name__ == "__main__":
    my_hand=hand()
    my_hand.FindHand()
 
    
