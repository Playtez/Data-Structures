import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a  storage dictthat provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        # current number of nodes it holds
        self.capacity = limit
        self.size = 0
        # a doubly-linked list that holds the key-value entries in the correct
        # order
        self.linked_list = DoublyLinkedList()
        # a  storage dictthat provides fast access
        # to every node stored in the cache
        self.storage_cache = {}
        

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        #     Retrieves the value associated with the given key. Also
        if key in self.storage_cache:
            # fetch the DLL node which is the value of this key
            node = self.storage_cache[key]
            self.linked_list.move_to_front(node)
            return node.value[1]
        else:
            return None
            # self.linked_list.move_to_front(self.storage_cache[key])
        
            

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        #if the key is in the cache
        if key in self.storage_cache:
            node = self.storage_cache[key]
            #overwrite the value
            node.value = (key,value)
            # move this node to the front
            self.linked_list.move_to_front(node)
            return
        if self.size == self.capacity:
            # first del the LRU
            oldest_key = self.linked_list.remove_from_tail()
            del self.storage_cache[oldest_key[0]]
            # remove the tail node
            self.size -= 1
        # key is not in storage and we still have room in our cache
        # add the key and value
        self.linked_list.add_to_head((key,value))
        self.storage_cache[key] = self.linked_list.head
        self.size += 1



        # ## if the cache is already at max limit
        # if self.size >= self.capacity:
        # ## then the oldest entry aka the tail needs to be removed
        #     self.size -= 1
        #     self.linked_list.remove_from_tail()
        #     self.linked_list.move_to_front(self.storage_cache[key])
        # ## if the key already exists
        # if key in self.storage_cache:
        #     node = self.storage_cache[key] 
        #     node.value = (key,value)
        #     return 
        # ## then overwrite the old value associated with the key 
        
        
        # self.size += 1
        # self.storage_cache[key] = self.linked_list.add_to_head((key,value))
    
       



