# 706. Design HashMap

# Design a HashMap without using any built-in hash table libraries.

# Implement the MyHashMap class:

# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
# int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
 

# Example 1:

# Input
# ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
# [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
# Output
# [null, null, null, 1, -1, null, 1, null, -1]

# Explanation
# MyHashMap myHashMap = new MyHashMap();
# myHashMap.put(1, 1); // The map is now [[1,1]]
# myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
# myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
# myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
# myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
# myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
# myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
# myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]

# Constraints:

# 0 <= key, value <= 106
# At most 104 calls will be made to put, get, and remove.

# Time complexity
# put(key, value)
# Scans the list to see if key exists: O(n)
# If found: update and return (still worst-case O(n) if key is at end / not present)
# If not found: append is O(1) amortized

# ✅ Worst-case: O(n)
# ✅ Best-case: O(1) (if the first element matches)
# ✅ Amortized append: O(1), but scan dominates

# get(key)
# Linear scan over all pairs: O(n)

# ✅ Worst-case: O(n)
# ✅ Best-case: O(1) (first pair matches)

# remove(key)
# Linear scan to find the key: O(n)
# pop(i) in a Python list shifts elements after index i: O(n) in worst case

# So combined worst-case:

# find key: O(n)
# shifting after pop: O(n)

# ✅ Worst-case: O(n) (because O(n) + O(n) = O(n))
# ✅ Best-case: O(1) if key at end? (find might still be O(1) if first; pop at end is O(1))

class MyHashMap:

    def __init__(self):
        self.hashmap = []

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.hashmap)):
                if self.hashmap[i][0]==key:
                    self.hashmap[i][1] = value
                    return
        self.hashmap.append([key, value])

    def get(self, key: int) -> int:
        for k, v in self.hashmap:
            if k==key:
                return v
        return -1
            
    def remove(self, key: int) -> None:
        for i in range(len(self.hashmap)):
            if self.hashmap[i][0]==key:
                self.hashmap.pop(i)
                break


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# Another solution
# time complexity: O(1) for all operations
# but space complexity is too large, that is 10**6

class MyHashMap:

    def __init__(self):
        self.hashmap = [-1]*((10**6)+1)

    def put(self, key: int, value: int) -> None:
        self.hashmap[key] = value

    def get(self, key: int) -> int:
        return self.hashmap[key]
            
    def remove(self, key: int) -> None:
        self.hashmap[key]=-1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# time complexity amortized: O(1)
# using chaining: have array at each index and insert (key, value) at that index. retrieve index by hashing: key%size
class MyHashMap:

    def __init__(self):
        self.size = 10**4
        self.hashmap = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        idx = key%self.size
        for i in range(len(self.hashmap[idx])):
            if key==self.hashmap[idx][i][0]:
                self.hashmap[idx][i][1] = value
                return
        self.hashmap[idx].append([key, value])

    def get(self, key: int) -> int:
        idx = key%self.size
        for k, v in self.hashmap[idx]:
            if key==k:
                return v
        return -1
            
    def remove(self, key: int) -> None:
        idx = key%self.size
        for i in range(len(self.hashmap[idx])):
            if key==self.hashmap[idx][i][0]:
                self.hashmap[idx].pop(i)
                break


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)