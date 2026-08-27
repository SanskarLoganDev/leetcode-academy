# 169. Majority Element
# Neetcode 250

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:

# Input: nums = [3,2,3]
# Output: 3

# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 

# Constraints:

# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109
# The input is generated such that a majority element will exist in the array.
 

# Follow-up: Could you solve the problem in linear time and in O(1) space?

# here ⌊n / 2⌋ means floor, so 2.5 becomes 2

# Brute force
# time complexity: O(nlogn)
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort() # nlogn, simply sort and the number in the middle will be the majority element
        n = len(nums)
        return nums[n//2]
    
    
# optimised solution, time complexity O(N)
# Boyer-Moore majority vote algorithm
# It is guaranteed that the solution exists so we can skip the verification step in the Boyer-Moore algo

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 0
        # change the candidate as the count reaches 0, the one with majority elements will be the last standing candidate
        for n in nums:
            if count == 0:
                candidate = n
            if n == candidate:
                count+=1
            else:
                count-=1
        return candidate
    
#### OR ####

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 0

        for n in nums:
            if count == 0:
                candidate = n
                count = 1 # here we reset it to 1, in the above code resetting is not needed as it is already handled in the next if statement
            elif n == candidate:
                count+=1
            else:
                count-=1
        return candidate