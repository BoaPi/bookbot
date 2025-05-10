import sys

from stats import get_num_words, get_num_characters, sort_character_count, get_num_words, sort_word_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
       return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book = get_book_text(f"./{book_path}")
    num_words = get_num_words(book)
    num_characters = get_num_characters(book)
    char_count = sort_character_count(num_characters) 
    word_count = sort_word_count(get_num_words(book))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for c in char_count:
        if c["char"].isalpha():
            print(f"{c['char']}: {c['count']}")
    for w in word_count:
        print(f"{w['word']}: {w['count']}")
    print("============= END ===============")
main()
