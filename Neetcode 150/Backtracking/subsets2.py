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
            
            temp.append(nums[i]) # include nums[i]
            backtrack(i+1)
            temp.pop() # exclude nums[i]
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
            
            temp.append(nums[i]) # include nums[i]
            backtrack(i+1)
            temp.pop()
# Following while loop means:
# If the current number is the same as the next number,
# keep moving i forward until you reach the last occurrence of this duplicate run.
# So if you are at the first 2 in [1,2,2,2,3], this loop jumps i to the last 2.

            while i+1<len(nums) and nums[i]==nums[i+1]: # skip duplicates
                i+=1
            backtrack(i+1) # exclude nums[i]
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

# Example scenario to understand while loop usage:
# Zoom into the duplicate section: indices 1 and 2 are both 2
# Case A: temp = [1], call backtrack(1) (first 2)

# Your code does:

# 1) Include branch
# temp.append(2)      # temp = [1,2]
# backtrack(2)
# temp.pop()          # temp = [1]


# Now inside backtrack(2) (second 2), it again does include/exclude, so it will generate:

# [1,2,2] (include second 2)

# [1,2] (exclude second 2)

# So far, this is correct and necessary.

# 2) Exclude branch (this is where the while loop matters)

# After popping, you are back to:

# temp = [1]

# still in the frame where i = 1 and nums[i] = 2

# If you did not skip duplicates, you would do:

# backtrack(2)


# That would mean: “exclude the first 2, but still consider the second 2.”

# From there, you could include that second 2 and produce [1,2] again.

# So [1,2] would be generated twice:

# Path 1: include first 2, exclude second 2 → [1,2]

# Path 2: exclude first 2, include second 2 → [1,2] (duplicate)

# What the while loop changes

# Instead of backtrack(2), you do:

# while i+1 < len(nums) and nums[i] == nums[i+1]:
#     i += 1
# backtrack(i+1)


# At i=1, nums[1]==nums[2]==2, so i becomes 2 (last 2).
# Then backtrack(i+1) becomes backtrack(3).

# That means:
# if you exclude a 2, you exclude all consecutive 2s at once, so you never create the “exclude first, include second” duplicate path.

# So from temp=[1], excluding the 2s yields only [1] (and not [1,2] again).

# Why the while loop is after temp.pop() and not after temp.append()
# 1) Because the while loop is meant for the exclude decision

# Logically, that code block corresponds to:

# include nums[i] (normal recursion)

# exclude nums[i] (skip all duplicates of this value) and recurse

# The exclude decision happens after you return from the include branch and undo it (pop), because at that point you are exploring “what if I do NOT take nums[i]?”

# 2) If you skipped duplicates right after adding, you would break valid subsets

# Example: nums = [2,2]

# If you skipped duplicates immediately after adding the first 2, you might jump past the second 2 and you would lose the subset [2,2], which is valid and must be included.

# In other words:

# The include path must not skip duplicates, because you may want to include multiple copies.

# The exclude path should skip duplicates, because “exclude this value” should exclude all its identical copies at the same recursion depth.

# That is the main invariant.