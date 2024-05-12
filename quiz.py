
import random
import time
N = ["No", "no", "N"]
Y = ["Yes", "yes", "Y"]
#ask them if they want to play the game
asking = str(input(print("Would you like to play the game???(Y/N): ")))
if asking == "N":
    print("Oh ok ):")
    exit()
elif asking == "Y":
    print("Ok, lets introduce you to the math quiz game.")
else:
    print("???")
    exit()
#introduce them to the game
print(f"Welcom to the Simple math quiz")
time.sleep(2)
print("In this math quiz you will be asked questions, and you have to anwser them correctly to get a high score.")
time.sleep(2)
print('''
The question will apear quick 
You have to anwser each question in 10 seconds or the question will skip.
If the question skips it will count as an incorect anwser.
''')
time.sleep(2)
print("OK ready? Lets go!")
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("GO!")
#create veriables for the player to save score (a = correct anwser, b = incorect anwsers, c = ran out of time)
a = 0
b = 0
c = 0
