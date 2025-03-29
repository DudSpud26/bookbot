def get_book_text(filepath):
    book_as_string = ""
    with open(filepath) as f:
        book_as_string = f.read()

    return book_as_string

def get_word_count(string):
    num_words = 0
    list_of_words = string.split()

    for word in list_of_words:
        num_words += 1
    
    return num_words 

    
def main():
    frankenstein_word_count = get_word_count(get_book_text("books/frankenstein.txt"))
    print(f"{frankenstein_word_count} words found in the document")

main()