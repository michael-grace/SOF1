'''Decimal to Binary'''
decimal = int(input('Decimal> '))

remainders = []

while decimal != 0:
    remainders.append(str(decimal % 2))
    decimal = decimal // 2

remainders.reverse()
print(''.join(remainders))
    
    
