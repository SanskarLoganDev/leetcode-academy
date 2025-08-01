# 121. Best Time to Buy and Sell Stock (Neetcode 150) Important
# Topics: Array, Dynamic Programming

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

# Brute force O(N)

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                val = prices[j]-prices[i]
                if val>max_profit:
                    max_profit = val
        return max_profit
        
# Optimised solution, time O(N), space O(1) using sliding window technique
# We can keep track of the minimum price seen so far and calculate the profit at each step
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float("inf")
        for i in range(len(prices)):
            if prices[i]<min_price:
                min_price = prices[i]
            elif prices[i]-min_price > max_profit:
                max_profit = prices[i]-min_price
        return max_profit 