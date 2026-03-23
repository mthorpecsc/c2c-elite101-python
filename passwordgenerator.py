"""
create a function called password_generator
create a list titled nums which holds all numbers
create a list titled lcl (lowercaseletters) holding all lowercase letters
do the same for upercase ^
print a message explaining the program and what it does
use a while true loop for reprompting
ask the user to input a desired length of the password (minimum 4)
if the input is not a digit reprompt the user to try again
if the input is less than 4 reprompt the user to try again
create values for has_lowercase, has_uppercase, has_digits and set them to False
ask the user to input if they want lowercase letters included (y/n)
if they respond with y, change the value to True
ask the user to input if they want uppercase letters included
if they respond with y, change the value to True
ask the user to input if they want digits included
if they respond with y, change the value to True
create a loop that appends characters to a list, and breaks only when the character limit is reached
depending on the characteristics the user wants in their password, the loop will append a random item from the digit, lowercase letter, and uppercase letter list to a list called final_password.
once the character limit is reached, the loop will stop and the final_password will be shuffled
the list will then be printed out the user
running into NameError / moving to the next function after being done with the loops
running into error of not getting the desired length
"""
import random
import time

#the function that does the generating
def generate_password(length, has_upcl, has_lcl, has_nums ,upcl, lcl, nums):
    final_password = [] #list to store the generated password
    characters = 0 #a counter to keep track of characters added
    while characters < length: #the loop will continue to add characters until the length is reached
        if has_upcl == True:
            final_password.append(random.choice(upcl))
            characters += 1
            if len(final_password) == length: #stops and checks to see if the length of the final password is equal to the length
                break
        if has_lcl == True:
            final_password.append(random.choice(lcl))
            characters+= 1
            if len(final_password) == length:
                break
        if has_nums == True:
            final_password.append(random.choice(nums))
            characters += 1
            if len(final_password) == length:
                break
    if has_upcl and has_lcl and has_nums == False:
        print("You wanted nothing in your password, therefore you have no password.")
    print("Generating Password...")
    time.sleep(2)
    print("Thinking of 2763+ unique combinations...")
    time.sleep(2)
    print("Your password is almost ready...")
    time.sleep(2)
    print("-"*20)
    print(f"Your newly generated password: \nLength: {length}\nHas Uppercase: {has_upcl}\nHas Lowercase: {has_lcl}\nHas Digits: {has_nums}")
    random.shuffle(final_password)
    print(''.join(map(str,final_password))) #turns finalpassword into a string


#main function
def password_generator():
    #lists of characters that can be included in the password
    nums = ['0','1','2','3','4','5','6','7','8','9']
    lcl = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upcl = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    print("Welcome to Password Generator! \nThis program will generate you a new password based on your chosen preferences. \nYou can choose to include lowercase letters, uppercase letters, and digits in your password. \nThe minimum length of the password must be 4 characters.")
    print("-"*30)
    while True:
        try: #try and except block to rule out non-integer inputs and reprompt user to try again
            length = int(input("Please enter the desired length of your password. (minimum 4): "))
            if length >=4:
                break #breaks this loop if the integer is valid and goes to the next one
            else:
                print("Your minimum password length must be 4 characters. Please try again.")
        except ValueError:
            print("Please enter a positive integer.")
            print()

    while True:
        has_upcl = input("Would you like to include uppercase letters in your password? (y/n): ") #upcl = uppercase letters
        if has_upcl == 'y':
            has_upcl = True
            break
        elif has_upcl == 'n':
            has_upcl = False
            break
        else:
            print("Please respond with 'y' or 'n'")

    while True:
        has_lcl = input("Would you like to include lowercase letters in your password? (y/n): ") #lcl = lowercase letters
        if has_lcl == 'y':
            has_lcl = True
            break
        elif has_lcl == 'n':
            has_lcl = False
            break
        else:
            print("Please respond with 'y' or 'n'")

    while True:
        has_nums = input("Would you like to include digits in your password? (y/n): ") #nums = numbers
        if has_nums == 'y':
            has_nums = True
            break
        elif has_nums == 'n':
            has_nums = False
            break
        else:
            print("Please respond with 'y' or 'n'")

    generate_password(length, has_upcl, has_lcl, has_nums ,upcl, lcl, nums)

password_generator()

