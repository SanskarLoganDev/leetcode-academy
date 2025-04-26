# 1025. Divisor Game

# Alice and Bob take turns playing a game, with Alice starting first.

# Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:

# Choosing any x with 0 < x < n and n % x == 0.
# Replacing the number n on the chalkboard with n - x.
# Also, if a player cannot make a move, they lose the game.

# Return true if and only if Alice wins the game, assuming both players play optimally.

# Example 1:

# Input: n = 2
# Output: true
# Explanation: Alice chooses 1, and Bob has no more moves.
# Example 2:

# Input: n = 3
# Output: false
# Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.
 

# Constraints:

# 1 <= n <= 1000

# Technical solution using Dynamic Programming, time complexity O(N^2)
class Solution:
    def divisorGame(self, n: int) -> bool:
        # dp[i] will be True if the player whose turn it is at value i can force a win
        dp = [False] * (n + 1)
        dp[1] = False  # base case: at n=1 you have no moves, so you lose

        # compute from 2 up to n
        for i in range(2, n + 1):
            # try every proper divisor x of i
            for x in range(1, i):
                if i % x == 0 and not dp[i - x]:
                    dp[i] = True
                    break

        return dp[n]

# Logical Solution. time complexity O(1)

class Solution:
    def divisorGame(self, n: int) -> bool:
        return n%2==0

# DP Explanation
   
# Example 1: n = 8
# Initialization:

# dp[i] represents whether the player whose turn it is at value i can force a win.

# Initialize dp array: dp = [False, False, False, False, False, False, False, False, False] (index 0 to 8)

# Base case: dp[1] = False (since at n=1, the player has no moves and loses).

# DP Computation:

# Iterate from i = 2 to 8:

# For each i, iterate through all proper divisors x (1 to i-1).

# Check if i % x == 0 and if not dp[i - x] (meaning if by subtracting x, the opponent cannot force a win).

# Update dp[i] = True if such x is found.

# Detailed steps:

# i = 2: Divisors 1, dp[2] = True (Alice can force a win by choosing x = 1).

# i = 3: Divisors 1 but dp[x-i] = dp[3-1 = 2] = True, dp[3] = False.

# i = 4: Divisors 1, 2 and dp[x-i] = dp[3] (False) and dp[2] (True, at least one has to be true). dp[4] = True (Alice can force a win by choosing x = 1).

# i = 5: Divisors 1 but dp[x-i] = dp[5-1 = 4] = True, dp[5] = False.

# i = 6: Divisors 1, 2, 3. dp[6] = True (Alice can force a win by choosing x = 3).

# i = 7: Divisors 1 but dp[x-i] = dp[7-1 = 6] = True, dp[7] = False.

# i = 8: Divisors 1, 2, 4. dp[8] = True (Alice can force a win by choosing x = 1 or x = 4).

# Final dp array after computation: [False, False, True, False, True, True, False, True, True].

# return dp[8] will be True, indicating Alice can win when n = 8.

# Example 2: n = 9
# Initialization:

# Initialize dp array: dp = [False, False, False, False, False, False, False, False, False, False] (index 0 to 9)

# Base case: dp[1] = False (since at n=1, the player has no moves and loses).

# DP Computation:

# Iterate from i = 2 to 9:

# For each i, iterate through all proper divisors x (1 to i-1).

# Check if i % x == 0 and if not dp[i - x] (meaning if by subtracting x, the opponent cannot force a win).

# Update dp[i] = True if such x is found.

# Detailed steps:

# i = 2: No proper divisors, dp[2] = False.

# i = 3: No proper divisors, dp[3] = False.

# i = 4: Divisors 1, 2. dp[4] = True (Alice can force a win by choosing x = 1).

# i = 5: No proper divisors, dp[5] = False.

# i = 6: Divisors 1, 2, 3. dp[6] = True (Alice can force a win by choosing x = 3).

# i = 7: No proper divisors, dp[7] = False.

# i = 8: Divisors 1, 2, 4. dp[8] = True (Alice can force a win by choosing x = 1 or x = 4).

# i = 9: Divisors 1, 3. dp[9] = False (Bob can force a win regardless of Alice's move).

# Final dp array after computation: [False, False, True, False, True, True, False, True, True, False].

# return dp[9] will be False, indicating Alice cannot win when n = 9.

# Conclusion
# For n = 8, Alice can win (output True).

# For n = 9, Alice cannot win (output False).

# This dynamic programming solution effectively determines the winner based on optimal play by both players, iterating through all possible moves and checking if the current player can force a win given the current state n.