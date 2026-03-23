import string

sentence = input("Enter a sentence: ")
no_punct = str.maketrans('','', string.punctuation)
clean_sentence = sentence.translate(no_punct)
print(clean_sentence)


"""
def retry():
    while True:
        number = int(input("Enter 1 2 or 3: "))
        if number in [1, 2, 3]:
            print(f"you entered {number}")
            break
        else:
            print("Please try again")

retry()
"""
