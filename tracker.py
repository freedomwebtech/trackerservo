import cv2
from time import sleep
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
servo_pin = 23


GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin,GPIO.OUT)

pwm = GPIO.PWM(servo_pin,50)


TrDict={'csrt':cv2.TrackerCSRT_create}
tracker=TrDict['csrt']()
cap=cv2.VideoCapture(0)
ret,frame=cap.read()
frame=cv2.resize(frame,(640,480))
bb=cv2.selectROI(frame)
tracker.init(frame,bb)


count=0
pwm.start(0)
  

    


    
def track(img):
    success,box=tracker.update(img)
    if success:
        (x,y,w,h)=[int(a)for a in box]
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cx = (x + x + w) // 2
        cy = (y + y + h) // 2
        cv2.circle(img,(cx,cy),5,(0,0,255),-1)
        cv2.line(img,(cx,0),(cx,480),(0,0,255),2)
        a=int(cx)//65
    

        pwm.start(a)
        print(a)

   

  
while True:
    ret,frame=cap.read()
    count += 1
    if count % 10 != 0:
        continue
    frame=cv2.resize(frame,(640,480))
    frame=cv2.flip(frame,1)
    track(frame)

           
    cv2.imshow("FRAME",frame)
    if cv2.waitKey(1)&0xFF==27:
        break
cap.release()
pwm.start(0)
cv2.destroyAllWindows()
