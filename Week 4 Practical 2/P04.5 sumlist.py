def sum_lists(list_2d):
    output =[]
    total = 0
    for row in list_2d:
        for val in row:
            total += val
        output.append(total)
        total=0
    print(output)

sum_lists([[1,2,3], [2], [1, 2, 3, 4]])