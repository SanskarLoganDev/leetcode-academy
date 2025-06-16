# 2016. Maximum Difference Between Increasing Elements

# Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].

# Return the maximum difference. If no such i and j exists, return -1.

# Example 1:

# Input: nums = [7,1,5,4]
# Output: 4
# Explanation:
# The maximum difference occurs with i = 1 and j = 2, nums[j] - nums[i] = 5 - 1 = 4.
# Note that with i = 1 and j = 0, the difference nums[j] - nums[i] = 7 - 1 = 6, but i > j, so it is not valid.
# Example 2:

# Input: nums = [9,4,3,2]
# Output: -1
# Explanation:
# There is no i and j such that i < j and nums[i] < nums[j].
# Example 3:

# Input: nums = [1,5,2,10]
# Output: 9
# Explanation:
# The maximum difference occurs with i = 0 and j = 3, nums[j] - nums[i] = 10 - 1 = 9.

# Constraints:

# n == nums.length
# 2 <= n <= 1000
# 1 <= nums[i] <= 109

# time complexity: O(n), space complexity: O(1)
from typing import List
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff = -1
        min_pre = nums[0]
        i,j=0,1
        while i<len(nums) and j<len(nums):
            if nums[i]<nums[j]:
                min_pre = min(min_pre, nums[i]) # keep track of the minimum value before j
                max_diff = max(max_diff, nums[j]-min_pre) # maximum difference tracking
            i+=1
            j+=1
        return max_diff