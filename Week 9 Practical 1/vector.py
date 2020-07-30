class Vector(object):

    def __init__(self, data=None):
        if data==None:
            self._vector = []
        else:
            self._vector = [float(i) for i in data]

    def __str__(self):
        output = '<'
        for i in self._vector:
            output+=(str(i))
            output+=(', ')
        if output[-2:] == ', ':
            output = output[:-2]
        output+=('>')
        return output
        #return '<{0}, {1}, {2}>'.format(self._vector[0], self._vector[1], self._vector[2])
        

    def dim(self):
        return len(self._vector)

    def get(self, index):
        return self._vector[index]

    
    def set(self, index, value):
        self._vector[index] = value

    def scalar_product(self, scalar):
        return Vector([scalar*i for i in self._vector])


    def add(self, other_vector):

        if isinstance(other_vector, Vector):

            if len(self._vector)==len(other_vector._vector):

                _new_vector = []
                for i in range(len(self._vector)):
                    _new_vector.append(self.get(i) + other_vector.get(i))
                
                return Vector(_new_vector)
            else:
                raise ValueError
        else:
            raise TypeError


    def equals(self, other_vector):
        if (len(self._vector) == len(other_vector._vector)) and (isinstance(other_vector, Vector)):
            for i in range(len(self._vector)):
                if self._vector[i] != other_vector._vector[i]:
                    return False
            return True
        else:
            return False