'''Number Series'''

numbers = input('enter numbers> ').split()
list_of_evens = []

for i in numbers:
    if (int(i) % 2 == 0) and (i not in list_of_evens):
        list_of_evens.append(i)

print('There are {0} distinct even numbers: {1}'.format(len(list_of_evens), ' '.join(list_of_evens)))
