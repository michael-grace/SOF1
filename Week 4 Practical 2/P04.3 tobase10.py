#***To Base 10***

'''@author Lilian'''

def to_base10(binary):
    total = 0
    for i in range(len(binary)):
        total += int(binary[-i-1])*(2**(i))
    return total

print(to_base10(input()))