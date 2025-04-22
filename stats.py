

def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_character(text):
    list_char = {}
    for char in text.lower():
        if char in list_char:
            list_char[char] += 1
        else:
            list_char[char] = 1
    return list_char


def sorted_list_dictionnaries(num_char):
    char_list = []


    for char in num_char:
        #print(char, num_char[char])
        char_list.append({'letter': char, 'count': num_char[char]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def sort_on(dict):
    return dict["count"]