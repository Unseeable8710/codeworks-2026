import random
# import keyboard

name = "Colton Stone"
age = "15"
grade = "10th"
interests = "music, gaming, and coding"
hereBc = "I joined because I wanted a summer job that I was actually interested in, and I'm into computers and stuff."
goals = "I want to learn to be able to use a Raspberry Pi"
personality = ["Error: could not locate brain", "Error: could not interpret behaviors", "Error: could not find personality"]
n = 0

def proceed():
  global n
  match n:
    case 0:
      print("\nMy name is " + name)
    case 1:
      print("\nI'm " + str(age) + " years old")
    case 2:
      print("\nI'm in " + grade)
    case 3:
      print("\nMy main interests are " + interests)
    case 4:
      print("\n" + hereBc)
    case 5:
      print("\n" + goals)
    case 6:
      print(personality[random.randint(0, 2)])
    case 7:
      # print("Press ENTER to exit...")
      # keyboard.wait("enter")
      input("Press ENTER to exit...")
      exit()
  n += 1

while n >= 0 & n <= 6:
  # print("Press ENTER to continue...")
  # keyboard.wait("enter")
  input("Press ENTER to continue...")
  proceed()
