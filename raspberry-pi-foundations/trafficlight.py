from gpiozero import LED
from time import sleep

red = LED(17)
yellow = LED(27)
green = LED(22)

red.off()
yellow.off()
green.off()

while True:
  green.on()
  sleep(3)
  green.off()
  yellow.on()
  sleep(1)
  yellow.off()
  red.on()
  sleep(3)
  red.off()
  
