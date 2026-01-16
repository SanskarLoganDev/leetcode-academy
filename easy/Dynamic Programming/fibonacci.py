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

# Solution using Dynamic Programming: memoization (top down)
# time complexity O(N) and space complexity O(N) for recursion stack and dp array
class Solution:
    def fib(self, n: int) -> int:
        dp = [-1]*(n+1)
        def solve(n):
            if n==0 or n==1:
                return n
            if dp[n]!=-1:
                return dp[n] 
            dp[n] = solve(n-1)+solve(n-2) # memoization step where we store the result
            return dp[n] # return the result
        return solve(n)

# Solution using Dynamic Programming: tabulation (bottom up)
# time complexity O(N) and space complexity O(N) for dp array
class Solution:
    def fib(self, n: int) -> int:
        dp = [0]*(n+1) # dp array to store fibonacci values 
        if n<=1:
            return n

        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1]+dp[i-2] # filling the dp array in bottom up manner
        return dp[n]
        
# Solution using Dynamic Programming: tabulation (bottom up) optimized space
# time complexity O(N) and space complexity O(1)

class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n

        a = 0
        b = 1
        for _ in range(n-1): # we run loop n-1 times as we already have first two fibonacci numbers
            c = a+b # current fibonacci number
            a = b # update a to previous fibonacci number
            b = c # update b to current fibonacci number
        return b  # b now contains F(n), we return b as it has c     

# Using recursion time complexity O(2^N), space complexity O(N) for recursion stack
class Solution:
    def fib(self, n: int) -> int:
        if n==0 or n==1:
            return n
        return self.fib(n-1)+self.fib(n-2)
    
# time complexity O(N) and space complexity O(1)
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
        
        