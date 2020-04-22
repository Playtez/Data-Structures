import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # add to the back of the queue
        if value is not None:
            self.size += 1
            self.storage.add_to_tail(value)
        


    def dequeue(self):
        # remove and return an item from the front of the queue

        if self.storage.length == 0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_from_head()
        
    

    def len(self):
        # returns number of items in the queue
        return self.size
        


