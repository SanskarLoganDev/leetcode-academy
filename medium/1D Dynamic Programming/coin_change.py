# 322. Coin Change
# Neetcode 150 (Important)

# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

# Example 1:
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

# Example 2:
# Input: coins = [2], amount = 3
# Output: -1

# Example 3:
# Input: coins = [1], amount = 0
# Output: 0
 

# Constraints:

# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104

# Recursive solution
# time complexity: O(Number of coins^amount) in worst case as for each amount we are trying all coins and space complexity O(amount) for recursion stack
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        coins.sort() # we sort because if coin is greater than amount we can break early
        def solve(amt):
            minn = float("inf")
            if amt == 0: # base case where amount is 0 and we need 0 coins
                return 0
            for coin in coins:
                diff = amt - coin # remaining amount after taking current coin
                if diff<0:
                    break
                minn = min(minn, 1+solve(diff)) # take minimum of current minimum and 1 + result of remaining amount
            return minn

        res = solve(amount)
        if res<float("inf"): # if res is updated
            return res
        else:
            return -1
        
# Using memoization to optimize the above solution
# time complexity O(N*M) where N is amount and M is number of coins as we are storing results for each amount and 
# space complexity O(N) for recursion stack + O(N) for memoization
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        memo = {} # here memo[amt] = minimum coins needed to make amount amt
        memo[0] = 0 # base case where amount is 0 and we need 0 coins
        coins.sort() # we sort because if coin is greater than amount we can break early
        def solve(amt):
            minn = float("inf")
            if amt in memo: # check if already computed
                return memo[amt]
            for coin in coins:
                diff = amt - coin # remaining amount after taking current coin
                if diff<0: # no need to check further as coins are sorted
                    break
                minn = min(minn, 1+solve(diff)) # take minimum of current minimum and 1 + result of remaining amount
            memo[amt] = minn # store in memo
            return minn

        res = solve(amount)
        if res<float("inf"):
            return res
        else:
            return -1
        
# Memoization solution using 2D DP (Knapsack approach)
# time complexity O(N*M) where N is amount and M is number of coins as we are storing results for each amount and coin index
# space complexity O(N*M) for memoization table and O(N) for recursion stack
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        memo = {}
        n = len(coins)
        def solve(i, amt): # here i is the index of coin we are currently considering and amt is the remaining amount we need to make
            if amt==0:
                return 0 # base case: for 0 amount we need 0 coins
            if amt<0 or i>=n:
                return float("inf")
            key = (i, amt)
            if key in memo:
                return memo[key]
            take = 1+solve(i, amt-coins[i]) # take current coin and stay on same coin index because we can use same coin multiple times, we do +1 because we are taking current coin
            skip = solve(i+1, amt) # skip current coin and move to next coin index
            memo[key] = min(take, skip)
            return memo[key]
        
        res = solve(0, amount)
        if res<float("inf"):
            return res
        else:
            return -1
        
# using bottom up dynamic programming (tabulation)
# time complexity O(N*M) where N is amount and M is number of coins as we are filling dp array of size amount
# space complexity O(N) for dp array
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        coins.sort()
        dp = [0]*(amount+1) # dp[i] = minimum coins needed to make amount i
        for i in range(1, amount+1):
            minn = float("inf")
            for coin in coins:
                diff = i - coin
                if diff<0:
                    break
                minn = min(minn, dp[diff]+1) # take minimum of current minimum and 1 + dp[diff], here we do +1 because we are taking current coin
            dp[i] = minn # store minimum coins needed to make amount i
        
        if dp[amount]<float("inf"):
            return dp[amount]
        else:
            return -1


# Dry run using memoization for coins = [1,2,5], amount = 11
# Call: solve(11)

# 11 not in memo.

# Try coins:

# coin = 1 → diff = 10

# Need 1 + solve(10) → compute solve(10).

# solve(10)

# 10 not in memo.

# coin=1 → diff=9 → need 1 + solve(9) → compute solve(9)
# solve(9)

# 9 not in memo.

