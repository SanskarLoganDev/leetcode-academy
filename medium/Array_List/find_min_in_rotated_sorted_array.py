# 153. Find Minimum in Rotated Sorted Array (Neecode 150) Important

# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
# Example 2:

# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
# Example 3:

# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 

# Constraints:

# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# All the integers of nums are unique.
# nums is sorted and rotated between 1 and n times.

# Both the solutions below have time complexity of O(log n) and space complexity of O(1).

# Neetcode solution:
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        res = nums[l]
        while l<=r:
            if nums[r]>nums[l]: # remaining array is sorted
                res = min(res, nums[l])
                break
            mid = (l+r)//2
            res = min(res, nums[mid])
            if nums[mid]>=nums[l]: # means we are in the left sorted portion
                l = mid+1
            else: # in right sorted portion
                r = mid-1
        return res

# CodeStoryWithMIK solution:

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l<r: # here we use < instead of <= to avoid infinite loop as we are doing r = mid in the else condition
            mid = (l+r)//2
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r = mid # here we do not do mid-1 because we want to include mid in the next iteration as mid could be the minimum element
        return nums[r]