def word_freq(sentence):
    show_word_freq = {}
    split_sentence = sentence.lower().split()

    for word in split_sentence:
        if word not in show_word_freq:
            count = 0
            show_word_freq[word] = count+1
        elif word in show_word_freq:
            show_word_freq[word] = show_word_freq.get(word, count) +1

    return show_word_freq

sentence1 = word_freq("the cat and the dog")
print(sentence1)
sentence2 = word_freq("hello")
print(sentence2)
sentence3 = word_freq("a a a b b")
print(sentence3)
