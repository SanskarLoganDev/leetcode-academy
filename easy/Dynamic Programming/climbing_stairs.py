# 70. Climbing Stairs

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# Constraints:

# 1 <= n <= 45

# Using Bottom‑Up Tabulation

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range(2,n+1):
            dp[i] = dp[i-2]+dp[i-1]
        return dp[-1]
    
# Top‑Down with Dict Cache

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def ways(i):
            if i<=1:
                return 1
            if i in memo:
                return memo[i]
            memo[i] = ways(i-2)+ways(i-1)
            return memo[i]
        return ways(n)