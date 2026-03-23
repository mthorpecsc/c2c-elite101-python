import random
import time

def bulls_cows():
    computer_choice = random.sample(range(0,9), 4)
    attempts = 0
    max = 4
    while attempts <= max:
            user_guess = input("Enter a 4 digit number with no repeating digits: ").strip()
            if user_guess.isdigit() == True and len(set(user_guess))== 4: #checks if all numbers are unique using len(set())
                user_list = [int(num) for num in str(user_guess)] #converting it into a list of integers

                for digit in user_list:
                    if int(digit) in computer_choice:
                        if user_list.index(digit) == computer_choice.index(digit): #if the digits have the same index its a bull
                            print(f"{digit} is a Bull!")
                        else: #if the digits have difference indexes its a cow
                            print(f"{digit} is a Cow!")

                    elif int(digit) not in computer_choice: #if the digit is not in the computer chouice its not in the number
                        print(f"{digit} is not in the number.")

                attempts += 1 #add a count to the attempt
                print("-"*15)
                print(f"Attempts left: {(max + 1) - attempts}")

            else:
                print("Invalid input. Please enter a non-repeating 4 digit number.")
                print()

            if user_list == computer_choice: #if the user gusses correctly
                print(f"Congratulations! You've guessed the correct number *{''.join(map(str, computer_choice))}* in {attempts} attempt(s)!")
                retry = input("Would you like to play again? (y/n): ").strip().lower()
                if retry == 'y':
                    print("Starting new game...")
                    time.sleep(2)
                    bulls_cows()
                elif retry == 'n':
                    print('Thanks for playing! Goodbye!')
                    break

            if attempts > max: #if the user runs out of attempts
                print(f"You've run out of attempts! The correct number was *{''.join(map(str, computer_choice))}*.")
                retry = input("Would you like to play again? (y/n): ").strip().lower()
                if retry == 'y':
                    print("Starting new game...")
                    time.sleep(2)
                    bulls_cows()
                elif retry == 'n':
                    print('Thanks for playing! Goodbye!')
                    break

bulls_cows()
