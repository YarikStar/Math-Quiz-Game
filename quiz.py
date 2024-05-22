# This module let's me use random numbers for the math questions.
import random
# This module let's me pause the program and much more.
import time
# This is a list for yes or no
N = ["No", "no", "N", "n"]
Y = ["Yes", "yes", "Y", "y"]

# Ask for the player's name
name = input("What is your name?: ")

# Ask if they want to play the game
asking = input("Would you like to play the game???(Y/N): ")
if asking in N:
    print("Oh ok ):")
    exit()
elif asking in Y:
    print("Ok, let's introduce you to the math quiz game.")
else:
    exit()

# Introduce the game
print("Welcome to the Simple Math Quiz")
time.sleep(2)
print("In this math quiz, you will be asked questions, and you have to answer them correctly to get a high score.")
time.sleep(2)
print('''The questions will appear quickly.
You have to answer each question in 10 seconds or the game will end.''')

time.sleep(2)

# Ask the player how many questions they want to answer
question_amount = int(input("How many questions would you like to answer?(Max 20): "))
# Ask them Which mode they want to play
mode = str(input("What mode do you want to play?: Multiplication(x), Division(/), Subtraction(-), Addition(+). (write which one you want to play): "))

# Give them a countdown
print(f"OK {name}, ready? Let's go!")
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("GO!")

# Create variables to track the score (a = correct answer, b = incorrect answers)
a = 0
b = 0

# 10 second timer
def countdown_timer(seconds):
    start_time = time.time()
    elapsed_time = 0
    while elapsed_time < seconds:
        time.sleep(1)  # Wait for 1 second
        elapsed_time = time.time() - start_time
        remaining_time = seconds - elapsed_time
        # Update the display
        print("\rTime remaining: {:.2f} seconds".format(remaining_time), end="")
    print("\nTime's up!")

# This function lets me use multiply questions for the selection of type of question
def question_multiply():
    for i in range(question_amount):
        question_time1 = random.randint(1, 10)
        question_time2 = random.randint(1, 10)
        answer = question_time1 * question_time2
        print(f"What is {question_time1} times {question_time2}: ")
        player_answer = input()
        if player_answer.isdigit() and int(player_answer) == answer:
            print("Correct!")
            global a
            a += 1
        else:
            print("Incorrect!")
            global b
            b += 1

def question_addition():
    for i in range(question_amount):
        question_time1 = random.randint(1, 30)
        question_time2 = random.randint(1, 30)
        answer = question_time1 + question_time2
        print(f"What is {question_time1} plus {question_time2}: ")
        player_answer = input()
        if player_answer.isdigit() and int(player_answer) == answer:
            print("Correct!")
            global a
            a += 1
        else:
            print("Incorrect!")
            global b
            b += 1

def question_division():
    for i in range(question_amount):
        question_time1 = random.randint(1, 100)
        question_time2 = random.randint(1, 100)
        answer_division = question_time1 / question_time2
        print(f"What is {question_time1} divided by {question_time2}: ")
        player_answer = input()
        if player_answer.isdigit() and int(player_answer) == answer:
            print("Correct!")
            global a
            a += 1
        else:
            print("Incorrect!")
            global b
            b += 1

def question_subtraction():
    for i in range(question_amount):
        question_time1 = random.randint(1, 30)
        question_time2 = random.randint(1, 30)
        answer_multiply = question_time1 - question_time2
        print(f"What is {question_time1} take away {question_time2}: ")
        player_answer = input()
        if player_answer.isdigit() and int(player_answer) == answer:
            print("Correct!")
            global a
            a += 1
        else:
            print("Incorrect!")
            global b
            b += 1
# Call the question function
if mode == "multiplication":
    question_multiply()
elif mode == "division":
    question_division()
elif mode == "addition":
    question_addition()
elif mode == "subtraction":
    question_subtraction()

# Print the score
print(f"Your score: {a}/{question_amount}")
