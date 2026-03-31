# 912. Sort an Array

# Given an array of integers nums, sort the array in ascending order and return it.

# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

# Example 1:

# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
# Example 2:

# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessarily unique.
 

# Constraints:

# 1 <= nums.length <= 5 * 104
# -5 * 104 <= nums[i] <= 5 * 104

from typing import List

# Heap sort
# time: O(nlogn), space: O(1)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def max_heapify(n, idx):
            largest = idx
            left = 2*idx+1
            right = 2*idx+2

            if left<n and nums[largest]<nums[left]:
                largest = left

            if right<n and nums[largest]<nums[right]:
                largest = right

            if largest!=idx:
                nums[idx], nums[largest] = nums[largest], nums[idx]
                max_heapify(n, largest)

        n = len(nums)
        for i in range(n//2-1, -1, -1):
            max_heapify(n, i)

        for i in range(n-1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            max_heapify(i, 0)

        return nums

# merge sort
# time complexity O(nlogn) and space complexity o(n)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        mid = len(nums)//2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        
        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = 0
        j = 0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        result.extend(left[i:])
        result.extend(right[j:])

        return result
    
    
# Optimising space here, we are not creating the result array again and again, space complexity is still O(N) as we are using left_arr and right_arr
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        mid = len(nums)//2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        
        i=0
        j=0
        k=0

        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                nums[k] = left[i]
                i+=1
            else:
                nums[k] = right[j]
                j+=1
            k+=1
        if i<len(left):
            while i<len(left):
                nums[k] = left[i]
                i+=1
                k+=1
        if j<len(right):
            while j<len(right):
                nums[k] = right[j]
                j+=1
                k+=1

        return nums