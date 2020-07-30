'''Voronoi Diagrams'''

characters = ['X', 'O', 'I', '-', '/', '\\', '+', '<', '>', '#', '', 'E']
plane = [
(0,0),
(12,6),
(14,24),
(20,13),
(9,17),
(69,50),
(37,69),
(69,42),
(70,40),
(11,38),
    ]
width = 100
height = 100

'''for ypos in range(height):
    line_text = ''
    
    for xpos in range(width):
        
        closest_seed = 11
        closest_distance = 99999.99999
        iteration = 0
        
        for i in plane:
            if (ypos == i[1]) and (xpos == i[0]):
                closest_seed = 10
                line_text += '*'
                break
            else:
                distance = ((ypos-i[1])**2 + (xpos-i[0])**2)**0.5

                if distance < closest_distance:
                    closest_distance = distance
                    closest_seed = iteration
            iteration += 1
        line_text += characters[closest_seed]
        #line_text += ','#'({0}, {1})'.format(xpos, ypos)
    print(line_text)

'''

#Creates Coordinates System
all_points = []
all_values = []
coords = [] #List to cycle through
for xval in range(width):
    for yval in range(height):
        all_points.append((xval, yval))
        all_values.append(' ')

for i in plane:
    coords.append((i[0], i[1], characters[plane.index(i)]))

print(coords)
print(coords[0])
    #all_values[all_points.index(i)]='*'

#print(all_values)
a=0
while ' ' in all_values:
    #print(a)
    a+=1
    i = coords[0]
    new_left=0
    new_right=99
    new_down=0
    new_up=99
    if all_values[all_points.index((i[0], i[1]))]==' ':
        all_values[all_points.index((i[0], i[1]))] = i[2]

        if i[0]+1 != 100:
            new_right = i[0]+1
        if i[0]-1 != -1:
            new_left = i[0]-1
        if i[1]+1 != 100:
            new_up = i[1]+1
        if i[1]-1 != -1:
            new_down = i[1]-1
    #print(new_left, new_right, new_up, new_down)

    '''
    ***PLAN***

    1) Find all coordinates
    2) Check if already filled
    3) Add to todo list if not 
    
    
    '''



    for j in [(new_left, new_up), (i[0], new_up), (new_right, new_up), (new_right, i[1]), (new_right, new_down), (i[0], new_down), (new_left, new_down), (new_left, i[1])]:
        if all_values[all_points.index(j)] == ' ' and j not in coords:
            coords.append((j[0], j[1], i[2]))



    coords.pop(0)
    #print(coords)
    #print(a)
    
    """if a == 1000 or a <= 20:
        if a == 1000:
            a = 0
        for i in range(0,10000,100):
            
            the_sacred_string = ''
            for j in all_values[i:i+100]:
                the_sacred_string += j
            print('#'+the_sacred_string+'#')#
        '''if len(coords) > 350:
            print(len(coords))'''"""
        #print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')

for i in range(0,10000,100):
        
    the_sacred_string = ''
    for j in all_values[i:i+100]:
        the_sacred_string += j
        the_sacred_string += ','
    print(the_sacred_string)