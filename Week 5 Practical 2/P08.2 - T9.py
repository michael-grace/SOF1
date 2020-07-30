#***T9 Thing***

def extract_textonyms(vocabulary, keypad):
    user_dict = {}
    for word in vocabulary:
        output = ""
        for char in word:
            for key in keypad.keys():
                if char in keypad[key]:
                    ouput += key
                    break
        if output in user_dict.keys():
            updated = False
            for word_by_t9 in user_dict[output]:
                if word_by_t9[0] == word:
                    word_by_t9[1] += 1
                    updated = True
                    break
            if not updated:
                user_dict[output].append([word, 1])
      
        else:
            user_dict[output] = [word, 1]
    return user_dict

def get_words(digits, user_dict):

    def rtn_freq(elem):
        return elem[1]

    words_list_unordered = user_dict[digits]
    words_ordered = words_list_unordered.sort(key=rtn_freq)
    list_to_return = []
    for i in words_ordered:
        list_to_return.append(i[0])
    return list_to_return


def add_words(text, user_dict, keypad):
    #Same as Above, just minus 1st line
    for word in text:
        output = ""
        for char in word:
            for key in keypad.keys():
                if char in keypad[key]:
                    ouput += key
                    break
        if output in user_dict.keys():
            updated = False
            for word_by_t9 in user_dict[output]:
                if word_by_t9[0] == word:
                    word_by_t9[1] += 1
                    updated = True
                    break
            if not updated:
                user_dict[output].append([word, 1])
      
        else:
            user_dict[output] = [word, 1]
    return user_dict
