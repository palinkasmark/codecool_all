sentence = "Hello world!".upper()
sentence_2 = "again hello".upper()
words = sentence.split()
words_2 = sentence_2.split()

for word_1 in words:
    for word_2 in words_2:
        if word_1 == word_2:
            print(word_1)
        # print(f'Word 1: {word_1}, Word 2: {word_2}')
        """ if word_1 == word_2:
            print(word_1) """
    
