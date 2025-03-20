def word_count(file_words):
    count = 0
    for word in file_words:
        count +=1
    return count

def letter_count(fc):
    fc.split()
    letters = []
    for word in fc:
        word.split()
        letters.append(word)
    letter_count = {}
    for i in letters:
        i = i.lower()
        dict_check = i in letter_count

        if dict_check == False:
            letter_count.setdefault(i, 1)
        else:
            letter_count[i] += 1
    return letter_count
