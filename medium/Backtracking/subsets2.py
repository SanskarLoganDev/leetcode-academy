# 90. Subsets II
# Neetcode 150 (Important)

# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:

# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]
 

# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10

# time complexity: O(N * 2^N) where N is length of input array nums. As for each of N options we have 2 choices (include or exclude)
# Space complexity: O(N) where N is length of input array nums
from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # sorting to ensure duplicates are adjacent
        res = []
        temp = []
        used = set() # to track unique subsets
        def backtrack(i):
            if i>=len(nums):
                key = tuple(temp) # using tuple as lists are unhashable
                if key in used:
                    return
                res.append(temp.copy()) # add current subset to results
                used.add(key) # add the current subset to used set
                return
            
            temp.append(nums[i])
            backtrack(i+1)
            temp.pop()
            backtrack(i+1)
        backtrack(0)
        return res
    
# Same time complexity but optimized solution without using extra set
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # sorting to ensure duplicates are adjacent
        res = []
        temp = []

        def backtrack(i):
            if i>=len(nums):
                res.append(temp.copy())
                return
            
            temp.append(nums[i])
            backtrack(i+1)
            temp.pop()
# Following while loop means:
# If the current number is the same as the next number,
# keep moving i forward until you reach the last occurrence of this duplicate run.
# So if you are at the first 2 in [1,2,2,2,3], this loop jumps i to the last 2.

            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            backtrack(i+1)
        backtrack(0)
        return res
    
# A precise duplicate scenario in this problem (with actual duplicates)

# Let’s use a standard duplicates case:

# Input (unsorted):
# nums = [2, 1, 2]


# Your recursion generates subsets in input order. You will get (among others):

# Choose index 0 (2) and index 1 (1): subset [2, 1]

# Choose index 1 (1) and index 2 (2): subset [1, 2]

# Now, these represent the same set {1,2}, and for subsetsWithDup, you want only one copy of [1,2] (order doesn’t matter to the mathematical subset).

# But your used keys become:

# (2,1)

# (1,2)

# They are different keys, so both get included. That is the logical bug.

# Let’s see it explicitly

# Two different ways to pick a 2:

# pick the first 2 (index 0) + pick 1 (index 1) → [2,1]

# pick 1 (index 1) + pick the second 2 (index 2) → [1,2]

# Same subset content, different ordering due to how indices are arranged.

# Summary (why sorting fixes it)

# Your duplicate filter is based on exact sequence equality (tuple equality).

# Without sorting, the same subset can appear as different sequences like [2,1] and [1,2].

# Sorting makes every subset representation consistent (canonical), so duplicates collapse properly.