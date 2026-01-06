# 40. Combination Sum II
# Neetcode 150 (Important)

# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]

# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]

# Constraints:

# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30

# time complexity: O(2^n) where n is number of candidates
# space complexity: O(n) where n is number of candidates (temp list can go upto n in worst case)

from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        temp = []
        candidates.sort() # sort to handle duplicates, do sorting when input can have duplicates
        def backtrack(idx, total):
            if total<0: # exceeded the sum
                return
            if total==0: # found a combination
                res.append(temp.copy())
                return
            for i in range(idx, len(candidates)):
                if i>idx and candidates[i]==candidates[i-1]: # skip duplicates, we do i>idx to ensure that for the first index we don't skip
                    continue

                temp.append(candidates[i]) # include candidates[i]
                backtrack(i+1, total-candidates[i]) # i+1 because each number can only be used once
                temp.pop() # backtrack # exclude candidates[i]
        backtrack(0, target)

        return res
    
# Dry run (main branches that produce results)

# I’ll show the recursion as:

# backtrack(idx, total), temp = [...]

# Start

# backtrack(0, 8), temp = []

# Loop i from 0…

# Branch 1: pick candidates[0] = 1

# temp = [1]
# call backtrack(1, 7)

# backtrack(1,7), temp=[1]

# Loop i from 1…

# 1.1 pick candidates[1] = 1

# temp = [1,1]
# call backtrack(2, 6)

# backtrack(2,6), temp=[1,1]

# Loop i from 2…

# pick 2 → temp [1,1,2], call backtrack(3,4)

# try 5 (too big → total becomes -1) return

# try 6 (total becomes -2) return

# try 7 (total becomes -3) return

# try 10 (total becomes -6) return

# no solution, back

# pick 5 → temp [1,1,5], call backtrack(4,1)

# pick 6 → total -5 return

# pick 7 → total -6 return

# pick 10 → total -9 return

# no solution

# pick 6 → temp [1,1,6], call backtrack(5,0)

# total == 0 → ADD [1,1,6]

# return, pop 6

# pick 7 → total becomes -1 return

# pick 10 → total becomes -4 return

# So from [1,1] we found: [1,1,6]

# Back to backtrack(1,7) with temp back to [1].

# 1.2 next i=2 pick candidates[2] = 2

# temp = [1,2]
# call backtrack(3,5)

# backtrack(3,5), temp=[1,2]

# Loop i from 3…

# pick 5 → temp [1,2,5], call backtrack(4,0)

# total==0 → ADD [1,2,5]

# return

# pick 6 → total becomes -1 return

# pick 7 → total becomes -2 return

# pick 10 → total becomes -5 return

# So we found: [1,2,5]

# Back to backtrack(1,7) with temp [1].

# 1.3 next i=3 pick 5

# temp [1,5] → backtrack(4,2)

# pick 6 → total -4 return

# pick 7 → total -5 return

# pick 10 → total -8 return
# No solution.

# 1.4 next i=4 pick 6

# temp [1,6] → backtrack(5,1)

# pick 7 → total -6 return

# pick 10 → total -9 return
# No solution.

# 1.5 next i=5 pick 7

# temp [1,7] → backtrack(6,0)

# total==0 → ADD [1,7]
# Return.

# 1.6 next i=6 pick 10

# temp [1,10] → total -3 return

# So from starting with the first 1, we found:

# [1,1,6]

# [1,2,5]

# [1,7]

# Now back to root backtrack(0,8), temp [].

# Root: i=1 is also 1 (duplicate at same depth)

# At root level, idx=0.
# When i=1, condition:

# if i > idx and candidates[i] == candidates[i-1]:
#     continue


# Here: i=1 > 0 and candidates[1]==candidates[0]==1 → skip.

# This is how you avoid generating the same solution sets again starting from the “second 1”.

# Root Branch 2: pick candidates[2] = 2

# temp [2] → call backtrack(3,6)

# backtrack(3,6), temp=[2]

# Loop i from 3…

# pick 5 → temp [2,5] → backtrack(4,1)

# pick 6 → total -5 return

# pick 7 → total -6 return

# pick 10 → total -9 return
# No solution

# pick 6 → temp [2,6] → backtrack(5,0)

# total==0 → ADD [2,6]

# return

# pick 7 → total becomes -1 return

# pick 10 → total becomes -4 return

# So we found: [2,6]

# Back to root.

# Root Branch 3: pick candidates[3] = 5

# temp [5] → backtrack(4,3)

# pick 6 → total -3 return

# pick 7 → total -4 return

# pick 10 → total -7 return
# No solution.

# Root Branch 4: pick candidates[4] = 6

# temp [6] → backtrack(5,2)

# pick 7 → total -5 return

# pick 10 → total -8 return
# No solution.

# Root Branch 5: pick candidates[5] = 7

# temp [7] → backtrack(6,1)

# pick 10 → total -9 return
# No solution.

# Root Branch 6: pick candidates[6] = 10

# temp [10] → backtrack(7,-2) → total < 0 return

# Final res

# Your code produces exactly:

# [1,1,6]

# [1,2,5]

# [1,7]

# [2,6]

# Which matches the expected set of unique combinations for target 8.

# What to notice about the duplicate-skip in this dry run

# At the root depth (idx=0), you skipped the second 1 (i=1).

# But you did not skip using the second 1 deeper when it was valid (e.g., [1,1,6] requires two 1s). This is why the condition is i > idx (same depth only).