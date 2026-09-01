# 88) Merge Sorted Array
# Neetcode 250

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
# Example 2:

# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].
# Example 3:

# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

# my solu without using algorithm
# time complexity: O((n+m)log(n+m))
# space complexity: O(1)
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        for i in range(m, m+n):
            nums1[i] = nums2[j]
            j+=1
        nums1.sort()

# Slightly optimsed
# time complexity: O(n+m)
# space complexity: O(n+m)        
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        i = 0
        temp = []
        while i<m and j<n:
            if nums1[i]<nums2[j]:
                temp.append(nums1[i])
                i+=1
            else:
                temp.append(nums2[j])
                j+=1
        
        while i<m:
            temp.append(nums1[i])
            i+=1
        while j<n:
            temp.append(nums2[j])
            j+=1
        
        nums1[:] = temp # do not use nums1 = temp as it will just point to that list and not actually change it in place
        
# Pointing and Actually changing
# pointing to a new variable
# def test(nums1):
#     temp = [1,2,3]
#     nums1 = temp
#     print("inside:", nums1) # [1,2,3]

# a = [0,0,0]
# test(a)
# print("outside:", a) # [0,0,0]

# # actually changing in place
# def test(nums1):
#     temp = [1,2,3]
#     nums1[:] = temp # [1,2,3]

# a = [0,0,0]
# test(a)
# print(a) # [1,2,3]

# Optimised Solution
# time complexity: O(N+M)
# space complexity: O(1)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1 # end pointer for nums1 actual end
        j = n-1 # end pointer for nums2
        last = m+n-1 # end pointer for nums1 (including 0s)
        while i>-1 and j>-1:
            if nums1[i]<nums2[j]:
                nums1[last] = nums2[j] # greater values will be at the end
                j-=1
            else:
                nums1[last] = nums1[i]
                i-=1
            last-=1

        # Edge case handling of the leftover elements in nums2 (last elements for the iteration since we start the loop from the end)
        # if j reaches -1 and the last element (smallest) is in nums1, its fine since we have to return nums1 anyways
        # but if i reaches -1, that means the last element (smallest) is left inside nums2 and was not inserted (could be more than 1 values)
        while j>-1:
            nums1[last] = nums2[j]
            j-=1
            last-=1
