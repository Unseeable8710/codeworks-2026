# Simple blink led sketch using GPIO pins on a Raspberry Pi

from gpiozero import LED
from time import sleep

led = LED(17)

while True:
  led.on()
  sleep(0.2)
  led.off()
  sleep(0.2)
