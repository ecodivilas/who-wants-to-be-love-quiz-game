# Quiz Game

# Import modules
from random import choice, shuffle, randint
from time import sleep

import game_intro as dp
import test_questions as qa
import prize as pz

# Global Variables
level = 1 # Make this actual 1
accumulated_prize = 0
game_over = 0

correct_answer = ""
correct_answer_index = None
current_question = []
current_question_index = None
answer_choices = []
current_question_category = []

# Lifeline
life_line_50_50 = 1                     # 50:50: Remove two incorrect choices
life_line_switch_the_question = 1       # Switch the Question: Replace the Question based from Difficulty and Unquestioned
life_line_double_dip = 1                # Double Dip: Allows the player to answer the question once again
is_life_line_triggered = False

def display_level():
    # Display Level and Accumulated Prize
    global accumulated_prize
    global level

    line = "=" * 108
    print(line)
    line2 = f"Level: {level}"
    print(line2, end="")
    print(f"Accumulated Prize: {accumulated_prize:,} PHP".rjust(len(line)-len(line2)))
    print(line)

def display_question():
    global is_life_line_triggered
    # Prints out the current questions
    if is_life_line_triggered:
        print(f"{current_question[0]}")
    else:
        dp.delay_print(f"{current_question[0]}")
    print()

def answer_prompt():
    global life_line_50_50
    global life_line_switch_the_question
    global life_line_double_dip
    global level
    
    # Answer prompt
    print("\n(Just enter a, b, c or d) [LIFELINE: ", end="")
    if life_line_50_50 == 1:
        print("q = '50:50' ", end="")
    if life_line_switch_the_question == 1:
        print("w = 'Switch Question' ", end="")
    if life_line_double_dip == 1:
        print("e = 'Double Dip'", end="")
    print("]")
    print("g = 'quit and collect prize'")
    if level == 15:
        print(f"Enter your answer for {accumulated_prize:,} PHP and Brand New Loving Girlfriend : ", end="")
    else:
        print(f"Enter your answer for {pz.prize_per_level[level-1]:,} PHP : ", end="")
    
# Function to show current question
def get_question(question_category):
    global correct_answer
    global current_question_index
    global current_question
    global answer_choices
    global correct_answer_index
    global current_question_category

    # Set question category
    current_question_category = question_category

    # Randomly select choices from categorized questions
    # print(question_category)
    current_question = choice(question_category)

    # Get index of the question
    current_question_index = question_category.index(current_question)

    # Clear the terminal to avoid distraction
    dp.clear_screen()

    # Display the current level
    display_level()

    # Prints out the current questions
    display_question()                     

    # We shuffle the choices to prevent choices familiarity
    shuffle(current_question[2])
    # Re-assign the nested list to make it readable and shuffle() returns None                          
    answer_choices = current_question[2]                  

    # Extract choices then spot the CORRECT ANSWER
    letter = 97  # a in ascii
    print()
    for index in range(len(answer_choices)):                         
        print(f"{chr(letter)}. {answer_choices[index]}")
        if current_question[1] == answer_choices[index]:
            correct_answer = chr(letter)
            correct_answer_index = index

        letter += 1
    
    # Evaluate Answer based on the condition
    evaluate_answer()

    # Temporary deleted the CURRENT QUESTION to avoid repetition of questions
    del question_category[current_question_index]

    sleep(1) # Extra Delay

# Function to evaluate the answer if it's correct
def evaluate_answer():
    global level
    global game_over
    global life_line_double_dip
    global safe_attempt
    global accumulated_prize
    safe_attempt = 0

    while True:
        # Ask for Player Answer
        answer_prompt()
        answer = input().strip()
        if answer in 'abcdqweg' and len(answer) == 1:
            # Nested if-else for ANSWER VALIDATION
            # Double Dip
            if ord(answer) == 101:
                safe_attempt = 2
                #  print(safe_attempt)
                # Convert into ascii to see to it if it is letter between a - d
            if ord(answer) >= 97 and ord(answer) <= 100:      
                if answer == correct_answer:
                    print()
                    dp.delay_print("Your answer is, Correct!")
                    print("\n")
                    if level == 15:
                        pass
                    else:
                        accumulated_prize = pz.prize_per_level[0+level-1]
                    level += 1
                    break
                else:
                    if safe_attempt > 0:
                        print()
                        dp.delay_print("Wrong guess! You have another chance. ")
                        safe_attempt -= 1
                        life_line_double_dip = 0
                        continue
                    elif answer == "e":
                        dp.delay_print("first answer")
                    else:
                        print()
                        dp.delay_print("Wrong guess! Game Over")
                        if level >= 10:
                            accumulated_prize = pz.prize_per_level[9]
                        if level >= 5:
                            accumulated_prize = pz.prize_per_level[4]
                        else:
                            accumulated_prize = 0
                        print("\n")
                        dp.delay_print(f"You only won an amount of: {accumulated_prize:,} PHP")
                        print("\n")
                        game_over = 1
                        break
            
            # Lifeline Options
            # 50:50
            if answer == "q":
                fifty_fifty()
                continue
            
            # Switch the Question
            if answer == "w":
                switch_question()
                break
                # continue
            if answer == "g":
                end_game()
                break
            else:
                if safe_attempt > 0:
                    print()
                    dp.delay_print(f"Double Dip: You have {safe_attempt} attempts to answer. ")
                    safe_attempt -= 1
                    life_line_double_dip = 0
                    continue
                else:
                    dp.delay_print("Invalid Answer! ")
        else:
            dp.delay_print("Invalid Answer! ")

def end_game():
    global accumulated_prize
    global game_over
    print("\n")
    dp.delay_print(f"You have only won an amount of: {accumulated_prize:,} PHP")
    game_over = 1

# Lifeline functions
def fifty_fifty():
    global answer_choices
    global correct_answer
    global correct_answer_index
    global current_question
    global life_line_50_50
    global is_life_line_triggered

    is_life_line_triggered = True
    
    # Print the header
    dp.clear_screen()
    display_level()
    display_question()

    letter = 97  # a in ascii
    # Random select index for extra confusion w/ the correct answer
    while True:
        extra_index = randint(0,3)
        if extra_index == correct_answer_index:
            extra_index = randint(0,3)
            continue
        else:
            break
    
    # Display the choices
    for index in range(len(answer_choices)):
        if index == correct_answer_index:                        
            print(f"{chr(letter)}. {answer_choices[index]}")
        elif index == extra_index:
            print(f"{chr(letter)}. {answer_choices[index]}")
        else:
            print(f"{chr(letter)}. {''}")
        letter += 1
    life_line_50_50 = 0
    is_life_line_triggered = False

def switch_question():
    global life_line_switch_the_question
    life_line_switch_the_question = 0

# Main Program
dp.print_game_intro()
while True:
    if game_over == 1:
        break
    elif level > 15:
        print()
        dp.delay_print("You Win the jackpot Prize!")
        print("\n")
        dp.delay_print("You can take home your Brand New Loving Girlfriend ;)")
        print("\n")
        break
    else:
        if level > 10:
            # Pick a random current_question from medium
            get_question(qa.hard_questions)
        elif level > 5:
            # Pick a random current_question from medium
            get_question(qa.medium_questions)
        else:
            # Pick a random current_question from easy
            get_question(qa.easy_questions)