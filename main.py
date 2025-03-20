from stats import word_count

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

def main():

    print(f"{num_words} words found in the document")

main()
