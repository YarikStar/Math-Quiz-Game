import random
import time

# List of inputs for "No" and "Yes" answers
N = ["No", "no", "N", "n"]
Y = ["Yes", "yes", "Y", "y"]

# Function to ask for the player's name
def ask_name():
    while True:
        name = input("What is your name?: ")
        if name.isalpha():  # Ensure the name contains only letters
            return name
        else:
            print("Name can only contain letters and Name can not be empty. Please enter your name.")

# Function to ask if the player wants to play the game
def ask_to_play_game():
    while True:
        asking = input("Would you like to play the game???(Y/N): ")
        if asking in N:
            return False
        elif asking in Y:
            return True
        else:
            print("Invalid input. Please enter Y or N.")

# Function to show the introduction of the game
def show_introduction():
    print("Welcome to the Simple Math Quiz")
    time.sleep(2)
    print("In this math quiz, you will be asked questions, and you have to answer them correctly to get a high score.")
    time.sleep(2)

# Function to ask how many questions the player wants to answer
def ask_number_of_questions():
    while True:
        try:
            question_amount = int(input("How many questions would you like to answer? (Max 20): "))
            if 1 <= question_amount <= 20:
                return question_amount
            else:
                print("Please enter a number between 1 and 20.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Function to ask the game mode
def ask_game_mode():
    while True:
        mode = input("What mode do you want to play?: Multiplication(x), Division(/), Subtraction(-), Addition(+). (write the symbol with the mode you want to play): ")
        if mode in ["x", "-", "+", "/"]:
            return mode
        else:
            print("Please enter either: x, /, -, +")

# Function to ask the difficulty level
def ask_difficulty_level():
    while True:
        difficulty = input("Choose difficulty level: Easy (E), Medium (M), Hard (H): ").strip().upper()
        if difficulty in ["E", "M", "H"]:
            return difficulty
        else:
            print("Invalid input. Please enter E, M, or H.")

# Function to get the range of numbers based on difficulty level
def get_range_by_difficulty(difficulty):
    if difficulty == "E":
        return 1, 10
    elif difficulty == "M":
        return 1, 30
    else:
        return 1, 50

# Function to ask multiplication questions
def question_multiply(question_amount, range_min, range_max):
    correct_answers = 0
    question_history = []
    for _ in range(question_amount):
        question_time1 = random.randint(range_min, range_max)
        question_time2 = random.randint(range_min, range_max)
        answer = question_time1 * question_time2
        while True:
            try:
                player_answer = int(input(f"What is {question_time1} times {question_time2}: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        if player_answer == answer:
            print("Correct!")
            correct_answers += 1
            question_history.append((f"{question_time1} * {question_time2}", player_answer, "Correct", answer))
        else:
            print(f"Incorrect! The correct answer is {answer}.")
            question_history.append((f"{question_time1} * {question_time2}", player_answer, "Incorrect", answer))
    return correct_answers, question_history

# Function to ask addition questions
def question_addition(question_amount, range_min, range_max):
    correct_answers = 0
    question_history = []
    for _ in range(question_amount):
        question_time1 = random.randint(range_min, range_max)
        question_time2 = random.randint(range_min, range_max)
        answer = question_time1 + question_time2
        while True:
            try:
                player_answer = int(input(f"What is {question_time1} plus {question_time2}: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        if player_answer == answer:
            print("Correct!")
            correct_answers += 1
            question_history.append((f"{question_time1} + {question_time2}", player_answer, "Correct", answer))
        else:
            print(f"Incorrect! The correct answer is {answer}.")
            question_history.append((f"{question_time1} + {question_time2}", player_answer, "Incorrect", answer))
    return correct_answers, question_history

# Function to ask division questions
def question_division(question_amount, range_min, range_max):
    correct_answers = 0
    question_history = []
    for _ in range(question_amount):
        question_time2 = random.randint(1, range_max)
        answer = random.randint(1, range_max)
        question_time1 = answer * question_time2
        while True:
            try:
                player_answer = int(input(f"What is {question_time1} divided by {question_time2}: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        if player_answer == answer:
            print("Correct!")
            correct_answers += 1
            question_history.append((f"{question_time1} / {question_time2}", player_answer, "Correct", answer))
        else:
            print(f"Incorrect! The correct answer is {answer}.")
            question_history.append((f"{question_time1} / {question_time2}", player_answer, "Incorrect", answer))
    return correct_answers, question_history

# Function to ask subtraction questions
def question_subtraction(question_amount, range_min, range_max):
    correct_answers = 0
    question_history = []
    for _ in range(question_amount):
        question_time1 = random.randint(range_min, range_max)
        question_time2 = random.randint(range_min, range_max)
        answer = question_time1 - question_time2
        while True:
            try:
                player_answer = int(input(f"What is {question_time1} take away {question_time2}: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        if player_answer == answer:
            print("Correct!")
            correct_answers += 1
            question_history.append((f"{question_time1} - {question_time2}", player_answer, "Correct", answer))
        else:
            print(f"Incorrect! The correct answer is {answer}.")
            question_history.append((f"{question_time1} - {question_time2}", player_answer, "Incorrect", answer))
    return correct_answers, question_history

# Function to save the score to a file
def save_score(name, score, question_amount, mode, difficulty):
    with open("scores.txt", "a") as file:
        file.write(f"Name: {name}, Score: {score}/{question_amount}, Mode: {mode}, Difficulty: {difficulty}\n")

# Function to get the highest score from the file
def get_highest_score():
    try:
        with open("scores.txt", "r") as file:
            scores = file.readlines()
            highest_score = 0
            highest_scorer = ""
            for line in scores:
                parts = line.split(", ")
                score_part = parts[1]
                score = int(score_part.split(": ")[1].split("/")[0])
                if score > highest_score:
                    highest_score = score
                    highest_scorer = parts[0].split(": ")[1]
            return highest_scorer, highest_score
    except FileNotFoundError:
        return None, 0

# Function to display all scores from the file
def display_all_scores():
    try:
        with open("scores.txt", "r") as file:
            scores = file.readlines()
            if scores:
                print("All past scores:")
                for score in scores:
                    print(score.strip())
            else:
                print("No scores recorded yet.")
    except FileNotFoundError:
        print("No scores recorded yet.")

# Function to clear all scores from the file
def clear_scores():
    with open("scores.txt", "w") as file:
        file.write("")
    print("All scores have been deleted.")

def main():
    name = ask_name()  # Ask for the player's name
    show_introduction()  # Show the introduction

    while True:
        question_amount = ask_number_of_questions()  # Ask how many questions the player wants to answer
        mode = ask_game_mode()  # Ask the game mode
        difficulty = ask_difficulty_level()  # Ask the difficulty level
        range_min, range_max = get_range_by_difficulty(difficulty)  # Get the number range based on difficulty

        print(f"OK {name}, ready? Let's go!")
        for i in range(3, 0, -1):
            print(i)
            time.sleep(1)
        print("GO!")

        # Ask the questions based on the selected mode
        if mode == "x":
            correct_answers, question_history = question_multiply(question_amount, range_min, range_max)
        elif mode == "/":
            correct_answers, question_history = question_division(question_amount, range_min, range_max)
        elif mode == "+":
            correct_answers, question_history = question_addition(question_amount, range_min, range_max)
        elif mode == "-":
            correct_answers, question_history = question_subtraction(question_amount, range_min, range_max)

        # Showing their score
        score_percentage = (correct_answers / question_amount) * 100
        score_message = f"Your score: {correct_answers}/{question_amount} ({score_percentage:.2f}%)"
        print(score_message)
        save_score(name, correct_answers, question_amount, mode, difficulty)

        # Display question history
        while True:
            history_answer = input("Would you like your history? (Y/N): ").strip()
            if history_answer in Y:
                print("Here is a history of your questions:")
                for question, answer, result, correct_answer in question_history:
                    print(f"Question: {question}, Your Answer: {answer}, Result: {result}, Correct Answer: {correct_answer}")
                break
            elif history_answer in N:
                break
            else:
                print("Please input a valid answer")

        # Ask if the player wants to play again
        if not ask_to_play_game():
            break

    # Display all past scores
    display_all_scores()
    highest_scorer, highest_score = get_highest_score()  # Get the highest score
    if highest_scorer:
        print(f"The highest score so far is {highest_score}, achieved by {highest_scorer}.")
    else:
        print("No scores recorded yet.")

    # Ask if the player wants to delete all scores
    while True:
        delete_scores = input('Would you like to delete all scores? (Y/N): ').strip()
        if delete_scores in Y:
            clear_scores()
            break
        elif delete_scores in N:
            print("Scores are not deleted.")
            break
        else:
            print("Invalid input. Please enter Y or N.")

if __name__ == "__main__":
    main()
