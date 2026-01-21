# 213. House Robber II
# Neetcode 150 (Important)

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

# Example 1:

# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

# Example 2:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

# Example 3:

# Input: nums = [1,2,3]
# Output: 3
 

# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 1000

# using to down dynamic programming with memoization

from typing import List
# time complexity O(N) and space complexity O(N)
class Solution:
    def house_robber(self, nums: List[int]) -> int: # helper function to solve house robber 1 problem. Same as house robber 1 problem
        n = len(nums)
        memo = {}
        def solve(i):
            if i>=n:
                return 0
            if i in memo:
                return memo[i]
            steal = nums[i]+solve(i+2) # rob current house and move to i+2
            skip = solve(i+1) # skip current house and move to i+1
            memo[i] = max(steal, skip)
            return max(steal, skip)
        return solve(0)
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # edge case as take [0:0] and skip [1:1] will not consider when n=1
        if n==1:
            return nums[0]

        take = nums[0:n-1] # all elements from 0 to n-2
        skip = nums[1:n] # all elements from 0 to n-1
        return max(self.house_robber(take), self.house_robber(skip)) # return the maximum of taking first element and skipping last or skipping first and taking last
          
# time complexity O(N) and space complexity O(N)
# using bottom up dynamic programming (tabulation)       
class Solution:
    def house_robber(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*(n+1) # max stolen money till house i
        # dp[i] = max stolen money till i house

        # no house or uptill 1st house (at index 0 in nums) will be 
        # sum of conditions before it but since this is the first house, it is 0
        dp[0] = 0
        dp[1] = nums[0] # only one house to rob

         # fill dp array

        for i in range(2, len(dp)): # here i goes through dp array
            steal = nums[i-1] + dp[i-2] # rob current house and add money from i-2
            skip = dp[i-1] # skip current house and take money till i-1

            dp[i] = max(steal, skip) # store maximum of stealing or skipping
        return dp[n] # maximum money till last house
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # edge case as take [0:0] and skip [1:1] will not consider when n=1
        if n==1:
            return nums[0]

        take = nums[0:n-1] # all elements from 0 to n-2
        skip = nums[1:n] # all elements from 0 to n-1
        return max(self.house_robber(take), self.house_robber(skip))
          