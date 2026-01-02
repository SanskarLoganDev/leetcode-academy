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

# Detailed trace for nums = [1,2,3]

# I will number the steps.
# I’ll show:

# Call: backtrack(i)

# What i means

# temp before / after

# When we save a subset

# Start:

# temp = []

# results = []

# Call backtrack(0) (deciding about nums[0] = 1)

# Call 1: backtrack(0) (decide about 1)
# Option 1: INCLUDE 1

# temp.append(1) → temp = [1]

# Call backtrack(1) (now decide about 2)

# Call 2: backtrack(1) (decide about 2), temp = [1]
# Option 1: INCLUDE 2

# temp.append(2) → temp = [1, 2]

# Call backtrack(2) (now decide about 3)

# Call 3: backtrack(2) (decide about 3), temp = [1,2]
# Option 1: INCLUDE 3

# temp.append(3) → temp = [1, 2, 3]

# Call backtrack(3) (base case)

# Call 4: backtrack(3) (base case), temp = [1,2,3]

# Base case hit → results.append([1,2,3])

# results = [[1,2,3]]

# Return to Call 3 (where we were deciding about 3)

# Now we must undo the include of 3 to try the exclude branch:

# temp.pop() → removes 3 → temp = [1,2]

# Option 2: EXCLUDE 3

# Call backtrack(3) again

# Call 5: backtrack(3) (base case), temp = [1,2]

# Save snapshot → results.append([1,2])

# results = [[1,2,3], [1,2]]

# Return to Call 3

# We are done with both include/exclude for 3. So Call 3 finishes and returns to Call 2 (where we were deciding about 2).

# But before returning, remember: Call 2 had included 2 earlier, so now we must undo that to try excluding 2.

# temp.pop() → removes 2 → temp = [1]

# Option 2: EXCLUDE 2

# Call backtrack(2) (decide about 3) with temp = [1]

# Call 6: backtrack(2) (decide about 3), temp = [1]
# Option 1: INCLUDE 3

# temp.append(3) → temp = [1,3]

# Call backtrack(3) base case

# Call 7: backtrack(3) base case, temp = [1,3]

# Save → results.append([1,3])

# results = [[1,2,3],[1,2],[1,3]]

# Return to Call 6

# Undo include of 3:

# temp.pop() → temp = [1]

# Option 2: EXCLUDE 3

# Call backtrack(3) base case

# Call 8: backtrack(3) base case, temp = [1]

# Save → results.append([1])

# results = [[1,2,3],[1,2],[1,3],[1]]

# Return to Call 6

# Now Call 6 is done (both choices for 3), so it returns to Call 2.
# Call 2 is also done (both include/exclude for 2), so it returns to Call 1 (where we were deciding about 1).

# But we had included 1 at the very beginning, so to explore excluding 1, we must undo it:

# temp.pop() → removes 1 → temp = []

# Back to Call 1: backtrack(0) (decide about 1), temp = []
# Option 2: EXCLUDE 1

# Call backtrack(1) (decide about 2) with temp = []

# Call 9: backtrack(1) (decide about 2), temp = []
# Option 1: INCLUDE 2

# temp.append(2) → temp = [2]

# Call backtrack(2) (decide about 3)

# Call 10: backtrack(2) (decide about 3), temp = [2]
# Option 1: INCLUDE 3

# temp.append(3) → temp = [2,3]

# Call backtrack(3) base case

# Call 11: backtrack(3) base case, temp = [2,3]

# Save → results.append([2,3])

# results = [[1,2,3],[1,2],[1,3],[1],[2,3]]

# Return to Call 10

# Undo include 3:

# temp.pop() → temp = [2]

# Option 2: EXCLUDE 3

# Call backtrack(3) base case

# Call 12: backtrack(3) base case, temp = [2]

# Save → results.append([2])

# results = [[1,2,3],[1,2],[1,3],[1],[2,3],[2]]

# Return to Call 10

# Call 10 done → return to Call 9.
# Undo include 2 (to explore excluding 2):

# temp.pop() → temp = []

# Option 2: EXCLUDE 2

# Call backtrack(2) (decide about 3) with temp = []

# Call 13: backtrack(2) (decide about 3), temp = []
# Option 1: INCLUDE 3

# temp.append(3) → temp = [3]

# Call backtrack(3) base case

# Call 14: backtrack(3) base case, temp = [3]

# Save → results.append([3])

# results = [[1,2,3],[1,2],[1,3],[1],[2,3],[2],[3]]

# Return to Call 13

# Undo include 3:

# temp.pop() → temp = []

# Option 2: EXCLUDE 3

# Call backtrack(3) base case

# Call 15: backtrack(3) base case, temp = []

# Save → results.append([])

# results = [[1,2,3],[1,2],[1,3],[1],[2,3],[2],[3],[]]

# Return and unwind completely.
