#Scalar Product Matrices




def new_matrix():
    matrix = []
    to_add = True

    while to_add:
        user = input('\nType the next line of the matrix, seperated by | characters>')
        try:
            test1 = []
            test2 = []
            test1 = user.split('|')
            test2 = user.split(' | ')
        finally:
            if len(test1) > len(test2):
                matrix.append(test1)
            elif len(test2) > len(test1):
                matrix.append(test2)
            elif (len(test2) == len(test1)) and (len(test1)==1):
                matrix.append(test1)
            else:
                print('Error. Somethings happened. Probably you haven\'t actually eneterd a proper matrix line. Please do.')
                quit()
        
        compare_length = len(matrix[0])
        for i in matrix:
            if len(i) != compare_length:
                print('Error. Please make your matrix entries the same size.')
                quit()
        
        new_line = input('\nWould you like to enter a new line? Y or N>')
        if (new_line=='Y') or (new_line=='y'):
            to_add = True
        elif (new_line=='N') or (new_line=='n'):
            to_add = False
        else:
            print('Error. Please enter an appropriate answer.')
            quit()()
        
    return matrix


matrixa = new_matrix()

try:
    scaler = int(input('Please enter a Scalar Integer Multiple:'))
except ValueError:
    print('Error. Please enter a Scalar Integer Multiple')
    quit()
else:
    print('\nScalar Multiplication:\n')
    for row in matrixa:
        output = ""
        for value in row:
            output += str(int(value)*scaler)
            output += "    "
        print(output)

matrixb = new_matrix()

if (len(matrixa) != len(matrixb)) or (len(matrixa[0]) != len(matrixb[0])):
    print('Error. Your matrices must be the same size.')
else:
    print('\nSum:\n')
    for row in range(len(matrixa)):
        output = ""
        for value in range(len(matrixa[0])):
            output += str(int(matrixa[row][value])+int(matrixb[row][value]))
            output += "    "
        print(output)

transpose = []

for i in range(len(matrixa[0])):
    transpose.append([])

for row in range(len(matrixa)):
    for value in range(len(matrixa[0])):
        transpose[value].append(matrixa[row][value])

print("\nTranspose:\n")
for row in transpose:
    output = ""
    for value in row:
        output += value
        output += "    "
    
    print(output)

