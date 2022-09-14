import RPi.GPIO as GPIO
# from controller.lcd import lcd
import time


Motor1A = 35
Motor1B = 36
Motor2A = 37
Motor2B = 38

def config():
    LED = 26
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Motor1A,GPIO.OUT)  # All pins as Outputs
    GPIO.setup(Motor1B,GPIO.OUT)
    GPIO.setup(Motor2A,GPIO.OUT)  # All pins as Outputs
    GPIO.setup(Motor2B,GPIO.OUT)

def moters(moter_no): 
    config()
    # lcd.clear()
    time.sleep(1)
    if(moter_no == 1):
        print("Entry Gate is open")
        # lcd.message('Entry Gate Open\nPlease Park Car')
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.LOW)
        time.sleep(0.0042)
        GPIO.output(Motor1A,GPIO.LOW)
        GPIO.output(Motor1B,GPIO.LOW)
        time.sleep(2)
        GPIO.output(Motor1A,GPIO.LOW)
        GPIO.output(Motor1B,GPIO.HIGH)
        time.sleep(0.0042)
        GPIO.output(Motor1A,GPIO.LOW)
        GPIO.output(Motor1B,GPIO.LOW)
    else:
         print("Exit gate is open")
        #  lcd.message("Succesfully Paid\n   Your Bill")
         time.sleep(2)
        #  lcd.clear()
        #  lcd.message("Exit Gate Open")
        #  lcd.message("\n   Thank You")
         GPIO.output(Motor2A,GPIO.HIGH)
         GPIO.output(Motor2B,GPIO.LOW)
         time.sleep(0.0042)
         GPIO.output(Motor2A,GPIO.LOW)
         GPIO.output(Motor2B,GPIO.LOW)
         time.sleep(2)
         GPIO.output(Motor2A,GPIO.LOW)
         GPIO.output(Motor2B,GPIO.HIGH)
         time.sleep(0.0042)
         GPIO.output(Motor2A,GPIO.LOW)
         GPIO.output(Motor2B,GPIO.LOW)
    # lcd.clear()
