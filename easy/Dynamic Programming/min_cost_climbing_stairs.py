# 746. Min Cost Climbing Stairs

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


# Using DP, time complexity: O(N)

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