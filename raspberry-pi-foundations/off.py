from gpiozero import LED
from time import sleep

red = LED(17)
yellow = LED(27)
green = LED(22)

red.off()
yellow.off()
green.off()
