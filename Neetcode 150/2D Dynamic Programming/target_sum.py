# 494. Target Sum
# Neetcode 150 (Important)

# You are given an integer array nums and an integer target.

# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
# Return the number of different expressions that you can build, which evaluates to target.
 

# Example 1:

# Input: nums = [1,1,1,1,1], target = 3
# Output: 5
# Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3

# Example 2:

# Input: nums = [1], target = 1
# Output: 1
 
# Constraints:

# 1 <= nums.length <= 20
# 0 <= nums[i] <= 1000
# 0 <= sum(nums[i]) <= 1000
# -1000 <= target <= 1000

# Recursive solution
# time complexity: O(2^n) as for each number we have 2 choices and 
# space complexity O(n) for recursion stack

from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        def solve(i, amt):
            if i==n:
                return 1 if amt==0 else 0
            
            # consider positive
            pos = solve(i+1, amt - nums[i])

            # consider negative
            neg = solve(i+1, amt - (-1)*nums[i])

            return pos+neg
        return solve(0, target) 
    
# Using memoization to optimize the above solution
# time complexity O(n*amount) as we are storing results for each index and amount combination
# space complexity O(n*amount) for memoization table and O(n) for recursion stack

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}
        def solve(i, amt):
            if i==n:
                return 1 if amt==0 else 0
            key = (i, amt)
            if key in memo:
                return memo[key]
            
            # consider positive
            pos = solve(i+1, amt - nums[i])

            # consider negative
            neg = solve(i+1, amt - (-1)*nums[i])
            memo[key] = pos+neg
            return memo[key]
        return solve(0, target) 

# Bottom-up DP solution
# time complexity O(n*amount) as we are storing results for each index and amount combination
# space complexity O(amount) for dp array
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {} # dp[s] = number of ways to get sum s
        dp[0] = 1  # base case: one way to get sum 0 (by choosing nothing)
        for n in nums:
            next_dp = {}
            for s, cnt in dp.items(): # for each sum s we have cnt ways to get that sum
                next_dp[s+n] = next_dp.get(s+n, 0) + cnt # add current number positively
                next_dp[s-n] = next_dp.get(s-n, 0) + cnt # add current number negatively
            dp = next_dp
        return dp.get(target, 0) # return number of ways to get target or 0 if not possible