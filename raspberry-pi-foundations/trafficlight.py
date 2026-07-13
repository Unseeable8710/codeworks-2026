from gpiozero import LED
from time import sleep

red = LED(17)
yellow = LED(27)
green = LED(22)

while True:
  red.off()
  yellow.off()
  green.on()
  sleep(3)

  green.off()
  red.off()
  yellow.on()
  sleep(1)

  yellow.off()
  green.off()
  red.on()
  sleep(3)
