from stats import word_count
from stats import letter_count
from stats import sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        fc = ""
        fc = f.read()
        return fc

file_contents = ""
file_contents = get_book_text("./books/frankenstein.txt")

file_words = []
file_words = file_contents.split()

num_words = 0
num_words = word_count(file_words)

letter_count = letter_count(file_contents)
sorted_count = sort_dict(letter_count)


def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted_count:
        print(f"{i['name']}: {i['num']}")
    print("============= END ===============")

main()
