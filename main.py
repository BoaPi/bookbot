def get_book_text(path_to_file):
    with open(path_to_file) as f:
       return f.read()

def count_words(text):
    return len(text.split())

def main():
    num_words = count_words(get_book_text("./books/frankenstein.txt"))
    print(f"{num_words} words found in the document")

main()
