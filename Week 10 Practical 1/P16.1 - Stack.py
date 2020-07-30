class ListNode(object):
    def __init__(self, data = None):
        """Initialising Node

        Arguments
            Data - defaults None, the data for the node
        """

        self._data = data
        self._next = None

    def __str__(self):
        """Returns data from node
        """

        return str(self._data)

class LinkedStack(object):

    def __init__(self):
        """Initialising Stack
        """
        
        self._top = None

    def __str__(self):
        """String Overloader for Stack

        Loops through all the data to add it to the output list, which gets
            put into a string

        Returns
            String of LinkedStack data
        """

        output = []
        currentnode = self._top
        while currentnode is not None:
            if currentnode._data is not None:
                output.append(currentnode._data)
            currentnode = currentnode._next
        return "LinkedStack({})".format(output)

    def peek(self):
        """Viewing top

        Returns the value at the top of the stack, but doesn't remove it

        Returns
            String of the top element, called from __str__ in ListNode
        """

        return str(self._top)

    def push(self, value):
        """Adding to top of stack

        Creates a new node, and will create a memory pointer if neccesary and
            update the top value of the stack
        
        Args
            value - the value to be added
        """

        newnode = ListNode(value)
        if self._top is None:
            self._top = newnode
        else:
            newnode._next = self._top
            self._top = newnode
    
    def __len__(self):
        """Length of the stack

        Keeps adding to count for each node until a node is empty

        Returns
            count - the number of nodes in the stack
        """

        count = 0
        currentnode = self._top
        while currentnode is not None:
            count += 1
            currentnode = currentnode._next
        return count

    def pop(self):
        """Removing from top of stack

        Reassigns the next memory position of the top of the stack to omit
            the first node, jumping straight to the seconds

        Returns
            value - the data in the node that was removed
            
        Raises
            ValueError is stack is too short
        """

        if self.__len__()<2:
            raise ValueError
        else:
            value = str(self._top)
            self._top = self._top._next
            return value
        

stack = LinkedStack()

print("===STACK===")

print("Length=>{}".format(len(stack)))

for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
    stack.push(i)
    print("Top=>{}".format(stack.peek()))
    print("Length=>{}".format(len(stack)))

print(stack)

for i in range(7):
    print("Removed from Top=>{}".format(stack.pop()))

print("Length=>{}".format(len(stack)))
