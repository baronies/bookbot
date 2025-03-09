from stats import word_count
from stats import character_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    count = word_count(text)
    characters = character_count(text)
    print(f"{count} words found in the document")
    print(f"{characters}")

main()
