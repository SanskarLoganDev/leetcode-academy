# 3411. Maximum Subarray With Equal Products

# You are given an array of positive integers nums.

# An array arr is called product equivalent if prod(arr) == lcm(arr) * gcd(arr), where:

# prod(arr) is the product of all elements of arr.
# gcd(arr) is the GCD of all elements of arr.
# lcm(arr) is the LCM of all elements of arr.
# Return the length of the longest product equivalent subarray of nums.

# Example 1:

# Input: nums = [1,2,1,2,1,1,1]

# Output: 5

# Explanation: 

# The longest product equivalent subarray is [1, 2, 1, 1, 1], where prod([1, 2, 1, 1, 1]) = 2, gcd([1, 2, 1, 1, 1]) = 1, and lcm([1, 2, 1, 1, 1]) = 2.

# Example 2:

# Input: nums = [2,3,4,5,6]

# Output: 3

# Explanation: 

# The longest product equivalent subarray is [3, 4, 5].

# Example 3:

# Input: nums = [1,2,3,1,4,5,1]

# Output: 5 

# Constraints:

# 2 <= nums.length <= 100
# 1 <= nums[i] <= 10

from typing import List
import math

# time complexity: O(N^2log(M))
# According to Euclidean alogrithm, both GCD and LCM take logM time. N = number of elements in nums. M = maximum element in nums.
# space complexity: O(1)

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        max_len = 0
        for i in range(len(nums)):
            prod = 1
            gcd = 0 # intialize as 0 as greatest common divisor for any postive integer and 0 is the integer itself. Ex: gcd(0, 4) = 4
            lcm = 1
            for j in range(i, len(nums)):
                prod = prod*nums[j]
                gcd = math.gcd(gcd, nums[j])
                lcm = math.lcm(lcm, nums[j])
                if prod == gcd*lcm:
                    max_len = max(max_len, j-i+1)
        return max_len