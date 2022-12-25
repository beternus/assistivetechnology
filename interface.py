#from cProfile import label   
from PySide2.QtWidgets import(QApplication, QMainWindow, QWidget, QLabel)
from tela1 import Ui_Dialog
#from tela2 import Ui_Form
from tela3 import Ui_Form
import sys
from math import acos, degrees

#from turtle import delay
import time # Provides time-related functions
import cv2 # OpenCV library      //importa as bibliotecas
import mediapipe as mp
import numpy as np
#import RPi.GPIO as GPIO
#import threading
#import keyboard

#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

#GPIO.setup(16, GPIO.OUT)
#GPIO.setup(12, GPIO.OUT)
#GPIO.setup(18, GPIO.OUT)
#GPIO.setup(23, GPIO.OUT)

#GPIO.output(16, GPIO.HIGH)
#GPIO.output(12, GPIO.LOW)

#pwm = GPIO.PWM(18, 500)
#pwm.start(100)

#pwm2 = GPIO.PWM(23, 500)
#pwm2.start(100)

def calculate_angle(a,b,c):   //funcao que calcula o angulo de flexao/extensao
    a = np.array(a) # Primeiro
    b = np.array(b) # Segundo
    c = np.array(c) # último
    
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)   //aparentemente conversao para unidade de referencia
    
    if angle > 180.0:
        angle = 360-angle
        
    return angle


#cap = cv2.VideoCapture(0)
 

counter = 0
stage = "cima"
repeticoes = 0
anguloflexao = 0
#70
anguloextensao = 0
#150
up = False
down = False
count = 0


class tela1(QMainWindow, Ui_Dialog):
    def __init__(self):
        super(tela1, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Smart CPM")

        self.pushButton.clicked.connect(self.open_tela2)

        self.pushButton_2.clicked.connect(self.fecha_tela1)

    
    def fecha_tela1(self):
        self.close()
        
        
    def open_tela2(self):
        global repeticoes
        repeticoes = self.lineEdit.text()
        repeticoes = int(repeticoes)

        global anguloextensao
        anguloextensao = self.lineEdit_2.text()    //calcula o angulo de extensao
        anguloextensao = int(anguloextensao)

        global anguloflexao
        anguloflexao = self.lineEdit_3.text()
        anguloflexao = int(anguloflexao)
        
        def iniciar():
            
            #global repeticoes
            #self.label_6.setNum(repeticoes)
            
            #self.pushButton.clicked.connect(self.parar)
            
            mp_drawing = mp.solutions.drawing_utils
            mp_pose = mp.solutions.pose
            pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
                            
            cap = cv2.VideoCapture(0)

            while cap.isOpened():
                
                global up, down, count, stage
                
                ret, frame = cap.read()
                if ret == False:
                   break
                #frame = cv2.flip(frame, 1)
                height, width, _ = frame.shape
                
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                
                results = pose.process(frame_rgb)
                
                
                if results.pose_landmarks is not None:
                    x1 = int(results.pose_landmarks.landmark[24].x * width)
                    y1 = int(results.pose_landmarks.landmark[24].y * height)
                    x2 = int(results.pose_landmarks.landmark[26].x * width)
                    y2 = int(results.pose_landmarks.landmark[26].y * height)
                    x3 = int(results.pose_landmarks.landmark[28].x * width)
                    y3 = int(results.pose_landmarks.landmark[28].y * height)
                    p1 = np.array([x1, y1])
                    p2 = np.array([x2, y2])
                    p3 = np.array([x3, y3])
                    l1 = np.linalg.norm(p2 - p3)
                    l2 = np.linalg.norm(p1 - p3)
                    l3 = np.linalg.norm(p1 - p2)
                    
                    # Calcular angulo
                    angle = degrees(acos((l1**2 + l3**2 - l2**2) / (2 * l1 * l3)))
                                        
                    if angle >= 150:
                        up = True
                        
                    if up == True and down == False and angle <= anguloflexao:
                        #GPIO.output(16, GPIO.LOW)
                        #GPIO.output(12, GPIO.LOW)
                        down = True
                        stage="cima"
                        count += 1
                        
                    if up == True and down == True and angle >= anguloextensao and stage =='cima':
                        #GPIO.output(16, GPIO.HIGH)
                        #GPIO.output(12, GPIO.HIGH)
                        stage = "baixo"
                        up = False
                        down = False

                    if count >= repeticoes:
                        #GPIO.output(16, GPIO.HIGH)
                        #GPIO.output(12, GPIO.LOW)
                        count = 0
                        self.w = tela3()
                        self.w.show()
                        self.close()
                        break
                        
                    #print("count: ", count)
                    # Vizualização
                    aux_image = np.zeros(frame.shape, np.uint8)
                    cv2.line(aux_image, (x1, y1), (x2, y2), (255, 255, 255), 20)
                    cv2.line(aux_image, (x2, y2), (x3, y3), (255, 255, 255), 20)
                    cv2.line(aux_image, (x1, y1), (x3, y3), (255, 255, 255), 5)
                    contours = np.array([[x1, y1], [x2, y2], [x3, y3]])
                    cv2.fillPoly(aux_image, pts=[contours], color=(0, 0, 0))
                    output = cv2.addWeighted(frame, 1, aux_image, 0.8, 0)
                    cv2.circle(output, (x1, y1), 6, (1, 1, 190), 4)
                    cv2.circle(output, (x2, y2), 6, (1, 1, 190), 4)
                    cv2.circle(output, (x3, y3), 6, (1, 1, 190), 4)
                    
                    #cv2.rectangle(output, (0, 0), (60, 60), (0, 0, 0), -1)
                    cv2.putText(output, str(int(angle)), (x2 + 30, y2), 1, 1.5, (254, 254, 254), 2)
                    #cv2.putText(output, str(count), (10, 50), 1, 3.5, (254, 254, 254), 2)
                    
                    #cv2.rectangle(image, (0,0), (270,70), (245,117,16), -1)
                    
                    # Caixa de status
                    cv2.rectangle(output, (0,0), (270,70), (245,117,16), -1)
                
                    # Repetições
                    cv2.putText(output, 'REP.', (20,12), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
                    cv2.putText(output, str(count), 
                                (10,60), 
                                cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
                    
                    # Status
                    cv2.putText(output, 'STATUS', (150,12), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
                    cv2.putText(output, stage, 
                                (100,60), 
                                cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
                    
                    cv2.imshow("output", output)


                if cv2.waitKey(10) & 0xFF == ord('q'):
                    count = 0
                    #GPIO.output(16, GPIO.HIGH)
                    #GPIO.output(12, GPIO.LOW)
                    self.w = tela1()
                    self.w.show()
                    self.close()
                    break
                    
            cap.release()
            cv2.destroyAllWindows()
            #cap.release()
            #cv2.destroyWindow(results)
            #cv2.destroyWindow('Projeto')      
            #time.sleep(2)
        
        iniciar()
        
class tela3(QMainWindow, Ui_Form):
    def __init__(self):
        super(tela3, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Smart CPM")

        self.pushButton_2.clicked.connect(self.sair)
        self.pushButton.clicked.connect(self.reiniciar)
    
    def reiniciar(self):
        self.t1 = tela1()
        self.t1.show()
        self.close()
        global repeticoes
        repeticoes = 0 
        counter = 0

    def sair(self):
        self.close()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = tela1()
    window.show()
    app.exec_()
