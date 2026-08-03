# 380. Insert Delete GetRandom O(1)

# Implement the RandomizedSet class:

# RandomizedSet() Initializes the RandomizedSet object.
# bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
# You must implement the functions of the class such that each function works in average O(1) time complexity.


# Example 1:

# Input
# ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
# [[], [1], [2], [2], [], [1], [2], []]
# Output
# [null, true, false, true, 2, true, false, 2]

# Explanation
# RandomizedSet randomizedSet = new RandomizedSet();
# randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
# randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
# randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
# randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
# randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
# randomizedSet.insert(2); // 2 was already in the set, so return false.
# randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
 

# Constraints:

# -231 <= val <= 231 - 1
# At most 2 * 105 calls will be made to insert, remove, and getRandom.
# There will be at least one element in the data structure when getRandom is called.

# USING SET

# Time: O(N), problem with getRandom
# Space: O(N)
import random
class RandomizedSet:

    def __init__(self):
        self.randomSet = set()

    def insert(self, val: int) -> bool: # O(1)
        if val not in self.randomSet:
            self.randomSet.add(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool: # O(1)
        if val in self.randomSet:
            self.randomSet.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        random_element = random.choice(list(self.randomSet)) # O(N) as converting to list takes O(N) and also requires extra space
        return random_element
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# USING LIST
# Time: O(N), problem with remove
# Space: O(N)

import random
class RandomizedSet:

    def __init__(self):
        self.randomSet = []

    def insert(self, val: int) -> bool: # O(N) due to check of val in list
        if val not in self.randomSet:
            self.randomSet.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool: # O(N)
        if val in self.randomSet:
            self.randomSet.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        random_element = random.choice(self.randomSet) # O(1)
        return random_element
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# OPTIMISED SOLUTION USING LIST + HASH MAP

# Logic with remove even if we know the index to remove:
# Finding the index → this part is O(1), since self.randomHash[val] gives you idx directly via a dict lookup. 
# Removing the element at that index → this part is where the O(n) cost comes from, and it has nothing to do with searching.
# Why removal itself costs O(n)

# Python lists are implemented as dynamic arrays (contiguous blocks of memory), not linked lists. 
# This means each element sits in a specific memory slot, indexed by position.

# When you call self.randomSet.pop(idx) where idx is not the last index, Python has to:
# Remove the element at idx
# Shift every element after idx one position to the left, to close the gap and keep the array contiguous -> this causes O(N)

import random
class RandomizedSet:

    def __init__(self):
        self.randomSet = []
        self.randomHash = {}  # {number: its index in list}

    def insert(self, val: int) -> bool:
        if val not in self.randomHash:
            self.randomSet.append(val) # appending at the end
            self.randomHash[val] = len(self.randomSet)-1 # the newest index will be last index
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.randomHash:           # check if in hash map
            idx = self.randomHash[val]       # find the index of the value to be removed
            lastElement = self.randomSet[-1] 
            self.randomSet[-1] = val         # make the last element as the value to be removed 
            self.randomSet[idx] = lastElement# convert the value to be removed at its old index to lastelement
            self.randomSet.pop()             # pop the last element which is the value to be removed
            self.randomHash[lastElement] = idx # update the hash
            del self.randomHash[val]         # only delete at the end, after updating the hashmap
            return True
        else:
            return False

    def getRandom(self) -> int:
        random_element = random.choice(self.randomSet)
        return random_element


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


# EDGE CASE HANDLING

# if the remove code was like this:
def remove(self, val: int) -> bool:
    if val in self.randomHash:           
        idx = self.randomHash[val]       
        lastElement = self.randomSet[-1] 
        self.randomSet[-1] = val         
        self.randomSet[idx] = lastElement
        self.randomSet.pop()    
        del self.randomHash[val] # the element is removed before adding to hashmap. Single element edge case is triggered         
        self.randomHash[lastElement] = idx 
                
        return True
    else:
        return False
# Workflow of the edge case

# Step 1 — RandomizedSet()
# list = [], hash = {}

# Step 2 — remove(0)
# 0 isn't in hash → returns False. Nothing changes.

# Step 3 — remove(0)
# Same as above → returns False.

# Step 4 — insert(0)
# 0 not in hash → append it. list = [0], hash = {0: 0} → returns True.

# Step 5 — getRandom()
# Only element in the list → returns 0.

# Step 6 — remove(0) ← this is where it breaks
# 0 is in hash, so we proceed:

# idx = hash[0] = 0
# lastElement = list[-1] = 0 — since 0 is the only element, lastElement and val are literally the same value.
# The swap steps run (harmlessly, since there's only one slot), then list.pop() → list = []. The list is now correctly empty.
# del hash[0] → hash = {}. Correct so far — the key is gone.
# hash[lastElement] = idx → since lastElement == 0, this executes hash[0] = 0 → hash becomes {0: 0} again. The deletion just performed gets silently undone.
# remove(0) returns True (correctly, since 0 really was removed from the list) — but the internal state is now inconsistent: list = [] but hash = {0: 0}.

# Step 7 — insert(0)
# The check is if val not in self.randomHash. Since the corrupted hash still contains the key 0, this check is True (0 is in hash) → the else branch runs → returns False, and — critically — 0 is never appended back to list.

# That's the failure: insert(0) should return True (since 0 isn't actually present in the conceptual set anymore — the list is empty) and should add 0 back in. 
# Instead it wrongly reports False and the set stays permanently empty for the value 0, even though the caller was told the insert "failed because it already exists."