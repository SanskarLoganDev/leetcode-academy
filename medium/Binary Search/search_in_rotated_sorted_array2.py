# 81. Search in Rotated Sorted Array II
# Neetcode 250

# There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

# Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

# Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

# You must decrease the overall operation steps as much as possible.

# Example 1:

# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true

# Example 2:

# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
 

# Constraints:

# 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# nums is guaranteed to be rotated at some pivot.
# -104 <= target <= 104

# CORRECT APPROACH
# time complexity: O(N)
# space complexity: O(1)

class Solution:
    def binarySearch(self, nums, l, r, target):
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return True
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return False
        
    def findMin(self, nums): # O(N), here since there are repeated elements, the previous O(logn) approach will not work as 
        # finding the minimum value is not the same as finding the rotation boundary
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                return i

        return 0

    def search(self, nums: list[int], target: int) -> bool:
        idx = self.findMin(nums)
        f1 = self.binarySearch(nums, 0, idx-1, target)
        if f1:
            return f1
        f2 = self.binarySearch(nums, idx, len(nums)-1, target)
        return f2
    
    
    
# THE FOLLOWING CODE (CodeStoryWithMIK) IS WRONG (REASON EXPLAINED BELOW IT)
class Solution:
    def binarySearch(self, nums, l, r, target):
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return True
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return False
        
    def findMin(self, nums):
        l = 0
        r = len(nums)-1
        while l<r:
            while l<r and nums[l] == nums[l+1]: # to avoid duplicates from the left
                l+=1
            while l<r and nums[r] == nums[r-1]: # to avoid duplicates from the right
                r-=1
            mid = (l+r)//2
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid
        return r

    def search(self, nums: list[int], target: int) -> bool:
        idx = self.findMin(nums)
        f1 = self.binarySearch(nums, 0, idx-1, target)
        if f1:
            return f1
        f2 = self.binarySearch(nums, idx, len(nums)-1, target)
        return f2

# Why this approach fails:
#
# Example: nums = [1,2,2,3,0,0,0,1], target = 3
#
# Actual rotation pivot = index 4
# Correct split: [1,2,2,3] | [0,0,0,1]
#
# Dry run of findMin():
# 1. Initially l=0, r=7, mid=3.
#    nums[mid]=3 > nums[r]=1, so l=4.
#
# 2. Now l=4, r=7.
#    The left duplicate-removal loop skips repeated zeros:
#    nums[4]==nums[5] -> l=5
#    nums[5]==nums[6] -> l=6
#
# 3. Now l=6, r=7, mid=6.
#    nums[mid]=0 < nums[r]=1, so r=6.
#    The loop ends and findMin() returns 6 instead of 4.
#
# 4. Binary search now operates on:
#    [1,2,2,3,0,0] | [0,1]
#    The first half is NOT sorted, so binary search can miss target=3.
#
# Root cause:
# We need the actual ROTATION PIVOT, not just any minimum-value index.
# Indices 4, 5, and 6 all contain 0, but only index 4 is the pivot.
# Skipping duplicates from the left can skip the actual pivot.