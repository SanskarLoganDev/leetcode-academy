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

def climbStairs(n):
        """
        :type n: int
        :rtype: int
        """
        if n==0 or n==1:
            return 1
        return climbStairs(n-1)+climbStairs(n-2)
    
print(climbStairs(38))

# If funciton is in a class, use it with self in recursion as shown below

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0 or n==1:
            return 1
        return self.climbStairs(n-1)+self.climbStairs(n-2)
    
# Both the above solutions take a lot of time to complete, for example climbStairs(38) would itself take a lot of time
# Therefore to solve this problem we have to use DP (Dynamic Programming)
