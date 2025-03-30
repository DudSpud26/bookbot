def get_word_count(string):
    num_words = 0
    list_of_words = string.split()

    for word in list_of_words:
        num_words += 1
    
    return num_words