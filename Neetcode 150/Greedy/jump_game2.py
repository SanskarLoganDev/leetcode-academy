# 45. Jump Game II
# Neetcode 150 (Important)

# You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.

# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:

# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:

# Input: nums = [2,3,0,1,4]
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 104
# 0 <= nums[i] <= 1000
# It's guaranteed that you can reach nums[n - 1].

from typing import List

# time complexity O(N^2) where N is the length of nums because in the worst case we will have to check all the jumps from each index, 
# space complexity O(N^2) because we are using a memoization dictionary to store the results of subproblems
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)-1
        memo = {}
        def solve(i, step):
            min_step = float("inf")
            if i>=n:
                return step
            key = (i, step)
            if key in memo:
                return memo[key]
            for j in range(nums[i], 0, -1):
                res = solve(i+j, step+1)
                min_step = min(res, min_step)
            memo[key] = min_step
            return memo[key]
        return solve(0, 0)
    
# time complexity O(N) where N is the length of nums because we are iterating through the array once, 
# space complexity O(1) because we are using a constant amount of space to store the variables
class Solution:
    def jump(self, nums: List[int]) -> int:
        l = 0
        r = 0
        res = 0
        while r<len(nums)-1:
            farthest = 0
            for i in range(l, r+1): # we are iterating from l to r because we want to check all the jumps from the current range of indices that we can jump to, and we want to find the farthest index that we can jump to from any of these indices
                farthest = max(farthest, i+nums[i])
            l = r+1 # we update l to r+1 because we want to move to the next range of indices that we can jump to
            r = farthest
            res+=1 # we increment the result because we have made a jump to the next range of indices
            
        return res