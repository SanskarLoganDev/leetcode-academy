# 69. Sqrt(x)
# Neetcode 250

# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

# Example 1:

# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.

# Example 2:

# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

# Time complexity: O(logx)
# space complexity: O(1)

class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        r = x
        while l<=r:
            mid = (l+r)//2
            if mid*mid == x:
                return mid
            elif mid*mid<x:
                l=mid+1
            else:
                r=mid-1
        return r
        