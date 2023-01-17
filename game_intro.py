# First We need to Automate CRUD on Questions and answer
# As of now HardCoded
# Need to Categorize Questions Difficulty into 3 (easy, medium, hard)
# Question Have 15 Levels

# Development Steps:
# 1: Question and Answer Logic
# 2: LifeLine Logic (Special Features)
# 3: Price Settings

from time import sleep
from sys import stdout

import pyfiglet as pfg
import os

intro_prints = [
"Do you want to read Game Description? y for Yes or n for Skip Description : ",
'''
Rules:
* In this game, you need to answer the questions accurately for the love of your dreams
* You have only one attempt per questions to answer correctly
* You can get your accumulated money in an instant whenever you want just press 'g'
* You will get prizes amount depends upon the level you've answer correctly

''',
'''Level  1: P1,000
Level  2: P2,000 
Level  3: P3,000
Level  4: P5,000
Level  5: P10,000   # Secure Amount of the Easy Question
Level  6: P20,000
Level  7: P30,000
Level  8: P40,000
Level  9: P50,000
Level 10: P100,000  # Secure Amount of the Medium Question
Level 11: P200,000
Level 12: P300,000
Level 13: P500,000
Level 14: P1,000,000

Level 15: GRAND PRIZE: 'BRAND NEW LOVING GIRLFRIEND ;D'

* If you missed to guess the answer in:
LVL 1 - 4 ==========> prize ===> 0 PHP
LVL 5 - 9 ==========> prize ===> 10,000 PHP
LVL 10 - 14 ==========> prize ===> 100,000 PHP

* You will have 3 lifeline which can be only access once in the whole game
3 Lifeline Available:
1. 50:50: Remove two incorrect choices
2. Switch Question: Replace the Question based from Difficulty and Unquestioned
3. Double Dip: Allows the player to answer the question once again\n''',
'''
Are you ready? y for Yes and n for No : 
''',
'''
The Game is about to start!
'''
]

def clear_screen():
    # Clear screen to avoid distraction
    os.system('cls||clear')
    # Use the FigletFont class to create a Beautiful Header
    print(pfg.figlet_format('Who Wants to be Love',
                            font="slant",
                            justify="left",
                            width=150
                            ))

# Delay printing
def delay_print(s):
    # print one character at a time
    for c in s:
        stdout.write(c)
        stdout.flush()
        sleep(0.05)

def print_game_intro():
    # Clear the terminal
    clear_screen()
    sleep(2)
    # Buffer to view description
    
    while True:
        # Prompts if the player needs to see the description
        print(intro_prints[0], end="")
        res = input()
        if res == "y":
            delay_print(intro_prints[1])
            sleep(2)

            delay_print(intro_prints[2])

            sleep(2)
            # Prompts if player is ready
            delay_print(intro_prints[3])
            print("\n")
            while True:
                res = input()
                if res == "y":
                    break
                else:
                    pass
            break

        if res == "n":
            # Prints that the game is about to start
            print(intro_prints[4])
            sleep(2)
            break