# coin=1 → diff=8 → need 1 + solve(8) → compute solve(8)
# solve(8)

# 8 not in memo.

# coin=1 → diff=7 → need 1 + solve(7) → compute solve(7)
# solve(7)

# 7 not in memo.

# coin=1 → diff=6 → need 1 + solve(6) → compute solve(6)
# solve(6)

# 6 not in memo.

# coin=1 → diff=5 → need 1 + solve(5) → compute solve(5)
# solve(5)

# 5 not in memo.

# coin=1 → diff=4 → need 1 + solve(4) → compute solve(4)
# solve(4)

# 4 not in memo.

# coin=1 → diff=3 → need 1 + solve(3) → compute solve(3)
# solve(3)

# 3 not in memo.

# coin=1 → diff=2 → need 1 + solve(2) → compute solve(2)
# solve(2)

# 2 not in memo.

# coin=1 → diff=1 → need 1 + solve(1) → compute solve(1)
# solve(1)

# 1 not in memo.

# coin=1 → diff=0 → 1 + solve(0)

# solve(0) is in memo → 0

# candidate = 1 + 0 = 1

# coin=2 → diff=-1 break

# So:

# memo[1] = 1
# Return solve(1)=1

# Memo now: {0:0, 1:1}

# Back to solve(2)

# We were computing solve(2):

# coin=1: candidate = 1 + solve(1)=1+1=2

# coin=2: diff=0 → candidate = 1 + solve(0)=1

# coin=5: diff=-3 break

# Minimum is 1.

# So:

# memo[2] = 1
# Return solve(2)=1

# Memo: {0:0, 1:1, 2:1}

# Back to solve(3)

# coin=1: 1 + solve(2)=1+1=2

# coin=2: 1 + solve(1)=1+1=2 (memo hit)

# coin=5: break

# So:

# memo[3] = 2
# Return solve(3)=2

# Memo includes: 3:2

# Back to solve(4)

# coin=1: 1 + solve(3)=3

# coin=2: 1 + solve(2)=2

# coin=5: break

# So:

# memo[4] = 2
# Return solve(4)=2

# Back to solve(5)

# coin=1: 1 + solve(4)=3

# coin=2: 1 + solve(3)=3

# coin=5: 1 + solve(0)=1

# Minimum is 1.

# So:

# memo[5] = 1
# Return solve(5)=1

# Back to solve(6)

# coin=1: 1 + solve(5)=2

# coin=2: 1 + solve(4)=3

# coin=5: 1 + solve(1)=2

# Minimum is 2.

# So:

# memo[6] = 2
# Return solve(6)=2

# Back to solve(7)

# coin=1: 1 + solve(6)=3

# coin=2: 1 + solve(5)=2

# coin=5: 1 + solve(2)=2

# Minimum is 2.

# So:

# memo[7] = 2
# Return solve(7)=2

# Back to solve(8)

# coin=1: 1 + solve(7)=3

# coin=2: 1 + solve(6)=3

# coin=5: 1 + solve(3)=3

# So:

# memo[8] = 3
# Return solve(8)=3

# Back to solve(9)

# coin=1: 1 + solve(8)=4

# coin=2: 1 + solve(7)=3

# coin=5: 1 + solve(4)=3

# So:

# memo[9] = 3
# Return solve(9)=3

# Back to solve(10)

# coin=1: 1 + solve(9)=4

# coin=2: 1 + solve(8)=4

# coin=5: 1 + solve(5)=2

# So:

# memo[10] = 2
# Return solve(10)=2

# Back to solve(11)

# Now evaluate solve(11) with memo hits:

# coin=1: 1 + solve(10)=1+2=3

# coin=2: 1 + solve(9)=1+3=4

# coin=5: 1 + solve(6)=1+2=3

# Minimum is 3.

# So:

# memo[11] = 3
# Return solve(11)=3

# Final result

# res = 3, it’s finite ⇒ return 3

# ✅ Minimum coins for 11 using [1,2,5] is 3 (5 + 5 + 1)