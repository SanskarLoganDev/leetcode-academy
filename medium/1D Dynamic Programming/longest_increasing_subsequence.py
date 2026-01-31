# 300. Longest Increasing Subsequence
# Neetcode 150 (Important)

# Given an integer array nums, return the length of the longest strictly increasing subsequence.

# Example 1:

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

# Example 2:

# Input: nums = [0,1,0,3,2,3]
# Output: 4

# Example 3:

# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 2500
# -104 <= nums[i] <= 104
 
# Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?

# Using memoization we get memory time exceeded error for large test cases on leetcode because of large state space taken my memo dictionary. 
# Adding to python dictionary is expensive operation.
# time complexity O(N^2) and 
# space complexity O(N^2) for memoization and O(N) for recursion stack
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {} # (i, prev) -> int
        n = len(nums)

        def solve(i, prev): # here prev is the value of previous element in the subsequence
            if i>=n:
                return 0

            key = (i, prev)
            if key in memo:
                return memo[key]
            # take
            # here take = 0 does not stop/interfere with recursion; It just ensures that the invalid “take” option contributes nothing
            take = 0 # default value if we don't take current element
            if nums[i]>prev: # can only take if current number is greater than previous number in subsequence
                take = 1+solve(i+1, nums[i])
            # skip
            skip = solve(i+1, prev)
            memo[key] = max(take, skip)
            return memo[key]
        return solve(0, float("-inf"))
    
# Same memoization approach with index of previous element instead of value

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)

        def solve(i, prev_i):
            if i>=n:
                return 0

            key = (i, prev_i) # prev_i is index of previous element in subsequence
            if key in memo:
                return memo[key]
            # take
            take = 0
            # new check of prev_i==-1
            if prev_i==-1 or nums[i]>nums[prev_i]: # if prev_i==-1 means no previous element taken yet
                take = 1+solve(i+1, i)
            # skip
            skip = solve(i+1, prev_i)
            memo[key] = max(take, skip)
            return memo[key]
        return solve(0, -1)
    
# Using bottom-up DP approach
# time complexity O(N^2) and space complexity O(N)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums) # dp[i] = length of longest increasing subsequence ending at index i
        # all values initialized to 1 because minimum length of increasing subsequence ending at any index is 1 (the element itself)

        for i in range(len(nums)):
            for j in range(i+1):
                if nums[i]<=nums[j]: # nums[i] must be greater than nums[j] to form increasing subsequence
                    continue
                
                new_sub_len = dp[j]+1 # length of increasing subsequence ending at i if we take nums[i] after nums[j]
                if dp[i]>=new_sub_len: # if current length is already greater than or equal to new_sub_len
                    continue
                dp[i] = new_sub_len # update dp[i] to new_sub_len
        return max(dp)
                
