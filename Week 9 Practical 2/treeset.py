from collections import deque

class TreeSet(object):
        
        def __init__(self, root=None):
            self._root = root
            self._left = None
            self._right = None

 
        def __contains__(self, element):
            if self._root == element:
                return True

            elif element < self._root:
                if self._left == None:
                    return False
                else:
                    return self.__contains__(self._left)
                
            elif element > self._root:
                if self._right == None:
                    return False
                else:
                    return self.__contains__(self._right)
                


        def __sub__(self, other_set):
            return self.difference(other_set)


        def __and__(self, other_set):
            return self.intersection(other_set)


        def __or__(self, other_set):
            return self.union(other_set)


        def __xor__(self, other_set):
            return self.symettric_difference(other_set)


        def isempty(self):
            return True if [self._root, self._left, self._right] == [None, None, None] else False


        def add(self, element):
            if self.isempty():
                self._root = element
               
            else:
            
                if element < self._root:
                    if self._left is None:
                        self._left = TreeSet(element)
                    else:
                        self._left.add(element)
                                
                elif element > self._root:
                    if self._right is None:
                        self._right = TreeSet(element)
                    else:
                        self._right.add(element)
            
                else:
                    return


        def remove(self, element):
            pass


        def difference(self, other_set):
            pass


        def intersection(self, other_set):
            pass


        def union(self, other_set):
            pass


        def isdisjoint(self, other_set):
            if self.intersection=={}:
                return True
            else:
                return False


        def issubset(self, other_set):
            pass


        def issuperset(self, other_set):
            pass


        def symettric_difference(self, other_set):
            pass


        def discard(self, element):
            pass


        def clear(self):
            pass


        def pop(self):
            pass

tree = TreeSet()
tree.add(3)
tree.add(1)
tree.add(2)
tree.add(4)
