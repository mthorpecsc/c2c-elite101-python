import string
no_punct = str.maketrans('','', string.punctuation)

def unique_word_counter():
    print("Welcome to Unique Word Counter. Type in a sentence to see how many unique words it has!")
    sentence = input(": ").lower().translate(no_punct).split() #lowers, removes punctuation, and splits into a list

    display_words = [] #a list created to show the user the unique words and all words
    display_unique_words = []
    word_count = 0 #a counter for total words
    unique_words = 0 #a counter for unique words
    print("-"*15)

    for char in sentence: #for each word in sentence, its appended to display_words
        if char.isdigit() == True: #if the character is a digit, loop skips it
            continue
        else:
            display_words.append(char)
            word_count += 1 #add 1 to count
    fdw = ', '.join(display_words) #fdw stands for format display words
    print(f"*Total Words*: {fdw}")
    print(f"Amount: {word_count}") #number of words

    print("-"*15)

    for char in set(sentence):
        if char.isdigit() == True:
            continue
        else:
            display_unique_words.append(char)
            unique_words +=1
    fduw = ', '.join(display_unique_words) #fduw stands for format display unique words
    print(f"*Unique Words*: {fduw}" )
    print(f"Amount: {unique_words}") #number of unique words


unique_word_counter()
