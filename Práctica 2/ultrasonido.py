import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup (PIN,GPIO.IN)
GPIO.setup (PIN,GPIO.OUT)
