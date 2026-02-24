# 55. Jump Game
# Neetcode 150 (Important)

# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

# Constraints:

# 1 <= nums.length <= 104
# 0 <= nums[i] <= 105

from typing import List

# time complexity O(N^2) where N is the length of nums because in the worst case we will have to check all the jumps from each index, 
# With your memoization, each index i is computed at most once (after that you return memo[i]), but computing it requires looping over up to nums[i] jumps.

# space complexity O(N)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = len(nums)-1
        memo = {}
        def jump(i):
            if i + nums[i] >= len(nums) - 1: # if we can jump to the end from the current index, then we can return true
                return True
            if i in memo:
                return memo[i]
            for j in range(nums[i],0,-1): # we start from the maximum jump length and go down to 1 because if we can jump to the end from the current index, then we can return true, otherwise we will check the next jump length
                if jump(i+j):
                    memo[i] = True
                    return memo[i]
            memo[i] = False
            return memo[i]
        return jump(0)
    
# Using bottom up DP

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False]*(n) # dp[i] will be True if we can jump to the end from index i, otherwise it will be False
        dp[0] = True # we can always jump to the first index because we are already there
        for i in range(1, n):
            for j in range(i-1, -1, -1): # we start from the previous index and go down to the first index because to check if we can jump to the current index from any of the previous indices
                if j+nums[j]>=i and dp[j]==True: #
                    dp[i] = True
                    break
        return dp[n-1] # we return the last index of dp because it will be True if we can jump to the end from the first index, otherwise it will be False
    
# optimised solution using greedy approach
# time complexity O(N) where N is the length of nums because we will loop through the array once, 
# space complexity O(1) because we are using only a constant amount of space to store the maximum reachable index
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = nums[0]
        for i in range(len(nums)):
            if i>max_reachable:
                return False
            max_reachable = max(max_reachable, i+nums[i]) # we update the maximum reachable index by taking the maximum of the current maximum reachable index and the index we can jump to from the current index
        return True