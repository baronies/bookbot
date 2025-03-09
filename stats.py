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
