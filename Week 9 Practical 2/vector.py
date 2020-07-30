class Vector(object):

    def __init__(self, *args):
        if len(args)==0:
            self._vector = []

        elif type(args[0]) == list:
            self._vector = [float(i) for i in args[0]]

        else:
            points_list = []
            for i in args:
                points_list.append(i)
            self._vector = [float(i) for i in points_list]


    def __str__(self):
        output = '<'

        for i in self._vector:
            output+=(str(i))
            output+=(', ')

        if output[-2:] == ', ':
            output = output[:-2]

        output+=('>')
        return output
              

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
        if (isinstance(other_vector, Vector)) and (len(self._vector) == len(other_vector._vector)):

            for i in range(len(self._vector)):

                if self._vector[i] != other_vector._vector[i]:
                    return False

            return True

        else:
            return False


    def __eq__(self, other_vector):
        return self.equals(other_vector)


    def __ne__(self, other_vector):
        return not self.equals(other_vector)


    def __add__(self, other_vector):
        return self.add(other_vector)


    def __rmul__(self, scalar):
        return self.scalar_product(scalar)


    def __iadd__(self, other_vector):
        return self.add(other_vector)


    def __imul__(self, scalar):
        return self.scalar_product(scalar)


    def __getitem__(self, key):
        return self._vector[key]


    def __setitem__(self, key, value):
        self._vector[key] = value    