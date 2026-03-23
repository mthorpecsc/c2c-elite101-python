def unique_or_not(user_input):
    print("***UNIQUE INPUT CHECKER***")
    user_input = input("ENTER IN SOME TEXT:").strip() #accounting for whitespace
    if len(user_input) == 0: #if the length is zero, no input was given
        print("YOU DIDN'T ENTER ANYTHING!")
        return False
    elif len(user_input) == len(set(user_input)): #if the lenghths are the same, all characters are unique
        return True
    else: #anything else is not unqiue
        return False

tof = unique_or_not("")
print(tof)
