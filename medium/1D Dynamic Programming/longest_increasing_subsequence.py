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
                
                
# Using patience sorting with binary search
# time complexity O(N log N) and 
# space complexity O(N)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        for i in range(len(nums)): # iterate through all numbers
            if not res: # if res is empty
                res.append(nums[i])
                continue
            # binary search for the index of the smallest number >= nums[i]
            l = 0
            r = len(res)-1
            idx = float("inf") # index of smallest number >= nums[i]

            while l<=r:
                mid = (l+r)//2
                if res[mid]>=nums[i]: # found a number >= nums[i]
                    idx = mid
                    r = mid-1
                else:
                    l = l+1
            if idx == float("inf"): # means no number in res is >= nums[i]
                res.append(nums[i]) # append nums[i] to the end
            else:
                res[idx] = nums[i] # replace the number at idx with nums[i]
        return len(res) # length of res is the length of longest increasing subsequence
                
# patience sorting using inbuilt bisect module for binary search

import bisect
# here bisect.bisect_left(res, x) returns the index of the first element in res which is >= x
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []  # res[k] = smallest possible tail of an LIS of length k+1
        for x in nums:
            idx = bisect.bisect_left(res, x)  # first position with res[idx] >= x
            if idx == len(res):
                res.append(x)
            else:
                res[idx] = x
        return len(res)
