#***Cell Counting***

count = 0

def cell_size(image_arg, x, y, coords=[(-1, -1)]):
    if coords[0]==(-1,-1):
        coords[0]=(x,y)
    #print(image_arg[x][y])
    if image_arg[x][y] == 0:
        return False
    elif image_arg[x][y] == 1:
        
        '''
            1) Test Neigbourhood
            2) Add to tested
        '''
        #coords = [(x,y)]

        #=====> INCREASE A COUNTER HERE <=====
        #=====> ADD TO COORDINATEs LIST <=====
        coords.append((x,y))

        if True: #work out this condition
            new_left = 0
            new_right = len(image_arg)
            new_up = 0
            new_down = len(image_arg[0])

            if x-1 != 0:
                new_left = x-1
            if x+1 != 7:
                new_right = x+1
            if y-1 != 0:
                new_up = y-1
            if y+1 != 7:
                new_down = y+1

            for i in ([(new_left, new_up), (x, new_up), (new_right, new_up), (new_right, y), (new_right, new_down), (x, new_down), (new_left, new_down), (new_left, y)]):
                if i in coords:
                    continue
                print(i, image_arg[i[0]][i[1]])
                #if image_arg[i[0]][i[1]]==1:
                cell_size(image_arg, i[0], i[1], coords)
                    
                    #pass
                    #count += cell_size(image_arg, i[0], i[1])
                    #return count
                #else:
                    #return 1
                #coords.append(i)
            return count

    else:
        print('Error')
        quit()



image = [
    [0,0,0,0,0,0,0,0],
    [1,0,0,0,0,1,0,0],
    [1,1,1,0,1,1,1,0],
    [1,0,1,0,0,1,1,0],
    [1,1,1,0,0,0,0,0],
    [1,1,0,1,1,1,0,0],
    [0,0,0,0,0,1,0,1],
    [0,0,0,0,0,0,1,1]
]

print(cell_size(image, 5, 4))

'''
1) Check Current Coordinate
2) Find all appropriate surrounding coordinates
3) Check those
4) Repeat

COORDINATE
if 0:
    end
else:
    increase counter
    add coordinate to the list of already checked

    find the 8 surrounding coordinates
    1) must be in the grid
    2) shouldn't be checked before

    for each of the 8/whatevers left:
        rerun the function

output the count


'''