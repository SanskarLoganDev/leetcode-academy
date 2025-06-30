# 217. CONTAINS DUPLICATE (Neetcode 150)

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:

# Input: nums = [1,2,3,1]

# Output: true

# Explanation:

# The element 1 occurs at the indices 0 and 3.

# Example 2:

# Input: nums = [1,2,3,4]

# Output: false

# Explanation:

# All elements are distinct.

# This method is correct but gives time exceeded error for a really long test case

# Time Complexity: O(n^2) and Space Complexity: O(n)
def containsDuplicate(nums):
    dup = []
    for i in range(len(nums)):
        if nums[i] in dup:
            return True
        dup.append(nums[i])
    return False

print(containsDuplicate([1,2,3,4]))

# Method 2
# time complexity: O(n log n) and space complexity: O(1) if we ignore the input size
def containsDuplicate2(nums):
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i]==nums[i+1]:
            return True
    return False

print(containsDuplicate2([1,2,3,4]))

# Using set
# time complexity: O(n) and space complexity: O(n)
def containsDuplicate3(nums):
    s1 = set(nums)
    if len(s1)!=len(nums):
        return True
    return False

print(containsDuplicate3([1,2,3,4]))

# Neetcode method
# time complexity: O(n) and space complexity: O(n)
def containsDuplicate4(nums):
    num_set = set()
    for num in nums:
        if num in num_set:
            return True
        num_set.add(num)
    return False

# My revision menthod
# time complexity: O(n) and space complexity: O(n)
from collections import Counter
from typing import List
class Solution:
    def hasDuplicate5(self, nums: List[int]) -> bool:
        count = Counter(nums)
        for key in count:
            if count[key]>1:
                return True
        return False