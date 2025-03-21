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
    # split book string in to words and then split words to letters
    letter_count = {}

    for i in letters:
        i = i.lower()
        dict_check = i in letter_count
        # is letter in dict?
        if dict_check == False:
            letter_count.setdefault(i, 1)
            #create key:value if no letter in dict, set to 1
        else:
            letter_count[i] += 1
            # increase value by 1 of given key
    return letter_count

def sort_dict(dict):
    def sort_on(dict):
        return dict["num"]
    letter_list = []
    for d in dict:
        tf = d.isalpha()
        if tf == False:
            None
        else:
            letter_list.append({"name":d,"num":dict[d]})
    letter_list.sort(reverse=True,key=sort_on)
    return letter_list
