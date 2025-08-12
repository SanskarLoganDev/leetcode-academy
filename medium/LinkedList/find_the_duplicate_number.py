# 287. Find the Duplicate Number

# Neetcode 150 (Important)

# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and using only constant extra space. 

# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: nums = [3,1,3,4,2]
# Output: 3
# Example 3:

# Input: nums = [3,3,3,3,3]
# Output: 3
 
# Constraints:

# 1 <= n <= 105
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer which appears two or more times.
 
# Follow up:

# How can we prove that at least one duplicate number must exist in nums?
# Can you solve the problem in linear runtime complexity?

# Most efficient solution: Floyd's Tortoise and Hare (Cycle Detection)

from typing import List

# time complexity: O(n)
# space complexity: O(1)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break

        slow2 = nums[0]
        while True:
            if slow == slow2:
                return slow
            slow = nums[slow]
            slow2 = nums[slow2]
            
# Brute force
# Time complexity: O(n^2)
# Space complexity: O(1)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]==nums[j]:
                    return nums[i]    
                
# Using set
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        set1 = set()
        for n in nums:
            if n in set1:
                return n
            set1.add(n)

        