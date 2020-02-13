import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup (PIN,GPIO.IN)

while True:

input_value = GPIO.input(PIN)
if input_value == False:
  print("El boton ha sido presionado")
  while input == False:
    input_value = GPIO.input(PIN)

