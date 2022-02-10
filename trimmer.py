

f = open('words.txt', 'r')
to_write = open('trimmed_words.txt', 'w')
for word in f:
    if len(word) == 6:
        to_write.write(word)

