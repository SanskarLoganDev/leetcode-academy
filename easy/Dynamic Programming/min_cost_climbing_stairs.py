# 746. Min Cost Climbing Stairs
# Neetcode 150 (Important)
# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

# You can either start from the step with index 0, or the step with index 1.

# Return the minimum cost to reach the top of the floor.

# Example 1:

# Input: cost = [10,15,20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.

# Example 2:

# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6
# Explanation: You will start at index 0.
# - Pay 1 and climb two steps to reach index 2.
# - Pay 1 and climb two steps to reach index 4.
# - Pay 1 and climb two steps to reach index 6.
# - Pay 1 and climb one step to reach index 7.
# - Pay 1 and climb two steps to reach index 9.
# - Pay 1 and climb one step to reach the top.
# The total cost is 6.
 

# Constraints:

# 2 <= cost.length <= 1000
# 0 <= cost[i] <= 999

from typing import List

# Recursion Brute Force
# time complexity O(2^N) and space complexity O(N) for recursion stack
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        def solve(i): # i is the current step
            if i>=n: # when we reach or cross the top
                return 0 # we return 0 as no more cost is needed
            a = cost[i] + solve(i+1) # taking 1 step
            b = cost[i] + solve(i+2) # taking 2 steps
            return min(a, b)

        return min(solve(0), solve(1))

# Input: cost = [10, 15, 20]
# n = 3
# solve(i) = minimum cost to reach (or pass) the top starting from step i, paying cost[i] when you step on i.

# Base case: if i >= 3, return 0 (already at/above top).

# You return: min(solve(0), solve(1)) because you can start at step 0 or step 1.

# Step-by-step calls
# Compute solve(0)

# solve(0):

# a = cost[0] + solve(1) = 10 + solve(1)

# b = cost[0] + solve(2) = 10 + solve(2)

# return min(a, b)

# So we must compute solve(1) and solve(2).

# Compute solve(1)

# solve(1):

# a = cost[1] + solve(2) = 15 + solve(2)

# b = cost[1] + solve(3) = 15 + solve(3)

# return min(a, b)

# So we must compute solve(2) and solve(3).

# Compute solve(2)

# solve(2):

# a = cost[2] + solve(3) = 20 + solve(3)

# b = cost[2] + solve(4) = 20 + solve(4)

# return min(a, b)

# Compute base cases:

# solve(3): i=3 >= n, return 0

# solve(4): i=4 >= n, return 0

# So:

# a = 20 + 0 = 20

# b = 20 + 0 = 20

# solve(2) = min(20, 20) = 20

# Back to solve(1)

# We already have solve(2)=20. Also:

# solve(3)=0

# So:

# a = 15 + solve(2) = 15 + 20 = 35

# b = 15 + solve(3) = 15 + 0 = 15

# solve(1) = min(35, 15) = 15

# Back to solve(0)

# We have:

# solve(1)=15

# solve(2)=20

# So:

# a = 10 + 15 = 25

# b = 10 + 20 = 30

# solve(0) = min(25, 30) = 25

# Final return

# min(solve(0), solve(1)) = min(25, 15) = 15

# Output: 15
# Meaning: start at step 1 (pay 15), then jump to the top.


# Using recursion with memoization

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}
        def solve(i):
            if i>=n: # when we reach or cross the top
                return 0 # we return 0 as no more cost is needed
            if i in memo: # check if already computed
                return memo[i]
            a = cost[i] + solve(i+1) # taking 1 step
            b = cost[i] + solve(i+2) # taking 2 steps
            memo[i] = min(a,b) # store in memo
            return min(a, b)

        return min(solve(0), solve(1))

# tabulation bottom up approach with optimized space
# time complexity O(N) and space complexity O(1)
# here we have modified the input cost array to store the minimum cost to reach each step
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n==2:
            return min(cost[0], cost[1])

        for i in range(2, n):
            cost[i] = cost[i] + min(cost[i-1], cost[i-2])

        return 0 + min(cost[n-1], cost[n-2])

# What the last return statement means
# return 0 + min(cost[n-1], cost[n-2])

# After the for loop, you have overwritten cost[i] to mean:

# cost[i] = minimum total cost to land on step i (and pay for it), starting from step 0 or 1.

# Now, the “top” is one step beyond the last index (beyond step n-1). To reach the top, your final move can be:

# from step n-1 to the top (a 1-step move), or

# from step n-2 to the top (a 2-step move)

