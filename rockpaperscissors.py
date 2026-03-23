import random
import time

win_conditions = {'rock': 'scissors',
                      'paper': 'rock',
                      'scissors': 'paper'}

def main_game():

    computer_choice = random.choice(['rock','paper','scissors'])
    while True:
        user_choice = input("Pick your choice: rock, paper, or scissors: ").strip().lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            print('Computer is making a decision....')
            time.sleep(3)
            comparisons(computer_choice, user_choice)
            break
        else:
            print("You can only choose rock, paper, or scissors! Please try again.")
            print('-'*20)

def comparisons(computer_choice, user_choice):

    print(f"The computer chose {computer_choice}!")

    if user_choice == computer_choice:
        print(f"It's a tie! You both chose {user_choice}.")

    elif win_conditions[user_choice] == computer_choice:
        print(f"You win! {user_choice} beats {computer_choice}!")

    else:
        print(f"You lost! The computer chose {computer_choice}, which beats {user_choice}")

    play_again()

def play_again():
    retry = input("Try again? (yes/no): ").strip().lower()
    if retry == 'yes':
        main_game()
    else:
        print("Thanks for playing! Goodbye!")

main_game()
