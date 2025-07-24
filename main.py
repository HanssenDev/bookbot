from stats import count_words
from stats import get_character_count
from stats import sort_characters
import sys

# read the book file and return its content
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    characters_dict = get_character_count(book_text)
    sorted = sort_characters(characters_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted:
        if item["char"].isalpha() == True:
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
main()