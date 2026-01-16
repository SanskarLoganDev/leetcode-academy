# 70. Climbing Stairs
# Neetcode 150 (Important)
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

# Using Brute force Recursion
# time complexity O(2^N) and space complexity O(N) for recursion stack
class Solution:
    def climbStairs(self, n: int) -> int:
        def solve(n):
            if n<0: # when the steps go below 0 that means we have corssed the top
                return 0

            if n==0: # when there are no steps left to climb that means we are at the top and this counts as a successful way
                return 1

            ways = solve(n-1) + solve(n-2) # taking 1 step or 2 steps
            return ways # return total ways to reach the top
        return solve(n)

# Using Bottom‑Up Tabulation
# time complexity O(N) and space complexity O(N) for dp array
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        if n<0: # if less than 0 steps, 0 ways (no need to put it as it is out of constriants)
            return 0
        if n<=2: # if n is 0, 1 or 2, return n
            return n
        dp[0]=0 # 0 steps means 0 ways
        dp[1]=1 # 1 step means 1 way
        dp[2]=2 # 2 steps means 2 ways (2 '1' steps, or 1 '2' step)
        for i in range(3, n+1): # here we start with 3 as 0,1,2 are already handled
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n] 

# Using Bottom‑Up Tabulation optimized space, we are able to do this as the current state only depends on last two states
# time complexity O(N) and space complexity O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<0:
            return 0
        if n<=2:
            return n
        a = 1
        b = 2
        for i in range(3, n+1):
            c = a+b
            a=b
            b=c
        return b         
    
# Top‑Down with Memoization
# time complexity O(N) and space complexity O(N) for recursion stack and memo dictionary
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {} # dictionary to store the results of subproblems
        def ways(n):
            if n<0:
                return 0 # when the steps go below 0 that means we have corssed the top

            if n==0: # when there are no steps left to climb that means we are at the top and this counts as a successful way
                return 1

            if n in memo: # check if result is already computed
                return memo[n]
            # here n-1 means we have taken 1 step and remaning steps are n-1
            memo[n] = ways(n-1) + ways(n-2) # taking 1 step or 2 steps
            return memo[n]
        return ways(n)