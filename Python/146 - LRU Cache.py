"""
Topics: | Design |
"""

class LRUCache:
    """An LRU cache, implemented with a doubly linked list and hashmap. """

    class CacheNode:
        """Inner class for doubly linked list nodes."""
        
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None
            self.prev = None
            
        def __str__(self):
            return str(self.key) + ", " + str(self.value)
    
        
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.MRU = None
        self.LRU = None
        self.nodes = dict()
        
        
    def get(self, key):
        """
        Time: O(1)
        
        Returns the key's value, or -1 if not found.
        Moves the key/value pair to the MRU position in the cache.
        """
        # print("get:", key)
        if key not in self.nodes.keys():
            return -1
        
        node = self.nodes[key]
        self.move_to_MRU(node)
        # self.print_LRUCache()
        return node.value
    

    def put(self, key, value):
        """
        Time: O(1)
        
        Sets or inserts the value for the given key into the cache.
        Moves the key/value pair to the MRU position in the cache.
        """
        # print("put:", key, value)
        # If node is present in cache, update value and move to MRU
        if key in self.nodes.keys():
            node = self.nodes[key]
            node.value = value
            self.move_to_MRU(node)
            # self.print_LRUCache()
            return
        
        # If node is not present, insert new node as MRU and possibly evict LRU
        node = self.CacheNode(key, value)
        self.nodes[key] = node
        self.move_to_MRU(node)
        self.size += 1
        if self.size > self.capacity:
            self.evict_LRU()
        # self.print_LRUCache()
        
        
    def move_to_MRU(self, node):
        """
        Moves the given node to the MRU position in the cache.
        """
        if self.MRU is None:
            self.MRU = node
            self.LRU = node
            return

        if self.MRU is node:
            return
        
        # Update LRU, if moving LRU to MRU
        if self.LRU is node:
            self.LRU = self.LRU.prev
            self.LRU.next = None
            node.next = self.MRU
            self.MRU.prev = node
            self.MRU = node
            node.prev = None
            return
            
        if node.next:
            node.next.prev = node.prev
            node.prev.next = node.next
        node.next = self.MRU
        self.MRU.prev = node
        self.MRU = node
        node.prev = None

        
    def evict_LRU(self):
        """
        Removes the LRU key/value pair from the cache.
        """
        self.nodes.pop(self.LRU.key)
        self.LRU = self.LRU.prev
        self.LRU.next = None
        self.size -= 1
        
        
#     def print_LRUCache(self):
#         print("MRU:\t", self.MRU)
#         print("LRU:\t\t", self.LRU)
#         print("size:\t\t", self.size)
#         print("nodes:\t", end='')
#         self.print_nodes()
        
#         print("forwards:\t\t", end='')
#         curr = self.MRU
#         while curr:
#             print("[", curr, "]", end=' => ')
#             curr = curr.next
#         print("")
        
#         print("backwards:\t", end='')
#         curr = self.LRU
#         while curr:
#             print("[", curr, "]", end=' => ')
#             curr = curr.prev
#         print("\n")
        
    
#     def print_nodes(self):
#         if not self.nodes:
#             print("Empty")
#         else:
#             for key, node in self.nodes.items():
#                 print("[", str(key) + ",", node.value, "]", end=', ')
#             print()
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)