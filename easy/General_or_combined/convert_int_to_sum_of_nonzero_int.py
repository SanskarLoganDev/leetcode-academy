# 1317. Convert Integer to the Sum of Two No-Zero Integers

# No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.

# Given an integer n, return a list of two integers [a, b] where:

# a and b are No-Zero integers.
# a + b = n
# The test cases are generated so that there is at least one valid solution. If there are many valid solutions, you can return any of them.

# Example 1:

# Input: n = 2
# Output: [1,1]
# Explanation: Let a = 1 and b = 1.
# Both a and b are no-zero integers, and a + b = 2 = n.
# Example 2:

# Input: n = 11
# Output: [2,9]
# Explanation: Let a = 2 and b = 9.
# Both a and b are no-zero integers, and a + b = 11 = n.
# Note that there are other valid answers as [8, 3] that can be accepted.
 
# Constraints:

# 2 <= n <= 104

# Let n be the input number and let d = number of decimal digits of n (d = ⌊log₁₀ n⌋ + 1)
# Each iteration:
# Converts a and b to strings → costs O(d) characters total (each ≤ d digits).

# Checks if '0' appears in each string → scans those strings → another O(d).
# Overall per-iteration cost = O(d).

# Time complexity (worst case)
# Iterations × work per iteration = O(n) · O(d) = O(n · log n).

from typing import List
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        a = 1
        b = n-1
        while '0' in str(a) or '0' in str(b):
            a+=1
            b-=1
        return [a,b]

# time complexity: O(logN)
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        a = n
        b = 0
        place_value = 1
        while n>1: # here we do n>1 because if n=1 then we have to take 2 digits in a and b to avoid 0
            take = 1
            if n%10==1:
                take = 2
            a = a - take*place_value
            b = b + take*place_value
            n = (n-take)//10 # here we do (n-take) because if n%10==1 and we do n//10 then in next iteration we will get 0 again
            place_value*=10
        return [a,b]
