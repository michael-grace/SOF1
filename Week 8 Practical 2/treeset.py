def isempty(treeset):
    if treeset == []:
        return True
    else:
        return False

def add(element, treeset):
    pass

def maxvalue(treeset):
    if len(treeset) == 0:
        return float('-inf')
    elif len(treeset) == 1:
        return treeset[0]        

    maxval = treeset[0]
    if treeset[2] != []:
        return maxvalue(treeset[2])
    else:
        return maxval

def minvalue(treeset):
    if len(treeset) == 0:
        return float('inf')
    elif len(treeset) == 1:
        return treeset[0]        

    minval = treeset[0]
    if treeset[1] != []:
        return minvalue(treeset[1])
    else:
        return minval


def get_values(treeset):
    pass

def contains(element, treeset):
    if (type(treeset) != list):
        if element == treeset:
            return True
        else:
            return False
    else:
        if element == treeset[0]:
            return True
        
        elif element < treeset[0]:
            if treeset[1] != []:
                return contains(element, treeset[1])
            else:
                return False
        elif element > treeset[0]:
            if treeset[2] != []:
                return contains(element, treeset[2])
            else:
                return False
        else:
            return False

def equals(treeset_a, treeset_b):
    pass

def remove(element, treeset):
    pass

print(contains(6, [8, [3, [-1,[],[]],[6,[4,[],[]],[7,[],[]]]], [10,[],[14,[13,[],[]],[]]]]))