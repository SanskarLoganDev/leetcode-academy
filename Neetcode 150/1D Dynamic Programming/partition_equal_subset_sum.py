# 416. Partition Equal Subset Sum
# Neetcode 150 (Important)

# Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

# Example 1:

# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].

# Example 2:

# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.
 
# Constraints:

# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100

# Recursive solution without memoization
# time complexity O(2^N) as we have 2 choices at each step and 
# space complexity O(N) for recursion stack
from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        total = sum(nums)//2
        def solve(i, target):
            if target==0: # base case: found a subset with required sum
                return True
            if target<0 or i>=len(nums): # base case: exceeded sum or no more elements to process
                return False
            take = 0 # take = 0 or take = False as default value if we don't take current element
            if nums[i]<=target: # can only take if current number is less than or equal to target
                take = solve(i+1, target-nums[i])
            skip = solve(i+1, target) # skip current element
            return take or skip # return True if either take or skip is True

        return solve(0, total) # start from index 0 and target sum as total sum/2
    
# Using memoization to optimize the above solution
# time complexity O(N*target) and space complexity O(N*target) for memoization
# this solution throws memory limit exceeded error on leetcode for large test cases due to large state space taken by memo dictionary
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        memo = {}
        total = sum(nums)//2
        def solve(i, target):
            if target==0: # base case: found a subset with required sum
                return True
            if target<0 or i>=len(nums): # base case: exceeded sum or no more elements to process
                return False
            key = (i, target)
            if key in memo: # check if already computed
                return memo[key]
            take = 0 # take = 0 or take = False as default value if we don't take current element
            if nums[i]<=target: # can only take if current number is less than or equal to target
                take = solve(i+1, target-nums[i])
            skip = solve(i+1, target) # skip current element
            memo[key] = take or skip # store in memo
            return memo[key] # return True if either take or skip is True

        return solve(0, total)
    
# Bottom-up DP solution using set
# time complexity O(N*target) and space complexity O(target)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        dp = set() # dp set to store achievable subset sums
        target = sum(nums)//2
        for n in nums:
            nextDP = set(dp) # create a new set for the next state which has all previous achievable sums
            if n==target:
                return True
            if not dp: # first element case
                dp.add(0) # add 0 as achievable sum
                dp.add(n) # add current number as achievable sum
                continue
            for num in dp:
                if num+n==target: # base case: found a subset with required sum
                    return True
                if num+n not in dp: # only add if not already present
                    nextDP.add(num+n)
                nextDP.add(n) # also add the current number as a new achievable sum
            dp = nextDP # update dp to next state
        return False