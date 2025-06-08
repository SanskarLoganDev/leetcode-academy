# 238. Product of Array Except Self

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 
# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 
# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

from typing import List

# time complexity O(n), space complexity O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        pre, post = 1, 1
        
        for n in nums:
            pre*=n
            prefix.append(pre)
        for n in nums[::-1]:
            post*=n
            postfix.append(post)
        postfix = postfix[::-1]
        output=[]
        for i in range(len(nums)):
            pre = i-1
            post = i+1
            if pre<0:
                output.append(1*postfix[post])
            elif post>=len(nums):
                output.append(1*prefix[pre])
            else:
                output.append(prefix[pre]*postfix[post])
        return output
