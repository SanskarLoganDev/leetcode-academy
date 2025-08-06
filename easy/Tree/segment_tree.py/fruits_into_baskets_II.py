# 3477. Fruits Into Baskets II

# You are given two arrays of integers, fruits and baskets, each of length n, where fruits[i] represents the quantity of the ith type of fruit, and baskets[j] represents the capacity of the jth basket.

# From left to right, place the fruits according to these rules:

# Each fruit type must be placed in the leftmost available basket with a capacity greater than or equal to the quantity of that fruit type.
# Each basket can hold only one type of fruit.
# If a fruit type cannot be placed in any basket, it remains unplaced.
# Return the number of fruit types that remain unplaced after all possible allocations are made.

# Example 1:

# Input: fruits = [4,2,5], baskets = [3,5,4]

# Output: 1

# Explanation:

# fruits[0] = 4 is placed in baskets[1] = 5.
# fruits[1] = 2 is placed in baskets[0] = 3.
# fruits[2] = 5 cannot be placed in baskets[2] = 4.
# Since one fruit type remains unplaced, we return 1.

# Example 2:

# Input: fruits = [3,6,1], baskets = [6,4,7]

# Output: 0

# Explanation:

# fruits[0] = 3 is placed in baskets[0] = 6.
# fruits[1] = 6 cannot be placed in baskets[1] = 4 (insufficient capacity) but can be placed in the next available basket, baskets[2] = 7.
# fruits[2] = 1 is placed in baskets[1] = 4.
# Since all fruits are successfully placed, we return 0.

# Constraints:

# n == fruits.length == baskets.length
# 1 <= n <= 100
# 1 <= fruits[i], baskets[i] <= 1000

from typing import List

# time complexity: O(n^2)
# space complexity: O(n)
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        i = 0
        used = []

        while i<len(fruits):
            j=0
            while j<len(baskets):
                if fruits[i]<=baskets[j] and j not in used:
                    used.append(j)
                    break
                j+=1
            i+=1
        return len(fruits)-len(used)

# time complexity: O(n^2)
# space complexity: O(1) 
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        i = 0
        count = 0
        while i<len(fruits):
            j=0
            while j<len(baskets):
                if fruits[i]<=baskets[j] and baskets[j]>0:
                    baskets[j]=-1
                    break
                j+=1
            i+=1
        for n in baskets:
            if n>0:
                count+=1
        return count
    
    
# time complexity: O(nlogn)
# space complexity: O(n)

from typing import List

class Solution:
    def build(self, i: int, l: int, r: int, baskets: List[int], seg: List[int]) -> None:
        if l == r:
            seg[i] = baskets[l]
            return
        m = (l + r) // 2
        self.build(2*i+1, l, m, baskets, seg)
        self.build(2*i+2, m+1, r, baskets, seg)
        seg[i] = max(seg[2*i+1], seg[2*i+2])

    def query(self, i: int, l: int, r: int, seg: List[int], val: int) -> bool:
        # If the maximum in this segment is < val, we can't place here
        if seg[i] < val:
            return False
        # If we've narrowed it to one basket, use it
        if l == r:
            seg[i] = -1
            return True
        m = (l + r) // 2
        placed = False
        # Try left child first if it can accommodate
        if seg[2*i+1] >= val:
            placed = self.query(2*i+1, l, m, seg, val)
        else:
            placed = self.query(2*i+2, m+1, r, seg, val)
        # Update this node after child modification
        seg[i] = max(seg[2*i+1], seg[2*i+2])
        return placed

    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        # build a segment tree of size up to 4*n
        seg = [-1] * (4 * n)
        self.build(0, 0, n-1, baskets, seg)

        unplaced = 0
        for fruit in fruits:
            if not self.query(0, 0, n-1, seg, fruit):
                unplaced += 1
        return unplaced
