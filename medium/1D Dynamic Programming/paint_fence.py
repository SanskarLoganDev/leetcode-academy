# 276. Paint Fence

# You are painting a fence of n posts with k different colors. You must paint the posts following these rules:

# Every post must be painted exactly one color.
# There cannot be three or more consecutive posts with the same color.
# Given the two integers n and k, return the number of ways you can paint the fence.

 

# Example 1:


# Input: n = 3, k = 2
# Output: 6
# Explanation: All the possibilities are shown.
# Note that painting all the posts red or all the posts green is invalid because there cannot be three posts in a row with the same color.

# Example 2:

# Input: n = 1, k = 1
# Output: 1
# Example 3:

# Input: n = 7, k = 2
# Output: 42
 
# Constraints:

# 1 <= n <= 50
# 1 <= k <= 105
# The testcases are generated such that the answer is in the range [0, 231 - 1] for the given n and k.


# Logic
# The first post has k possibilities because there's nothing before it to conflict with, so every color is a free, independent choice; 
# the second post also has k free choices regardless of what the first was, giving k*k, because two posts in a row can never violate the 
# "no three consecutive same color" rule no matter what you pick. 
# We stop treating things as "fresh" after post 2 because starting from the 3rd post, every new post is constrained by what came before it — 
# it can either repeat the color of the post directly before it (only valid if that previous pair itself ended in two different colors, 
# which is exactly what dp[i-2] represents, since dp[i-2] counts sequences valid up to i-2, and appending one "different" post then one "same" post keeps it legal), 
# or it can pick any of the k-1 colors different from the post directly before it (valid from any legal arrangement of the first i-1 posts, since a differing color never creates three-in-a-row). 
# That's why the recurrence adds dp[i-1] + dp[i-2] (the two ways to legally extend a shorter valid sequence) and multiplies by (k-1) — because both extension paths ultimately require picking a genuinely 
# different color for the newest post, just anchored at a different "how far back do I look" point.


# Gynamic programming: Bottom up/Tabulation
# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n==1:
            return k
        if n==2:
            return k*k
        dp = [0]*(n+1)
        dp[1] = k
        dp[2] = k*k
        
        for i in range(3, n+1):
            dp[i] = (dp[i-1] + dp[i-2])*(k-1)
        return dp[n] 

# time complexity: O(N)
# space complexity: O(1)

class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n==1:
            return k
        if n==2:
            return k*k

        prev2 = k
        prev1 = k*k
        
        for i in range(3, n+1):
            val = (prev2+prev1)*(k-1)
            prev2 = prev1
            prev1 = val
        return prev1

# Recursion
# Time complexity: O(2^n)
# space: O(N)
class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n==0:
            return 0
        if n==1:
            return k
        if n==2:
            return k*k

        return (self.numWays(n-1, k)+self.numWays(n-2, k))*(k-1)
    
    
# Recusion + Memoization
# Time complexity: O(N)
# space: O(N)

class Solution:
    def numWays(self, n: int, k: int) -> int:
        memo = {}
        def solve(num):
            key = num
            if num==0:
                memo[0] = 0
                return 0
            if num==1:
                memo[1] = k
                return k
            if num==2:
                memo[2] = k*k 
                return k*k
            if key in memo:
                return memo[key]
            
            memo[key] = (solve(num-1)+solve(num-2))*(k-1)

            return memo[key]
        
        return solve(n)
