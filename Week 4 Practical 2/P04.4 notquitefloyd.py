#***Right Angle Triangle

rows = int(input('Num Rows> '))

for i in range(rows):
    if (i+1) %2 == 0:
        final = ''
    else:
        final = '1'


    print('10' * ((i+1)//2)+final)
