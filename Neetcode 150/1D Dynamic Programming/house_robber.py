# 198. House Robber
# Neetcode 150 (Important)

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

# Example 2:

# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.

# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400

# Brute force Recursion solution
# time complexity O(2^N) as we have 2 choces at each step and space complexity O(N) for recursion stack
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        def solve(i):
            if i>=n:
                return 0 # no more houses to rob so money is 0
            steal = nums[i] + solve(i+2) # rob current house and move to i+2
            skip = solve(i+1) # skip current house and move to i+1
            return max(steal, skip)
        return solve(0)
    
# Using memoization to optimize the above solution
# time complexity O(N) and space complexity O(N) for recursion stack + O(N)

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def solve(i):
            if i>=n:
                return 0
            if i in memo: # check if already computed
                return memo[i]
            steal = nums[i] + solve(i+2) # rob current house and move to i+2
            skip = solve(i+1) # skip current house and move to i+1
            memo[i] = max(steal, skip) # store in memo
            return max(steal, skip) # return the maximum of stealing or skipping
        return solve(0)
    
# Dry run

# What solve(i) means

# solve(i) = maximum money you can rob starting from house index i.

# At house i you have two choices:

# steal: take nums[i] and then jump to i+2

# steal = nums[i] + solve(i+2)

# skip: don’t take it, move to i+1

# skip = solve(i+1)

# Then:

# solve(i) = max(steal, skip)

# Base case:

# if i >= n, return 0 (no houses left)

# Dry run 1: nums = [1,2,3,1]

# Indices: 0 1 2 3
# Values: 1 2 3 1
# n = 4

# We call: solve(0)

# solve(0)

# steal = nums[0] + solve(2) = 1 + solve(2)

# skip = solve(1)
# Need solve(2) and solve(1).

# solve(2)

# steal = nums[2] + solve(4) = 3 + solve(4)

# skip = solve(3)

# solve(4)

# i=4 >= n → return 0
# So in solve(2), steal = 3 + 0 = 3

# solve(3)

# steal = nums[3] + solve(5) = 1 + solve(5)

# skip = solve(4)

# solve(5)

# i=5 >= n → return 0

# solve(4) again

# returns 0

# So:

# solve(3): steal = 1 + 0 = 1, skip = 0

# solve(3) = max(1, 0) = 1
# Store: memo[3] = 1

# Back to solve(2):

# steal = 3

# skip = solve(3) = 1

# solve(2) = max(3, 1) = 3
# Store: memo[2] = 3

# solve(1)

# steal = nums[1] + solve(3) = 2 + solve(3)

# skip = solve(2)

# We already have:

# solve(3) from memo = 1

# solve(2) from memo = 3

# So:

# steal = 2 + 1 = 3

# skip = 3

# solve(1) = max(3, 3) = 3
# Store: memo[1] = 3

# Back to solve(0):

# steal = 1 + solve(2) = 1 + 3 = 4

# skip = solve(1) = 3

# solve(0) = max(4, 3) = 4
# Store: memo[0] = 4

# Final Answer

# solve(0) = 4

# Memo at end:
# {3: 1, 2: 3, 1: 3, 0: 4}

# Dry run 2: nums = [2,1,1,2]

# Indices: 0 1 2 3
# Values: 2 1 1 2
# n = 4

# Call: solve(0)

# solve(0)

# steal = 2 + solve(2)

# skip = solve(1)
# Need solve(2) and solve(1).

# solve(2)

# steal = 1 + solve(4) = 1 + 0 = 1

# skip = solve(3)

# solve(3)

# steal = 2 + solve(5) = 2 + 0 = 2

# skip = solve(4) = 0

# solve(3) = max(2, 0) = 2
# Store: memo[3] = 2

# Back to solve(2):

# steal = 1

# skip = solve(3) = 2

# solve(2) = max(1, 2) = 2
# Store: memo[2] = 2

# solve(1)

# steal = 1 + solve(3) = 1 + 2 = 3 (solve(3) from memo)

# skip = solve(2) = 2 (from memo)

# solve(1) = max(3, 2) = 3
# Store: memo[1] = 3

# Back to solve(0):

# steal = 2 + solve(2) = 2 + 2 = 4

# skip = solve(1) = 3

# solve(0) = max(4, 3) = 4
# Store: memo[0] = 4

# Final Answer

# solve(0) = 4

# Memo at end:
# {3: 2, 2: 2, 1: 3, 0: 4}

# Interpretation: rob houses 0 and 3 → 2 + 2 = 4.

# Bottom-up Dynamic Programming solution
class Solution:
    def rob(self, nums: List[int]) -> int:
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
     