# 31. Next Permutation

# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

# For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
# The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
# Given an array of integers nums, find the next permutation of nums.

# The replacement must be in place and use only constant extra memory.

# Example 1:

# Input: nums = [1,2,3]
# Output: [1,3,2]

# Example 2:

# Input: nums = [3,2,1]
# Output: [1,2,3]
# Example 3:

# Input: nums = [1,1,5]
# Output: [1,5,1]
 

# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100

from typing import List
from itertools import permutations

# Time: O(n! × n) — generating all n! permutations takes O(n!) time, each of length n to build/compare; sorting them adds O(n! log(n!)) on top.
# Space: O(n! × n)
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # we do this as permutations always returns tuples, and we do not want type mismatch while comparing
        current = tuple(nums)  # tuple so we can compare/find it among the generated permutations

        # generate every permutation of the current arrangement's values, then sort lexicographically
        all_perms = sorted(set(permutations(nums)))  # set() to dedupe in case of repeated values like [1,1,5]

        # find where current sits in this sorted list
        idx = all_perms.index(current)

        # the next permutation is the one right after it; wrap around to the first (smallest) if current is last
        if idx == len(all_perms) - 1:
            next_perm = all_perms[0]
        else:
            next_perm = all_perms[idx + 1]

        # copy the result back into nums in-place
        for i in range(n):
            nums[i] = next_perm[i]
            
# Time optimised solution
# Time complexity: O(N)  
# Space complexity: O(N)          
from itertools import permutations
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        gola_index = -1
        # finding gola index: first candidate for swapping: a number less than the number on its right
        for i in range(n-1, 0, -1): # O(N)
            if nums[i-1] < nums[i]:
                gola_index = i-1   # for example nums = [1,5,3,2], gola index would be 0, nums[0] = 1
                break

        # 2nd swap index, we only need to swap if we actually find gola index
        if gola_index!=-1:
            swap_index = gola_index # swap index = number on the right of gola_index immediately
            for i in range(n-1, gola_index, -1): # O(N)
                if nums[gola_index] < nums[i]:
                    swap_index = i    # for example nums = [1,5,3,2], swap index would be 3, or nums[3] = 2
                    break

            # swap
            nums[gola_index], nums[swap_index] = nums[swap_index], nums[gola_index]

        nums[gola_index+1:] = nums[gola_index+1:][::-1] # Space: O(N), The current slicing creates a copy of the sublist.

# reducing space complexity to O(1)

from itertools import permutations
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rev(arr, start): # using two pointer to reverse in place
            l = start
            r = len(arr)-1
            while l<r:
                arr[l], arr[r] = arr[r], arr[l]
                l+=1
                r-=1
            return arr

        n = len(nums)
        gola_index = -1
        # finding gola index: first candidate for swapping
        for i in range(n-1, 0, -1):
            if nums[i-1] < nums[i]:
                gola_index = i-1
                break

        # 2nd swap index
        if gola_index!=-1:
            swap_index = gola_index
            for i in range(n-1, gola_index, -1):
                if nums[gola_index] < nums[i]:
                    swap_index = i
                    break

            # swap
            nums[gola_index], nums[swap_index] = nums[swap_index], nums[gola_index]

        rev(nums, gola_index+1) # space complexity: O(1)

        

        

        