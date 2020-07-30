num_letters = int(input('Num. of Letters> '))
max_length = 2*num_letters -1

for i in range(num_letters):
    output = ''
    output += ' '*(max_length-(2*i -1))/2
    output += '* '*i
    output += ' '*(max_length-(2*i -1))/2
    print(output)