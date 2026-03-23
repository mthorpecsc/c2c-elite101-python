import string
no_punt = str.maketrans('', '', string.punctuation )  #library to do all the punctuation removing for me B)

def main():

    while True:
        str1 = input("Type in your first word: ").lower().strip().translate(no_punt)
        str2 = input("Type in your second word: ").lower().strip().translate(no_punt)
        if str1.isalpha() or str2.isalpha() == True:
            anagram(str1, str2)
            break
        else:
            print("Please input words without numericals.")
            print()



def anagram(str1, str2):

    if len(str1) != len(str2): #makes sure the lengths are the same to cut out potential rulers
        print('These words have different lengths and therefore cannot be anagrams.')

    first_word = [] #storing the letters in the first word
    second_word = [] #storing the letters in the second word

    for x in str1:
        first_word.append(x) #adds each letter to first_word

    for x in str2:
            second_word.append(x) #adds each letter to second_word

    if sorted(first_word) == sorted(second_word): #sorts each list in alphabetical order
        print(f'{str1} and {str2} are anagrams!')
    else:
        print(f"{str1} and {str2} aren't anagrams!")

main()
