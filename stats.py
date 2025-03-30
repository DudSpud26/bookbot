def get_word_count(string):
    num_words = 0
    list_of_words = string.split()

    for word in list_of_words:
        num_words += 1
    
    return num_words

def get_character_count(string):
    character_dictionary = {}
    for character in string:
        lower_case = character.lower()
        if lower_case in character_dictionary:
            character_dictionary[lower_case] += 1
        else:
            character_dictionary[lower_case] = 1
    
    return character_dictionary

def sort_on(dict):
    return dict["num"]

def get_sorted_list(dict):
    result = []
    for entry in dict:
        item = {"name":entry,"num":dict[entry]}
        result.append(item)
    
    result.sort(reverse=True, key=sort_on)
    return result


