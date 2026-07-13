from gpiozero import LED
from time import sleep

red = LED(17)
yellow = LED(27)
green = LED(22)

while True:
  green.on()
  red.off()
  yellow.off()
  sleep(3)
  
  yellow.on()
  green.off()
  red.off()
  sleep(1)
  
  red.on()
  yellow.off()
  green.off()  
  sleep(3)
