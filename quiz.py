# This module let's me use random numbers for the math questions.
import random
# This module let's me pause the program and much more.
import time

# This is a list for yes or no
N = ["No", "no", "N", "n"]
Y = ["Yes", "yes", "Y", "y"]

# Ask for the player's name
while True:
    name = input("What is your name?: ")
    if name.strip():  # Check if the input is not empty or just whitespace
        break
    else:
        print("Name cannot be empty. Please enter your name.")

# Ask if they want to play the game
while True:
    asking = input("Would you like to play the game???(Y/N): ")
    if asking in N:
        print("Oh ok ):")
        exit()
    elif asking in Y:
        print("Ok, let's introduce you to the math quiz game.")
        break
    else:
        print("Please answer Y or N.")

# Introduce the game
print("Welcome to the Simple Math Quiz")
time.sleep(2)  # Wait 2 second
print("In this math quiz, you will be asked questions, and you have to answer them correctly to get a high score.")
time.sleep(2)  # Wait 2 second

# Ask the player how many questions they want to answer
while True:
    try:
        question_amount = int(input("How many questions would you like to answer? (Max 20): "))
        if 1 <= question_amount <= 20:
            break
        else:
            print("Please enter a number between 1 and 20.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Tell them the amount of questions that they are going to be answering
print(f"You have chosen to answer {question_amount} questions.")
time.sleep(1)  # Wait 1 second

# Ask them which mode they want to play
while True:
    mode = input("What mode do you want to play?: Multiplication(x), Division(/), Subtraction(-), Addition(+). (write the symbol with the mode you want to play): ")
    if mode in ["x", "/", "-", "+"]:
        break
    else:
        print("Please enter either: x, /, -, +.")

# Give them a countdown
print(f"OK {name}, ready? Let's go!")
print("3")
time.sleep(1)  # Wait 1 second
print("2")
time.sleep(1)  # Wait 1 second
print("1")
time.sleep(1)  # Wait 1 second
print("GO!")

# Create variables to track the score (a = correct answer, b = incorrect answers)
a = 0
b = 0

# Define functions for each question type
def question_multiply():
    global a, b
    for _ in range(question_amount):
        question_time1 = random.randint(1, 10)
        question_time2 = random.randint(1, 10)
        answer = question_time1 * question_time2
        print(f"What is {question_time1} times {question_time2}: ")
        player_answer = input()
        if player_answer.isdigit() and int(player_answer) == answer:
            print("Correct!")
            a += 1
        else:
            print("Incorrect!")
            b += 1

def question_addition():
    global a, b
    for _ in range(question_amount):
        question_time1 = random.randint(1, 30)
        question_time2 = random.randint(1, 30)
        answer = question_time1 + question_time2
        print(f"What is {question_time1} plus {question_time2}: ")
        player_answer = input()
        if player_answer.isdigit() and int(player_answer) == answer:
            print("Correct!")
            a += 1
        else:
            print("Incorrect!")
            b += 1

def question_division():
    global a, b
    for _ in range(question_amount):
        question_time2 = random.randint(1, 10)
        answer = random.randint(1, 10)
        question_time1 = answer * question_time2  # Ensure the division results in an integer
        print(f"What is {question_time1} divided by {question_time2}: ")
        player_answer = input()
        if player_answer.isdigit() and int(player_answer) == answer:
            print("Correct!")
            a += 1
        else:
            print("Incorrect!")
            b += 1

def question_subtraction():
    global a, b
    for _ in range(question_amount):
        question_time1 = random.randint(1, 30)
        question_time2 = random.randint(1, 30)
        answer = question_time1 - question_time2
        print(f"What is {question_time1} take away {question_time2}: ")
        player_answer = input()
        if player_answer.isdigit() and int(player_answer) == answer:
            print("Correct!")
            a += 1
        else:
            print("Incorrect!")
            b += 1

# Call the appropriate function based on the chosen mode
if mode == "x":
    question_multiply()
elif mode == "/":
    question_division()
elif mode == "+":
    question_addition()
elif mode == "-":
    question_subtraction()

# Print the score
while True:
    asking_score = input('Would you like your score? (Y/N): ').strip()
    if asking_score in Y:
        print(f"Your score: {a}/{question_amount}")
        break
    elif asking_score in N:
        print("Ok thanks for playing the game (:")
        break
    else:
        print("Do you want your score? yes or no: ")
