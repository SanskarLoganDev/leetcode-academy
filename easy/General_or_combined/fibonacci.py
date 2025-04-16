# 509. Fibonacci Number

# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

# Example 1:

# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
# Example 2:

# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
# Example 3:

# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 
# Constraints:

# 0 <= n <= 30

# Using recursion/Dynamic programming time complexity O(2^N)
class Solution:
    def fib(self, n: int) -> int:
        if n==0 or n==1:
            return n
        return self.fib(n-1)+self.fib(n-2)
    
# Using for loop:
class Solution:
    def fib(self, n: int) -> int:
        val1 = 0
        val2 = 1
        ans = 0
        if n==0 or n==1:
            return n
        for i in range(n-1):
            ans = val1+val2
            val1 = val2
            val2 = ans
        return ans
        
        