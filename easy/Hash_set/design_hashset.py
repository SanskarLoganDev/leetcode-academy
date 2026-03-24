# 705. Design HashSet

# Design a HashSet without using any built-in hash table libraries.

# Implement MyHashSet class:

# void add(key) Inserts the value key into the HashSet.
# bool contains(key) Returns whether the value key exists in the HashSet or not.
# void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
 

# Example 1:

# Input
# ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
# [[], [1], [2], [1], [3], [2], [2], [2], [2]]
# Output
# [null, null, null, true, false, null, true, null, false]

# Explanation
# MyHashSet myHashSet = new MyHashSet();
# myHashSet.add(1);      // set = [1]
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(1); // return True
# myHashSet.contains(3); // return False, (not found)
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(2); // return True
# myHashSet.remove(2);   // set = [1]
# myHashSet.contains(2); // return False, (already removed)
 

# Constraints:

# 0 <= key <= 106
# At most 104 calls will be made to add, remove, and contains.

# Brute force approach, using list to implement hashset, time and space: O(N) for every operation
class MyHashSet:

    def __init__(self):
        self.s = []

    def add(self, key: int) -> None:
        if key not in self.s:
            self.s.append(key)

    def remove(self, key: int) -> None:
        if key in self.s:
            self.s.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.s:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


# optimized solution using hashing

# Hashing concepts
# bascially diving by a number and getting remainder as the index and then inserting in that index.
# but here we see that there might be collision: for example number 21 and 31 will result in same index when num%10

# Collision avoiding techniques
# 1) Separate chaining: Implemented below, at each index we will have a list and keep inserting numbers in it
# here we might also face an issue when our main array gets filled and there is no more space or very less space left
# ideally here load factor (% of indexes of main aray filled) comes onto play, for example if load factor reaches 75%, then its time for re-hashing
# re-hashing = double the size of array and hash again (not implmented here) 

# 2) Open addressing
# A) Linear probing: in main array if a number is already there, put the key in the next index.
# B) Quadratic probing: in main array, use a quadratic equation to insert keys to indexes

# time complexity: O(1) avg for each operation
# space complexity: O(N+B) here B =  number of buckets
class MyHashSet:

    def __init__(self):
        self.size = 10000 # given in constraints that the maximum number of operations can be 10^4
        self.hashset = [[] for _ in range(self.size)]

    def add(self, key: int) -> None:
        idx = key%self.size
        if key not in self.hashset[idx]:
            self.hashset[idx].append(key)

    def remove(self, key: int) -> None:
        idx = key%self.size
        if key in self.hashset[idx]:
            self.hashset[idx].remove(key)

    def contains(self, key: int) -> bool:
        idx = key%self.size
        if key in self.hashset[idx]:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)