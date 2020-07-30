#***Floyd's Triangle***

rows = int(input('Num Rows>'))

current_num = 1
for i in range(rows):
    to_write=''
    for j in range(i+1):
        if len(str(current_num))==1:
            to_write += '  {}'.format(current_num)
        elif len(str(current_num))==2:
            to_write += ' {}'.format(current_num)
        
        current_num+=1
    print(to_write)