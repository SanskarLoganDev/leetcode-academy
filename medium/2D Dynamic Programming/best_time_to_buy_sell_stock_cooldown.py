# 309. Best Time to Buy and Sell Stock with Cooldown
# Neetcode 150 (Important)

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

# After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

# Example 1:

# Input: prices = [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]

# Example 2:

# Input: prices = [1]
# Output: 0
 

# Constraints:

# 1 <= prices.length <= 5000
# 0 <= prices[i] <= 1000

# Recursive solution
# Time complexity: O(2^n) because at each day we have two choices (buy/sell or not buy/not sell)
# Space complexity: O(n) for the recursion stack
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # there is choice in both buying and selling
        def solve(i, state):
            if i>=n:
                return 0
            if state == "buy":
                # Option 1: buy today -> pay prices[i], then move to "sell" and that is why we subtract prices[i] from the profit. Option 2: don't buy today -> move to the next day and stay in "buy" state
                buy = solve(i+1, "sell") - prices[i]
                # Option 2: skip today -> move to the next day and stay in "buy" state
                not_buy = solve(i+1, state)
                return max(buy, not_buy)

            elif state == "sell": # ready to sell
                # Option 1: sell today -> gain prices[i], then cooldown (i+2) and go back to "buy". Since money was added to the profit, we add prices[i] to the profit.
                sell = prices[i] + solve(i+2, "buy")
                # Option 2: hold (don't sell) -> stay in "sell"
                not_sell = solve(i+1, state)
                return max(sell, not_sell)

        return solve(0, "buy")
    
# Memoization solution
# Time complexity: O(n) because we are storing the results of subproblems in a memoization table and each subproblem is solved only once.
# Space complexity: O(n) for the recursion stack and O(n) for the memoization

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # there is choice in both buying and selling
        memo = {}
        def solve(i, state):
            if i>=n:
                return 0
            key = (i, state)
            if key in memo:
                return memo[key]
            if state == "buy":
                # Option 1: buy today -> pay prices[i], then move to "sell" and that is why we subtract prices[i] from the profit. Option 2: don't buy today -> move to the next day and stay in "buy" state
                buy = solve(i+1, "sell") - prices[i]
                # Option 2: skip today -> move to the next day and stay in "buy" state
                not_buy = solve(i+1, state)
                memo[key] = max(buy, not_buy)
                return memo[key]

            elif state == "sell": # ready to sell
                # Option 1: sell today -> gain prices[i], then cooldown (i+2) and go back to "buy". Since money was added to the profit, we add prices[i] to the profit.
                sell = prices[i] + solve(i+2, "buy")
                # Option 2: hold (don't sell) -> stay in "sell"
                not_sell = solve(i+1, state)
                memo[key] = max(sell, not_sell)
                return memo[key]

        return solve(0, "buy")
            
            
# Tabulation solution
# time complexity: O(n^2) because of the nested loops
# space complexity: O(n) for the dp array

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n==1:
            return 0
        dp = [0]*n
        dp[0] = 0 # on day 0, no profit can be made
        dp[1] = max(prices[1]-prices[0], 0) # on day 1, either we sell on day 1 or do nothing
        for i in range(2, n):
            dp[i] = dp[i-1] # we assign the previous day's profit first to determine if we will have max profit today or the past day's profit
            for j in range(0, i): # we try to sell on day i and buy on any day j before i
                if j>=2:
                    prev_profit = dp[j-2] # because j-1 is cooldown day
                else:
                    prev_profit = 0
                profit = prices[i] - prices[j] # profit if we buy on day j and sell on day i
                dp[i] = max(dp[i], profit + prev_profit) # update dp[i] if we get more profit by selling on day i
                
        return dp[n-1] # maximum profit on the last day
    
    
# Space optimized tabulation solution
# time complexity: O(n)
# space complexity: O(1)

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0

        # Bottom-up DP with 3 states (Cooldown problem):
        # hold: max profit at end of day i if we are holding a stock
        # sold: max profit at end of day i if we sold a stock today
        # rest: max profit at end of day i if we do not hold a stock and did not sell today
        hold = -prices[0]
        sold = 0
        rest = 0

        for i in range(1, n):
            price = prices[i]

            prev_hold = hold
            prev_sold = sold
            prev_rest = rest

            hold = max(prev_hold, prev_rest - price)  # buy or keep holding
            sold = prev_hold + price                  # sell today
            rest = max(prev_rest, prev_sold)          # rest or cooldown from yesterday's sell

        return max(sold, rest)

