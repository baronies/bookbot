from stats import word_count
from stats import character_count
from stats import sort_letters_numbers
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)
    count = word_count(text)
    characters = character_count(text)
    sort = sort_letters_numbers(characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    
    for item in sort:
        if item["letter"].isalpha():
            print(f"{item['letter']}: {item['count']}")

main()
