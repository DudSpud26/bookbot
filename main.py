def get_book_text(filepath):
    book_as_string = ""
    with open(filepath) as f:
        book_as_string = f.read()

    return book_as_string

from stats import get_word_count 

    
def main():
    frankenstein_word_count = get_word_count(get_book_text("books/frankenstein.txt"))
    print(f"{frankenstein_word_count} words found in the document")

main()