import random
import time
N = ["No", "no", "N"]
Y = ["Yes", "yes", "Y"]
#ask them their name
name = str(input("What is your name?: "))
#ask them if they want to play the game
asking = str(input(print("Would you like to play the game???(Y/N): ")))
if asking in N:
    print("Oh ok ):")
    exit()
elif asking in Y:
    print("Ok, lets introduce you to the math quiz game.")
else:
    print("???")
    exit()

#introduce them to the game
print(f"Welcome to the Simple math quiz")
time.sleep(2)
print("In this math quiz you will be asked questions, and you have to anwser them correctly to get a high score.")
time.sleep(2)
print('''
The question will appear quick 
You have to answer each question in 10 seconds, or the game will end.
''')
time.sleep(2)
#Ask the player how many questions they want to answer.
question_amount = input("How many questions would you like to answer?: ")

#Give them a countdown
print(f"OK {name} ready? Lets go!")
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("GO!")
#create veriables for the player to save score (a = correct anwser, b = incorect anwsers)
a = 0
b = 0
