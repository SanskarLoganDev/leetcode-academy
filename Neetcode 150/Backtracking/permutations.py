# 46. Permutations
# Neetcode 150 (Important)

# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Example 2:

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]

# Example 3:

# Input: nums = [1]
# Output: [[1]]
 

# Constraints:

# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.

# Key operations per recursion node:

# You iterate for num in nums: → O(n) loop each call.

# Inside the loop you do if num in path: where path is a list → membership check is O(len(path)), up to O(n).

# So each recursion call costs up to O(n · n) = O(n²) in the worst case.
# And O(n!) total calls.

# So total time complexity is O(n² · n!) in the worst case.

from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(path):
            if len(path)==len(nums):
                res.append(path.copy())
                return
            for num in nums:
                if num in path:
                    continue

                path.append(num)
                backtrack(path)
                path.pop()

        backtrack([])

        return res
    
    
# Optimized solution using sets
# You do not need a “fresh set per permutation.” You need a fresh set per recursion path (i.e., for the current partial permutation). Backtracking gives you that by undoing changes as you return from recursion.

# What actually happens

# At each choice:

# You add a number to used and append to path.

# You recurse.

# When you come back, you remove that number from used and pop from path.

# Time complexity: O(N*N!) where N is length of input array nums. There are N! permutations and to construct each permutation we do O(N) work.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = set()
        path = []

        def backtrack():
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for num in nums:
                if num in used:
                    continue
                used.add(num)
                path.append(num)

                backtrack()

                path.pop()
                used.remove(num)

        backtrack()
        return res

# Logic behind no backtracking call after popping:

# In subsets, each element has exactly two explicit branches at index i:

# include nums[i]

# exclude nums[i]

# So you must make two recursive calls—one for each branch—separated by a pop() to undo the include:

# temp.append(nums[i])
# backtrack(i+1)     # include branch
# temp.pop()
# backtrack(i+1)     # exclude branch


# That second backtrack(i+1) after pop() is not “because we popped”; it exists because there is a separate exclude decision that must be explored.

# In permutations, the branching is already handled by the for loop

# In your permutations solution, the “branches” are:
# “At this position, choose any remaining number.”

# Key point

# After path.pop(), you do not call backtrack(path) again, because:

# The next iteration of the for loop automatically tries the next candidate number, which is the next branch.

# Calling backtrack(path) again immediately after pop would just re-run the same level without having chosen a new number, leading to duplicates or an incorrect explosion of calls.

# So in permutations:

# One recursive call per choice is enough.

# The loop provides the “other choices” (the sibling branches).