# You do not pay any cost for the “top” itself, so the final cost is just the minimum of the cost to reach n-1 or n-2.

# So:

# min(cost[n-1], cost[n-2]) is the answer.

# 0 + is redundant; it changes nothing.

# Dry run for cost = [1,100,1,1,1,100,1,1,100,1]

# Initial:

# n = 10

# cost indices: 0..9

# We iterate i from 2 to 9 and update:

# cost[i] = cost[i] + min(cost[i-1], cost[i-2])


# I’ll show each step clearly.

# Start

# cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]

# i = 2

# cost[2] = 1 + min(cost[1]=100, cost[0]=1)

# = 1 + 1 = 2
# cost = [1, 100, 2, 1, 1, 100, 1, 1, 100, 1]

# i = 3

# cost[3] = 1 + min(cost[2]=2, cost[1]=100)

# = 1 + 2 = 3
# cost = [1, 100, 2, 3, 1, 100, 1, 1, 100, 1]

# i = 4

# cost[4] = 1 + min(cost[3]=3, cost[2]=2)

# = 1 + 2 = 3
# cost = [1, 100, 2, 3, 3, 100, 1, 1, 100, 1]

# i = 5

# cost[5] = 100 + min(cost[4]=3, cost[3]=3)

# = 100 + 3 = 103
# cost = [1, 100, 2, 3, 3, 103, 1, 1, 100, 1]

# i = 6

# cost[6] = 1 + min(cost[5]=103, cost[4]=3)

# = 1 + 3 = 4
# cost = [1, 100, 2, 3, 3, 103, 4, 1, 100, 1]

# i = 7

# cost[7] = 1 + min(cost[6]=4, cost[5]=103)

# = 1 + 4 = 5
# cost = [1, 100, 2, 3, 3, 103, 4, 5, 100, 1]

# i = 8

# cost[8] = 100 + min(cost[7]=5, cost[6]=4)

# = 100 + 4 = 104
# cost = [1, 100, 2, 3, 3, 103, 4, 5, 104, 1]

# i = 9

# cost[9] = 1 + min(cost[8]=104, cost[7]=5)

# = 1 + 5 = 6
# cost = [1, 100, 2, 3, 3, 103, 4, 5, 104, 6]

# Final step (return)
# return min(cost[9], cost[8]) = min(6, 104) = 6


# Answer = 6

# Interpretation (one optimal path)

# Start at step 0, then step on:
# 0 → 2 → 4 → 6 → 7 → 9 → top
# Costs paid: 1 + 1 + 1 + 1 + 1 + 1 = 6


# tabulation bottom up approach
# time complexity O(N) and space complexity O(N)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dp = [0]*n
        dp[0]=cost[0]
        dp[1]=cost[1]
        for i in range(2,n):
            dp[i] = cost[i]+min(dp[i-1], dp[i-2])
        return min(dp[n-1],dp[n-2])

# Wrong approach using greedy
# Your current approach uses a greedy strategy to decide at each step whether to take one or two steps based on which option has a lower cost immediately ahead. However, this approach can miss the overall minimum cost path because it doesn't consider the cumulative cost from the current step to the end of the array. 

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #cost = [0]+cost+[0]
        n=len(cost)
        def helper(index):
            i = index
            cost0 = 0
            while i<n:
                if i==n-2 or i==n-1:
                    cost0+=cost[i]
                    break
                if cost[i+1]>=cost[i+2]:
                    cost0+=cost[i]
                    i+=2
                else:
                    cost0+=cost[i]
                    i+=1

            return cost0
        print(helper(0),helper(1))
        return min(helper(0),helper(1))


# Example Execution using DP:
# For cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1], let's go through the execution:

# Initialize dp as [0, 0, 0, 0, 0, 0, 0, 0, 0, 0].

# Set dp[0] = 1 and dp[1] = 100.

# Calculate dp[i] for each i from 2 to 9 using the formula dp[i] = cost[i] + min(dp[i-1], dp[i-2]).

# For dp[2]: dp[2] = 1 + min(dp[1], dp[0]) = 1 + min(100, 1) = 2

# Continue this calculation up to dp[9].

# Finally, return min(dp[9], dp[8]) = min(6, 7) = 6.

# Time Complexity:
# Time Complexity: O(n)

# Computing each dp[i] takes constant time, and you do this for each of the n steps in the staircase.

# Space Complexity: O(n)

# Additional space is used to store the dp array of size n.