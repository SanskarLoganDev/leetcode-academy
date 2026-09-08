# 209. Minimum Size Subarray Sum
# Neetcode 250

# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1

# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0

# Constraints:

# 1 <= target <= 109
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104

# Time complexity: O(N^2)
# Space complexity: O(1)
from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        n = len(nums)
        min_len = n+1
        for i in range(n):
            total = 0
            for j in range(i, n):
                total+=nums[j]
                if total >= target:
                    min_len = min(min_len, j-i+1)
        return min_len if min_len<n+1 else 0
                
# Time complexity: O(N)
# Space complexity: O(1)                
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # early exit handles all cases where sum of entire array is less than target
        if sum(nums) < target:
            return 0
        total = 0
        l = 0
        n = len(nums)
        min_len = n+1
        for i in range(n):
            total += nums[i]
            while total >= target: # while here to keep moving the left wall trying to minimize the length
                total = total - nums[l]
                min_len = min(min_len, i-l+1)
                l+=1
            
        return min_len             
                
                
