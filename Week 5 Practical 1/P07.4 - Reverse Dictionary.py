#***Reversing Dictionary***

def reverse_dictionary(dico):
    new_dico = {}
    for key in dico:
        new_dico[dico[key]] = key
    return new_dico

print(reverse_dictionary({"one":1, "two":2}))