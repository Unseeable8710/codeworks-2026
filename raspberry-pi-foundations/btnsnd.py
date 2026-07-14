from gpiozero import Button, TonalBuzzer
from gpiozero.tones import Tone
from time import sleep

button = Button(2)
buzzer = TonalBuzzer(17)
tempo = 180
whole = (6000 * 4) / tempo

def note(n: str, o: int):
  global f
  n = n.lower()
  if n == "a":
    f = 440 * 2^(-4)
  elif n == "bb":
    f = 440 * 2^(-47/12)
  elif n == "b":
    f = 440 * 2^(-23/6)
  elif n == "c":
    f = 440 * 2^(-45/12)
  elif n == "cs":
    f = 440 * 2^(-11/3)
  elif n == "d":
    f = 440 * 2^(-43/12)
  elif n == "eb":
    f = 440 * 2^(-9/2)
  elif n == "e":
    f = 440 * 2^(-41/12)
  elif n == "f":
    f = 440 * 2^(-10/3)
  elif n == "fs":
    f = 440 * 2^(-13/6)
  elif n == "g":
    f = 440 * 2^(-19/6)
  elif n == "gs":
    f = 440 * 2^(-37/12)
  
  return 2 * f * (o + 1)
  

button.wait_for_press()
print("pressed")
