# Please install 'pyttsx3' first to enjoy audio feature. This Programme also can work without it but there will be no audio feature.

import pyttsx3
import random


try:
  engine = pyttsx3.init('sapi5')
  voices = engine.getProperty('voices')
  engine.setProperty('voice', voices[1].id)


  def speak(audio):
    engine.say(audio)
    engine.runAndWait()


  random_num = random.randint(10, 40)
  the_number = random_num
  i = 10

  print("-===Welcome to the Rayhan Mahmud's gussing game===- \n ")
  speak("Welcome to the Rayhan Mahmud's gussing game ")
  print("***INTRODUCTION: \n *//The game is about to guss a number from some clues. You will be get 10 chances to guss the number correctly. If you can guss the number in this 10 chances you will be declare as winner. If you can't then you will be loss..")
  speak("INTRODUCTION: \n The game is about to guss a number from some clues. You will be get 10 chances to guss the number correctly. If you can guss the number in this 10 chances you will be declare as winner. If you can't then you will be loss..")
  print("***RULES: \n 1. You have to guss the number under 10 chances. \n 2. Your input must have to be a number. ")
  speak("RULES: \n  You have to guss the number under 10 chances. \n Your input must have to be a number. ")
  print("***CLUES: \n 1. The number is a posetive number. \n 2. The number is under 60.")
  speak("CLUES: \n  The number is a posetive number. \n  The number is under 60.")
  while True:

    # functionals
    speak("Enter your gussing number")
    user_input = int(input("Enter your gussing number:"))

    i = i - 1
    if user_input == the_number:
        print("Congratulations! You correctly guss the number..")
        speak("Congratulations! You correctly guss the number..")
        print("Number of chances you took to finish ", "=", " ", 10 - i)
        speak("Number of chances you took to finish ")
        speak(10 - i)
        break
    elif i == 0:
        print("game over boss..")
        speak("game over boss..")
        print("Think wisely and follow my clues!")
        speak("Think wisely and follow my clues!")
        print("The right answer is ", the_number)
        speak("The right answer is ")
        speak(the_number)
        break

# clues

    elif user_input > the_number + 10 and i < 9:
        print("You are too far from the number...")
        speak("You are too far from the number...")
        print("Try again. Never give up!")
        speak("Try again. Never give up!")
        print("Your gussing opportunity left ", "=", " ", i)
        speak("Your gussing opportunity left ")
        speak(i)
        print("#Clue: The number is less than 40 and more than 10..")
        speak("Clue: The number is less than 40 and more than 10..")
        continue

    elif (user_input + 5 == the_number and i < 8):
        print("Increase little bit more...")
        speak("Increase little bit more...")
        print("Your gussing opportunity left ", "=", " ", i)
        speak("Your gussing opportunity left ")
        speak(i)
    elif (user_input - 5 == the_number and i < 8):
        print("Decrease little bit more...")
        speak("Decrease little bit more...")
        print("Your gussing opportunity left ", "=", " ", i)
        speak("Your gussing opportunity left ")
        speak(i)

    elif user_input < the_number - 10 and i < 8:
        print("You are too far from the number...")
        speak("You are too far from the number...")
        print("Increase the number..")
        speak("Increase the number..")
        print("Your gussing opportunity left ", "=", " ", i)
        speak("Your gussing opportunity left ")
        speak(i)
        print("#Clue: The number is less than 40 and more than 10..")
        speak("Clue: The number is less than 40 and more than 10..")
        continue

    elif user_input + 2 == the_number or user_input - 2 == the_number and i < 8:
        print("Decrease little bit or incrase little bit..! You are near to the victory.")
        speak("Decrease little bit or increase little bit..! You are near to the victory.")
        print("Never give up!")
        speak("Never give up!")
        print("Your gussing opportunity left ", "=", " ", i)
        speak("Your gussing opportunity left ")
        speak(i)
        continue


