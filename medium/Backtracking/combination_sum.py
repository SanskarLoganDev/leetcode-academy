# 39. Combination Sum
# Neetcode 150 (Important)

# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

# Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:

# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# Example 3:

# Input: candidates = [2], target = 1
# Output: []

# time complexity: O(N^(T/M)) where N is number of candidates, T is target and M is minimum value in candidates.
from typing import List

# backtracking with for loop (general template)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        temp = []
        def backtrack(idx, total):
            if total<0:
                return
            if total==0: # found a valid combination
                res.append(temp.copy())
                return
            for i in range(idx, len(candidates)):
                temp.append(candidates[i]) # include candidates[i]
                backtrack(i, total - candidates[i])   # i (NOT i+1) because reuse is allowed
                temp.pop() # backtrack after exploring that path

        backtrack(0, target)

        return res

# same logic without for loop
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        temp = []
        def backtrack(i, total):
            if total==target: # found a valid combination
                res.append(temp.copy()) 
                return
            elif total>target: # exceed the target, no need to proceed further
                return
            if i >= len(candidates): # when we have exhausted all candidates
                return
            
            temp.append(candidates[i])
            backtrack(i, total+candidates[i]) # not i+1 because we can reuse same element
            temp.pop()
            backtrack(i+1, total) # move to next index

        backtrack(0, 0)

        return res
    
# Handling of total:
# we never explicitly subtract from total. The reason total “goes back down” is:

# total is not a global variable.

# total is a function parameter, so each recursive call has its own copy of total stored on the call stack.

# When a deeper call returns, Python resumes the previous call frame, which still has its earlier total.

# Also, integers in Python are immutable, so total + x creates a new integer; it does not modify the existing total in the caller.


# Dry run (key calls only, with a clear trace)

# Start:

# temp = []

# call backtrack(0, 0) where candidates[0] = 2

# Level 1: i=0 (candidate=2), total=0

# Choice A: Take 2

# temp = [2]

# call backtrack(0, 2)

# i=0, total=2

# Take 2 again:

# temp = [2,2]

# call backtrack(0, 4)

# i=0, total=4

# Take 2 again:

# temp = [2,2,2]

# call backtrack(0, 6)

# i=0, total=6

# Take 2 again:

# temp = [2,2,2,2]

# call backtrack(0, 8)

# Now total=8 > 7, so return (prune).
# Backtrack (pop last 2):

# temp becomes [2,2,2]

# Now we do Choice B: Skip 2 (move to next candidate):

# call backtrack(1, 6) where candidate=3

# i=1 (candidate=3), total=6

# Take 3:

# temp = [2,2,2,3]

# call backtrack(1, 9) → total>7, return
# Pop 3:

# temp = [2,2,2]

# Skip 3:

# call backtrack(2, 6) where candidate=6
# Take 6 → total=12 >7 return; skip 6 → try 7 → total=13 >7 return
# Eventually all pruned, return up.

# Back up to:

# temp = [2,2]

# we were at backtrack(0, 4) after exploring “take 2 until too big”.

# Back at i=0, total=4, temp=[2,2]

# Now we do Skip 2:

# call backtrack(1, 4) where candidate=3

# i=1 (candidate=3), total=4

# Take 3:

# temp = [2,2,3]

# call backtrack(1, 7)

# Now total == target (7):

# add [2,2,3] to res
# Return.
# Pop 3:

# temp = [2,2]

# Skip 3:

# call backtrack(2, 4) (try 6,7…) all exceed → return.

# So one solution found: [2,2,3]

# Now the recursion returns further up

# Back to:

# temp = [2] at backtrack(0,2)

# At backtrack(0,2), after exploring take-paths, we do Skip 2:

# call backtrack(1, 2) with candidate=3

# i=1, total=2

# Take 3:

# temp = [2,3]

# call backtrack(1, 5)

# i=1, total=5

# Take 3:

# temp = [2,3,3]

# call backtrack(1, 8) >7 return
# Pop:

# temp = [2,3]
# Skip 3 → try 6,7 → all exceed → return

# No new solution here.

# Back up again to start:

# temp = [] at backtrack(0,0)

# Now do Skip 2 at root:

# call backtrack(1, 0) with candidate=3

# Root skip branch: i=1, total=0 (candidate=3)

# Try combinations starting with 3:

# [3,3,3] exceeds

# [3,6] exceeds

# [3,7] exceeds
# No solution.

# Skip 3:

# call backtrack(2,0) candidate=6
# Try 6: [6] then try 6 again exceeds, try 7 exceeds

# Skip 6:

# call backtrack(3,0) candidate=7
# Take 7:

# temp = [7]

# call backtrack(3,7) ⇒ total==target
# Add [7].

# So second solution found: [7]

# Final result

# res = [[2,2,3], [7]]

# Why this avoids duplicates (important)

# Notice you never go backward in indices.

# Once you skip from i to i+1, you will never again consider candidates before i+1.

# That prevents generating permutations like [3,2,2] after [2,2,3].

# This “non-decreasing index” constraint is the core reason duplicates don’t appear.