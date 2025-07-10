# 4. Median of Two Sorted Arrays (Neetcode 150) Important

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

# Constraints:

# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106


from typing import List

# Time complexity: O((n+m)log(n+m)), space complexity: O(n+m)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1+nums2
        nums.sort()
        n = len(nums)
        if n%2==0:
            return (nums[(n//2)-1]+nums[n//2])/2
        else:
            return nums[n//2]
       
# Time complexity: O(n+m), space complexity: O(n+m)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i=j=0
        nums = []
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                nums.append(nums1[i])
                i+=1
            else:
                nums.append(nums2[j])
                j+=1
        if i<len(nums1):
            nums = nums+nums1[i:len(nums1)]
        if j<len(nums2):
            nums = nums+nums2[j:len(nums2)]
        n = len(nums)
        if n%2==0:
            return (nums[(n//2)-1]+nums[n//2])/2
        else:
            return nums[n//2]
        
# Time complexity: O(n+m), space complexity: O(1)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i=j=count=0
        n = len(nums1)
        m = len(nums2)
        idx1 = (n+m)//2
        idx2 = idx1 - 1
        e1 = e2 = 0
        while i<n and j<m:
            if nums1[i]<nums2[j]:
                if count == idx2:
                    e2 = nums1[i]
                if count == idx1:
                    e1 = nums1[i]
                i+=1
                count+=1
            else:
                if count == idx2:
                    e2 = nums2[j]
                if count == idx1:
                    e1 = nums2[j]
                j+=1
                count+=1
        while i<n:
            if count == idx2:
                e2 = nums1[i]
            if count == idx1:
                e1 = nums1[i]
            i+=1
            count+=1
        while j<m:
            if count == idx2:
                e2 = nums2[j]
            if count == idx1:
                e1 = nums2[j]
            j+=1
            count+=1
        if (n+m)%2==0:
            return (e1+e2)/2
        else:
            return e1
        
        