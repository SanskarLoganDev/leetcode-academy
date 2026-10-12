# 33. Search in Rotated Sorted Array (Neetcode 150) Important

# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:

# Input: nums = [1], target = 0
# Output: -1

# Constraints:

# 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -104 <= target <= 104

from typing import List

# time complexity: O(log n), space complexity: O(1)

class Solution:
    def findMin(self, nums: List[int]): # this function finds the index of the minimum element in a rotated sorted array (leetcode 153)
        l = 0
        r = len(nums)-1
        while l<r:
            mid = (l+r)//2
            if nums[mid]>nums[r]:
                l = mid+1
            else:
                r = mid
        return r

    def bs(self, start: int, end: int, nums: List[int], target: int): # binary search: leetcode 704
        while start<=end:
            mid=(start+end)//2
            if target<nums[mid]:
                end = mid-1
            elif target>nums[mid]:
                start = mid+1
            else:
                return mid
        return -1

    # divide the array into 2 sorted parts by the pivot and search in both parts
    def search(self, nums: List[int], target: int) -> int:
        
        min_idx = self.findMin(nums)
        idx = self.bs(0, min_idx-1, nums, target)

        if idx!=-1:
            return idx
        idx = self.bs(min_idx, len(nums)-1, nums, target)

        return idx