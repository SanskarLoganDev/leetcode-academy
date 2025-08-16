# 146. LRU Cache
# Neetcode 150, Important
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

 

# Example 1:

# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]

# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
 
# Constraints:

# 1 <= capacity <= 3000
# 0 <= key <= 104
# 0 <= value <= 105
# At most 2 * 105 calls will be made to get and put.


# time complexity: O(n^2) for get and put
# space complexity: O(n), where n is the capacity of the cache

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = []
        self.cap = capacity        

    def get(self, key: int) -> int:
        for pair in self.cache:
            if pair[0]==key:
                temp = pair
                self.cache.remove(pair) # remove the pair to update its position takes o(n) time
                self.cache.append(temp)
                return temp[1]
        return -1

    def put(self, key: int, value: int) -> None:
        for pair in self.cache:
            if pair[0]==key:
                self.cache.remove(pair)
                self.cache.append((key, value))
                return
        if len(self.cache)==self.cap:
            self.cache.remove(self.cache[0])
        self.cache.append((key, value))  


class Node:
     def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # map key to node {key: Node(key, val)}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left # here we are creating a doubly linked list with left and right dummy nodes
    
    # remove from linked list
    def remove(self, node):
        nxt = node.next
        prev = node.prev
        prev.next, nxt.prev = nxt, prev # here nxt and prev are the next and previous nodes of the node to be removed

    # add to the linked list from the right
    def insert(self, node):
        nxt = self.right
        prev = self.right.prev
        prev.next = nxt.prev = node
        node.prev = prev
        node.next = nxt
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key]) # remove from the linked list
            # insert the node to the right end of the linked list
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from the linked list and remove the LRU from the hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key] # could also use self.cache.pop(lru.key)

        