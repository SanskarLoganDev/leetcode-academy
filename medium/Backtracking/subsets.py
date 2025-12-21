# 78. Subsets
# Neetcode 150 (Important)

# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.


# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]
 

# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.

# Time comeplexity: O(N*2^N) where N is length of input array nums. As for each of N options we have 2 choices (include or exclude)
# Space complexity: O(N) where N is length of input array nums

from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        temp = []
        def backtrack(i):
            if i>=len(nums):
                results.append(temp.copy()) # here we use temp.copy() to avoid reference issues instead of just temp because temp will be modified later
                return
            temp.append(nums[i]) # include nums[i]
            backtrack(i+1) # move to next index
            temp.pop() # exclude nums[i]
            backtrack(i+1) # move to next index
 
        backtrack(0) # start backtracking from index 0

        return results
        
# temp.copy() explanation:

# Consider nums = [1, 2].

# Without .copy()

# At some base case, suppose temp = [1, 2].

# You do:

# results.append(temp)


# Now imagine later backtracking does:

# temp.pop()  # temp becomes [1]
# temp.pop()  # temp becomes []


# Because results[0] points to the same object as temp, it will also appear as [].

# So even though you “added” [1, 2] earlier, you didn’t store a frozen version—you stored the same container that later got emptied.

# With .copy()

# At the same base case (temp = [1, 2]):

# results.append(temp.copy())


# Now results stores a different list object, e.g. [1, 2] in a new container. When temp later becomes [], the stored [1, 2] remains unchanged.


# Dry run (step-by-step) for backtracking

# Example: nums = [1, 2]

# I’ll show (i, temp) and what happens.

# Start:

# backtrack(0), temp = []

# At i = 0 (consider element 1)

# Include 1

# temp.append(1) → temp = [1]

# call backtrack(1)

# At i = 1 (consider element 2), temp = [1]

# Include 2

# temp.append(2) → temp = [1, 2]

# call backtrack(2)

# Base case i = 2 (past end)

# append snapshot: results += [[1, 2]]

# return

# Backtrack step

# temp.pop() removes last element (2) → temp = [1]

# Exclude 2

# call backtrack(2) with temp = [1]

# Base case i = 2

# append snapshot: results += [[1]]

# return

# Return to i = 0 level, backtrack further

# temp.pop() removes last element (1) → temp = []

# At i = 0 again, temp = []

# Exclude 1

# call backtrack(1)

# At i = 1 (consider element 2), temp = []

# Include 2

# temp.append(2) → temp = [2]

# call backtrack(2)

# Base case i = 2

# append snapshot: results += [[2]]

# return

# Backtrack

# temp.pop() → temp = []

# Exclude 2

# call backtrack(2) with temp = []

# Base case i = 2

# append snapshot: results += [[]]

# return

# Done.

# Final results:

# [[1, 2], [1], [2], []]

# Key backtracking insight

# temp.append(x) = “choose”

# recursive call = “explore with that choice”

# temp.pop() = “undo choice” (so the next branch starts from the previous clean state)

# If you want, I can also draw the recursion tree for [1,2,3] so you can visually see how the include/exclude branches generate 2^n subsets.