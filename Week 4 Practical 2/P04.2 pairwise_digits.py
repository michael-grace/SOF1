#***Pairwise Digits***

def pairwise_digits(number_a, number_b):
    output = ''
    for i in range(len(str(number_a))):
        if str(number_a)[i]==str(number_b)[i]:
            output += '1'
        else:
            output += '0'
    
    return output

print(pairwise_digits(1213, 2113))
