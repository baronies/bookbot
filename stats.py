def word_count(string):
    return len(string.split())

def character_count(string):

    lower_case_words = string.lower()
    characters_dict = {}
    
    for character in lower_case_words:
        if character in characters_dict:
            characters_dict[character] += 1
        else:
            characters_dict[character] = 1

    return characters_dict

def sort_letters_numbers(char_dict):
    result = []

    for letter, count in char_dict.items():
        letter_info = {"letter": letter, "count": count}
        result.append(letter_info)

    def sort_big_to_small(dict):
        return dict["count"]

    result.sort(reverse=True, key=sort_big_to_small)
    
    return result
