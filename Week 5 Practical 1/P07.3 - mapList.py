#***List Mapping to Dictionary***

def map_list(keys, values):
    rtn_dico = {}
    for i in range(len(keys)):
        if keys.count(keys[i])>1:
            print('Error - Keys Must Be Unique')
            return None
        rtn_dico[keys[i]] = values[i]
    return rtn_dico

print(map_list(['un', 'two'], [1,2]))

letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
frequencies = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153, 0.772, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.36, 0.15, 1.974, 0.074]

print(map_list(letters_list, frequencies))