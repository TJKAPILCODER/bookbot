from stats import get_book_words, get_book_text, num_char, sort_dec
import sys 

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def main():
   # path = "books/frankenstein.txt"
    words_number = get_book_words(book_path)
    book_text = get_book_text(book_path)
    chars_dict =  num_char(book_text)
    sorted_chars = sort_dec(chars_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {words_number} total words")
    print("--------- Character Count -------")
    
    for char_info in sorted_chars:
        char = char_info["char"]
        count = char_info["count"]
        if char.isalpha(): # Only print alphabetical characters
            print(f"{char}: {count}")
    print("============= END ===============")


main()