# ending
    elif user_input != the_number and the_number % 2 == 0 and i < 6:
        print("Wrong gussing!")
        speak("Wrong gussing!")
        print("#Clue: The number is a Even number.")
        speak("Clue: The number is a Even number.")
        print("Your gussing opportunity left ", "=", " ", i)
        speak("Your gussing opportunity left ")
        speak(i)
        continue
    elif user_input != the_number and the_number % 2 != 0 and i < 6:
        print("Wrong gussing!")
        speak("Wrong gussing!")
        print("#Clue: The number is a Odd number.")
        speak("Clue: The number is a Odd number.")
        print("Your gussing opportunity left ", "=", " ", i)
        speak("Your gussing opportunity left ")
        speak(i)
        continue

    elif user_input != the_number:
        print("Wrong gussing!")
        speak("Wrong gussing!")
        print("Try again. Never give up!")
        speak("Try again. Never give up!")
        print("Your gussing opportunity left ", "=", " ", i)
        speak("Your gussing opportunity left ")
        speak(i)
        continue

    else:
        print("Input Error! Enter a valid input...")
        speak("Input Error! Enter a valid input...")












# witout audio feature
# please install 'pyttsx3' module to enjoy audio feature

except Exception as e:
  print(e)
  random_num = random.randint(10, 40)
  the_number = random_num
  i = 10

  print("-===Welcome to the Rayhan Mahmud's gussing game===- \n ")
  print("***INTRODUCTION: \n *//The game is about to guss a number from some clues. You will be get 10 chances to guss the number correctly. If you can guss the number in this 10 chances you will be declare as winner. If you can't then you will be loss..")
  print("***RULES: \n 1. You have to guss the number under 10 chances. \n 2. Your input must have to be a number. ")
  print("***CLUES: \n 1. The number is a posetive number. \n 2. The number is under 60.")
  while True:

    # functionals
    user_input = int(input("Enter your gussing number:"))

    i = i - 1
    if user_input == the_number:
        print("Congratulations! You correctly guss the number..")
        print("Number of chances you took to finish ", "=", " ", 10 - i)
        break
    elif i == 0:
        print("game over boss..")
        print("Think wisely and follow my clues!")
        print("The right answer is ", the_number)
        break


# clues
    elif user_input > the_number + 10 and i < 9:
        print("You are too far from the number...")
        print("Try again. Never give up!")
        print("Your gussing opportunity left ", "=", " ", i)
        print("#Clue: The number is less than 40 and more than 10..")
        continue

    elif (user_input + 5 == the_number and i < 8):
        print("Increase little bit more...")
        print("Your gussing opportunity left ", "=", " ", i)
    elif (user_input - 5 == the_number and i < 8):
        print("Decrease little bit more...")
        print("Your gussing opportunity left ", "=", " ", i)

    elif user_input < the_number - 10 and i < 8:
        print("You are too far from the number...")
        print("Increase the number..")
        print("Your gussing opportunity left ", "=", " ", i)
        print("#Clue: The number is less than 40 and more than 10..")
        continue

    elif user_input + 2 == the_number or user_input - 2 == the_number and i < 8:
        print("Decrease little bit or incrase little bit..! You are near to the victory.")
        print("Never give up!")
        print("Your gussing opportunity left ", "=", " ", i)
        continue


# ending
    elif user_input != the_number and the_number % 2 == 0 and i < 6:
        print("Wrong gussing!")
        print("#Clue: The number is a Even number.")
        print("Your gussing opportunity left ", "=", " ", i)
        continue
    elif user_input != the_number and the_number % 2 != 0 and i < 6:
        print("Wrong gussing!")
        print("#Clue: The number is a Odd number.")
        print("Your gussing opportunity left ", "=", " ", i)
        continue

    elif user_input != the_number:
        print("Wrong gussing!")
        print("Try again. Never give up!")
        print("Your gussing opportunity left ", "=", " ", i)
        continue

    else:
        print("Input Error! Enter a valid input...")
