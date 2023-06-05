# [Rock - Paper - Scissors] game with ASCII art & randomization in Python.

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

print("Welcome to Rock-Paper-Scissors game!")
user_choice = int(input("What do you choose ? : Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number! Try again..")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose :")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You have won the game!")

    elif computer_choice == 0 and user_choice == 2:
        print("You lose!")

    elif computer_choice > user_choice:
        print("You lose!")

    elif user_choice > computer_choice:
        print("You have won the game!")

    elif computer_choice == user_choice:
        print("It was a draw!")
