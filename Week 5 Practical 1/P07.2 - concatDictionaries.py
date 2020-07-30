#***Concat Dictionaries***

def concat_dico(dico1, dico2):
    for key in dico2:
        dico1[key] = dico2[key]     
    return dico1

print(concat_dico({"one":1, "two":2, "three":3}, {"four":4, "five":5}))

def concatDico(dico1, dico2):
    for key in dico2:
        if dico1[key]:
            dico1[key] = [dico1[key], dico2[key]]
        else:
            dico1[key] = dico2[key]
    return dico1

print(concatDico({"one":1, "two":2, "five":5}, {"two": "10", "five":"101"}))