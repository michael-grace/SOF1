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

class LinkedQueue(object):

    def __init__(self):
        """Initialising queue
        """
        
        self._front = None

    def __str__(self):
        """String Overloader for Queue

        Loops through all the data to add it to the output list, which gets
            put into a string

        Returns
            String of LinkedQueue data
        """

        output = []
        currentnode = self._front
        while currentnode is not None:
            if currentnode._data is not None:
                output.append(currentnode._data)
            currentnode = currentnode._next
        return "LinkedQueue({})".format(output)

    def peek(self):
        """Viewing front

        Returns the value at the front of the queue, but doesn't remove it

        Returns
            String of the front element, called from __str__ in ListNode
        """

        return str(self._front)

    def enqueue(self, value):
        """Adding to end of queue

        Creates a new node, and will create a memory pointer from the last
            element to the new element
        
        Args
            value - the value to be added
        """

        newnode = ListNode(value)
        
        if self._front is None:
            self._front = newnode
        else:
            currentnode = self._front
            while currentnode._next is not None:
                
                currentnode = currentnode._next
            currentnode._next = newnode
            
    
    def __len__(self):
        """Length of the queue

        Keeps adding to count for each node until a node is empty

        Returns
            count - the number of nodes in the queue
        """

        count = 0
        currentnode = self._front
        while currentnode is not None:
            count += 1
            currentnode = currentnode._next
        return count

    def pop(self):
        """Removing from front of queue

        Reassigns the next memory position of the front of the queue to omit
            the first node, jumping straight to the seconds

        Returns
            value - the data in the node that was removed

        Raises
            ValueError is queue is too short
        """
        if self.__len__()<2:
            raise ValueError
        else:
            value = str(self._front)
            self._front = self._front._next
            return value
    

queue = LinkedQueue()

print("===Queue===")

print("Length=>{}".format(len(queue)))

for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
    queue.enqueue(i)
    print("Length=>{}".format(len(queue)))
    
print("front=>{}".format(queue.peek()))

print(queue)

for i in range(4):
    print("Removed from front=>{}".format(queue.pop()))
    print("front=>{}".format(queue.peek()))

print("Length=>{}".format(len(queue)))
