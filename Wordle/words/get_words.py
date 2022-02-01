words = open('unigram_freq.csv').readlines()
four_letter_words = []
five_letter_words = []
six_letter_words = []
for line in words[0:150000]: # after this point most words aren't valid anymore
    word = line.split(',')[0]
    if len(word) == 4:
        four_letter_words.append(word)
    elif len(word) == 5:
        five_letter_words.append(word)
    elif len(word) == 6:
        six_letter_words.append(word)

with open('four_letter_words.txt', 'w') as f:
    for item in four_letter_words:
        f.write("%s\n" % item)

with open('five_letter_words.txt', 'w') as f:
    for item in five_letter_words:
        f.write("%s\n" % item)

with open('six_letter_words.txt', 'w') as f:
    for item in six_letter_words:
        f.write("%s\n" % item)