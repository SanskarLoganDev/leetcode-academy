# 560. Subarray Sum Equals K
# Neetcode 250

# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107

from typing import List

# Time complexity: O(N^3)
# Space complexity: O(N)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                subarr = nums[i:j]
                if sum(subarr) == k:
                    count+=1
        return count

# Optimised approach
# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cf_sum = {0:1} # cumulative sum {cf : occurences of that sum} as a sum can occur more than once, we initalise it this way to have the initial cumulative sum of 0 useful for the edge case of [-1, 1]
        count = 0
        csum = 0
        for i in range(len(nums)):
            csum+=nums[i]
            if csum-k in cf_sum: # here we check csum - k as it would take k for csum to reach this point, meaning the array in between would sum up to k
                count+=cf_sum.get(csum-k)
            cf_sum[csum] = cf_sum.get(csum, 0) + 1
        return count