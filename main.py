def get_book_text(filepath):
    book_as_string = ""
    with open(filepath) as f:
        book_as_string = f.read()

    return book_as_string

from stats import get_word_count 

from stats import get_character_count

from stats import get_sorted_list

def print_character_counts(dict_list):
    for entry in dict_list:
        if entry["name"].isalpha():
            print(f"{entry["name"]}: {entry["num"]}")


def main():
    file_path = "books/frankenstein.txt"
    book_as_string = get_book_text(file_path)
    total_word_count = get_word_count(book_as_string)
    print("============ BOOKBOT ============")
    print(f"Analyzing book fount at {file_path}...")
    print("----------- Word Count -----------")
    print(f"Found {total_word_count} total words")
    print("--------- Character Count ---------")
    print_character_counts(get_sorted_list(get_character_count(book_as_string)))
    print("============ END ============")
  
main()