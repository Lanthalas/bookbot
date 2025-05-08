def word_count(text):
    text_split = text.split()
    return len(text_split)


def sort_on(dict):
    return dict["num"]

def sort_dictionary(dictionary):
    sorted_dict_list = []

    for letter in dictionary:
        aux_dic = {}
        aux_dic["char"] = letter
        aux_dic["num"] = dictionary[letter]
        sorted_dict_list.append(aux_dic)
    
    sorted_dict_list.sort(reverse=True, key=sort_on)
    return sorted_dict_list

def character_count(text):
    text_split = text.lower().split()
    letter_dictionary = {}
    for word in text_split:
        for letter in word:
            if letter not in letter_dictionary:
                letter_dictionary[letter] = 1
            else: 
                aux = letter_dictionary[letter]
                aux += 1
                letter_dictionary[letter] = aux
    return letter_dictionary