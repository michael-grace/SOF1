'''Sudoku'''

line1 = input('Enter 4 digits> ').split()
line2 = input('Enter 4 digits> ').split()
line3 = input('Enter 4 digits> ').split()
line4 = input('Enter 4 digits> ').split()

for i in range(4):
    if line1[i] == '0':
        line1[i] = ' '

for i in range(4):
    if line2[i] == '0':
        line2[i] = ' '

for i in range(4):
    if line3[i] == '0':
        line3[i] = ' '

for i in range(4):
    if line4[i] == '0':
        line4[i] = ' '

print('+-+-+-+-+\n|{0}|{1}|{2}|{3}|'.format(line1[0], line1[1], line1[2], line1[3]))
print('+-+-+-+-+\n|{0}|{1}|{2}|{3}|'.format(line2[0], line2[1], line2[2], line2[3]))
print('+-+-+-+-+\n|{0}|{1}|{2}|{3}|'.format(line3[0], line3[1], line3[2], line3[3]))
print('+-+-+-+-+\n|{0}|{1}|{2}|{3}|'.format(line4[0], line4[1], line4[2], line4[3]))
print('+-+-+-+-+')
