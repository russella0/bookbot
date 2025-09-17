from stats import get_book_word_count, get_book_character_count, get_book_sorted_list
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        return(f.read())

def main():
    if len(sys.argv) == 2:
        book_name = sys.argv[1]
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_name}...")
        print("----------- Word Count ----------")
        book_text = get_book_text(book_name)
        book_words = get_book_word_count(book_text)
        print(f"Found {book_words} total words")
        print("--------- Character Count -------")
        book_characters = get_book_character_count(book_text)
        book_list = get_book_sorted_list(book_characters)
        for item in book_list:
            if item['char'].isalpha():
                print(f"{item['char']}: {item['num']}")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
main()
