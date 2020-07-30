def maxvalue(btree):
    if type(btree) != list:
        largestvalue=btree
        return largestvalue
    else:
        largestvalue=btree[0]
    if btree == [[],[],[]]:
        return '-inf'
    if (btree[1]==[]) and (btree[2]==[]):
        return btree[0]
    else:
        if btree[2]!=[]:
            right = maxvalue(btree[0])
        if btree[1]!=[]:
            left = maxvalue(btree[1])
        largestvalue = max(left, right, largestvalue)
    return largestvalue
        
def minvalue(btree):
    if type(btree) != list:
        smallestvalue=btree
        return smallestvalue
    else:
        smallestvalue=btree[0]
    if btree == [[],[],[]]:
        return '-inf'
    if (btree[1]==[]) and (btree[2]==[]):
        return btree[0]
    else:
        if btree[2]!=[]:
            right = minvalue(btree[0])
        if btree[1]!=[]:
            left = minvalue(btree[1])
        smallestvalue = min(left, right, smallestvalue)
    return smallestvalue

tree = [8, [3, [1,[],[]],[6,[4,[],[]],[7,[],[]]]], [10,[],[14,[13,[],[]],[]]]]

print(maxvalue(tree))
print(minvalue(tree))