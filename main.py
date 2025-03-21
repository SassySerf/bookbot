import sys
from stats import word_count
from stats import letter_count
from stats import sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        fc = ""
        fc = f.read()
        return fc

file_contents = ""
try:
    file_contents = get_book_text(sys.argv[1])
except:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

file_words = []
file_words = file_contents.split()

num_words = 0
num_words = word_count(file_words)

letter_count = letter_count(file_contents)
sorted_count = sort_dict(letter_count)


def main():
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for i in sorted_count:
            print(f"{i['name']}: {i['num']}")
        print("============= END ===============")


main()
