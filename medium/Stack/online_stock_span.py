# 901. Online Stock Span
# Neetcode 250

# Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

# The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day.

# For example, if the prices of the stock in the last four days are [7,2,1,2] and the price of the stock today is 2, then the span of today is 3 because starting from today, the price of the stock was less than or equal to 2 for 3 consecutive days.
# Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of the stock today is 8, then the span of today is 3 because starting from today, the price of the stock was less than or equal 8 for 3 consecutive days.
# Implement the StockSpanner class:

# StockSpanner() Initializes the object of the class.
# int next(int price) Returns the span of the stock's price given that today's price is price.
 
# Example 1:

# Input
# ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
# [[], [100], [80], [60], [70], [60], [75], [85]]
# Output
# [null, 1, 1, 1, 2, 1, 4, 6]

# Explanation
# StockSpanner stockSpanner = new StockSpanner();
# stockSpanner.next(100); // return 1
# stockSpanner.next(80);  // return 1
# stockSpanner.next(60);  // return 1
# stockSpanner.next(70);  // return 2
# stockSpanner.next(60);  // return 1
# stockSpanner.next(75);  // return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
# stockSpanner.next(85);  // return 6
 
# Constraints:

# 1 <= price <= 105
# At most 104 calls will be made to next.

class StockSpanner:

    def __init__(self): # space: O(N)
        self.stack = []

    def next(self, price: int) -> int: # O(N) each time next is called
        count = 1
        if self.stack:
            for i in range(len(self.stack)-1, -1, -1):
                if self.stack[i] > price:
                    break
                count+=1
        self.stack.append(price)
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)


# Optimised solution:

class StockSpanner:

    def __init__(self): # Space: O(N)
        self.stack = [] # store [price, span]

# Amortized O(1) means:
# A single call can sometimes cost more than O(1), but over a long sequence of calls, the average cost per call is O(1).

    def next(self, price: int) -> int: # Amortized O(1), Worst case: O(N)
        count = 1
        while self.stack and price >= self.stack[-1][0]:
            p, s = self.stack.pop()
            count+=s
        self.stack.append([price, count])
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

# Problem Hint: your current stack stores only the price:

# self.stack.append(price)

# That forces you to walk backward one day at a time.

# Instead, ask:

# Can each stack entry remember not just the price, but also how many consecutive days that price already represents?

# So store:

# (price, span)

# rather than just:

# price

# Example:

# 100 -> (100, 1)
# 80  -> (80, 1)
# 60  -> (60, 1)
# 70

# When 70 arrives, 60 <= 70, so you can pop (60,1) and add its span immediately:

# span = 1 + 1 = 2

# Then stop at 80 because:

# 80 > 70

# So push:

# (70, 2)

# Later for 75, instead of checking every previous day individually, you can reuse the spans already stored in popped entries.

# The pattern to think about is a monotonic decreasing stack