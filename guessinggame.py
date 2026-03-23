import random

def guessing_game(guess):
    answer = random.randint(1, 100) #random number from 1 to 100

    while guess != answer: #the loop will play until user guesses correctly

        try:
            guess = int(input("Enter a number between 1 and 100 (inclusive): "))
        except ValueError: #edegcases for letters
            print("INVALID INPUT! Please enter numbers only.")
            print("-"*20)
            print()
            continue #skips the if statements below and restarts the loop
        if len(str(guess)) == 0: #edgecase for empty inputs
            print("YOU DIDN'T ENTER ANYTHING!")
            print("-"*20)
            print()
        elif guess > 100 or guess < 1: #if the guess is out of bounds
            print("OUT OF BOUNDS! Please try again.")
            print("-"*20)
            print()
        elif guess < answer: #if guess is too low
            print("TOO LOW!")
            print("-"*20)
            print()
        elif guess > answer: #if guess is too high
            print("TOO HIGH!")
            print("-"*20)
            print()
    print()
    print(f"CONGRATS! YOU GUESSED IT! THE ANSWER WAS **{answer}**") #if the user wins
    print("-"*20)
    redo = input("Would you like to play again? (y/n): ").strip().lower() #retry
    if redo == 'y':
        print()
        return guessing_game("") #restarts the loop
    else:
        return "Thanks for playing!" #ends program

result = guessing_game("")
print(result)
