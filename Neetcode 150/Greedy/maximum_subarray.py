# 53. Maximum Subarray
# Neetcode 150 (Important)

# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.

# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
 

# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

from typing import List

# time complexity O(N^2) where N is the length of nums, space complexity O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        for i in range(len(nums)):
            cur_sum = 0
            for j in range(i, len(nums)):
                cur_sum+=nums[j]
                max_sum = max(max_sum, cur_sum)
        return max_sum
        
# time complexity O(N) where N is the length of nums, space complexity O(1)        
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        cur_sum = 0
        for n in nums:
            # here we reset the cur_sum to 0 because if cur_sum is negative then it will only decrease the sum of the next subarray, so we start fresh from the next element.
            if cur_sum<0: 
                cur_sum = 0
            cur_sum+=n
            max_sum = max(cur_sum, max_sum)
        return max_sum
        
# we do (if cur_sum<0: cur_sum = 0) this before adding n to cur_sum because it breaks completely on all-negative arrays and empty subarray is not allowed
# Example: nums = [-5, -1, -8]

# Correct answer: -1
# Buggy dry run:

# n=-5: cur_sum=-5 -> reset 0 -> max_sum=0

# n=-1: cur_sum=-1 -> reset 0 -> max_sum=0

# n=-8: cur_sum=-8 -> reset 0 -> max_sum=0
# Returns 0 ❌ (should be -1)