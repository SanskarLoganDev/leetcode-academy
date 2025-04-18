# 1752. Check if Array Is Sorted and Rotated

# Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

# There may be duplicates in the original array.

# Note: An array A rotated by x positions results in an array B of the same length such that B[i] == A[(i+x) % A.length] for every valid index i.

# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: true
# Explanation: [1,2,3,4,5] is the original sorted array.
# You can rotate the array by x = 3 positions to begin on the element of value 3: [3,4,5,1,2].
# Example 2:

# Input: nums = [2,1,3,4]
# Output: false
# Explanation: There is no sorted array once rotated that can make nums.
# Example 3:

# Input: nums = [1,2,3]
# Output: true
# Explanation: [1,2,3] is the original sorted array.
# You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.

from typing import List
#Time complexity O(N^2) [O(n log n) + O(n^2)]
class Solution:
    def check(self, nums: List[int]) -> bool:
        temp = sorted(nums) # O(n log n) time
        for _ in range(len(nums)):
            if nums==temp:
                return True
            rem = nums.pop()
            nums.insert(0,rem) # O(N)
        return False

