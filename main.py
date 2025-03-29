def get_book_text(filepath):
    book_as_string = ""
    with open(filepath) as f:
        book_as_string = f.read()

    return book_as_string

def main():
    print(get_book_text("books/frankenstein.txt"))

main()