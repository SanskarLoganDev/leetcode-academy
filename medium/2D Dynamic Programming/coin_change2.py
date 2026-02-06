# 518. Coin Change II
# Neetcode 150 (Important)

# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

# You may assume that you have an infinite number of each kind of coin.

# The answer is guaranteed to fit into a signed 32-bit integer.

# Example 1:

# Input: amount = 5, coins = [1,2,5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1

# Example 2:

# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.

# Example 3:

# Input: amount = 10, coins = [10]
# Output: 1
 

# Constraints:

# 1 <= coins.length <= 300
# 1 <= coins[i] <= 5000
# All the values of coins are unique.
# 0 <= amount <= 5000

from typing import List

# recursive solution
# Time complexity: O(2^n) because at each coin we have two choices (take or skip)
# Space complexity: O(n) for the recursion stack
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        def solve(i, amt):
            if amt==0:
                return 1
            if amt<0 or i>=n:
                return 0
            take = solve(i, amt-coins[i])
            skip = solve(i+1, amt)
            return take+skip
        return solve(0, amount)
    
# memoization solution
# Time complexity: O(n*amount) because we are storing the results of subproblems in a memoization table and each subproblem is solved only once.
# Space complexity: O(n*amount) for the memoization table and O(n) for the recursion stack
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        memo = {}
        def solve(i, amt):
            if amt==0: # if the amount is 0, we have found a valid combination, so we return 1 to count this combination
                return 1
            if amt<0 or i>=n: # if we have gone through all the coins or a combination exceeds the amount, we return 0 because that means we have not found a valid combination
                return 0
            key = (i, amt)
            if key in memo:
                return memo[key]
            # We do i+1 in skip because “take” means you’re allowed to use the same coin again, while “skip” means you’ve decided to never use that coin anymore, so you move on to the next coin type.
            take = solve(i, amt-coins[i])
            skip = solve(i+1, amt)
            memo[key] = take+skip
            return memo[key]
        return solve(0, amount)
    
    
# tabulation solution
# Time complexity: O(n*amount) because we have two nested loops, one iterating over the coins and the other iterating over the amounts up to the target amount.
# Space complexity: O(amount) because we are using a 1D array to store the number of combinations for each amount up to the target amount.

# Logic: We initialize a dp array of size amount + 1 with all values set to 0, except for dp[0] which is set to 1 because there is one way to make the amount of 0 (by using no coins). 
# We then iterate through each coin and for each coin, we iterate through the amounts from the coin's value up to the target amount. For each amount, we add the number of combinations that can be made with the current coin (which is dp[a - coin]) to the current number of combinations for that amount (dp[a]). Finally, we return dp[amount] which will contain the total number of combinations to make up the target amount.
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1) # here dp stores the number of combinations to make up the amount at each index
        dp[0] = 1

        for coin in coins:
            for a in range(coin, amount + 1):
                dp[a] += dp[a - coin]

        return dp[amount]
    
# Explanation:

# Here’s how to read that tabulation solution in a way that maps directly to “take/skip / knapsack”.

# ---

# ## What `dp[a]` means

# After you have processed some prefix of `coins` (coin types), `dp[a]` stores:

# > **number of combinations to make sum `a` using only the coins processed so far** (unlimited copies allowed).

# So `dp` is not “global” for all coins at once — it evolves coin by coin.

# ### Base case

# ```python
# dp[0] = 1
# ```

# There is exactly **1** way to make amount 0: choose **no coins**.

# Everything else starts at 0 because initially you can’t make positive sums with no coins.

# ---

# ## Why the transition works

# When you are processing a coin value `coin`, and you’re computing `dp[a]`:

# ```python
# dp[a] += dp[a - coin]
# ```

# Interpretation:

# * `dp[a]` already counts ways to make `a` **without using this coin** (i.e., using previous coins only).
# * `dp[a - coin]` counts ways to make the smaller amount `a - coin` using coins processed so far.
# * If you take one `coin`, any way to make `a - coin` becomes a way to make `a`.

# So you’re adding “ways that use at least one `coin`” to the existing ways.

# This is exactly the unbounded knapsack “take” logic:

# * take coin → `a` depends on `a - coin`

# ---

# ## Why the loop order matters (the key interview point)

# ### Outer loop over coins

# ```python
# for coin in coins:
# ```

# This enforces **combinations** (order doesn’t matter).
# You only build solutions in the fixed coin order, so you don’t count permutations like `2+1+2` separately from `1+2+2`.

# ### Inner loop increasing from `coin` to `amount`

# ```python
# for a in range(coin, amount + 1):
# ```

# Increasing order allows reuse of the same coin multiple times in the same iteration, because when you update `dp[a]`, the value `dp[a-coin]` already includes ways that may have used `coin` earlier in this coin’s pass.

# That is what makes it **unbounded**.

# ---

# # Dry run example

# Example: `amount = 5`, `coins = [1, 2, 5]`
# Expected answer = 4 combinations:

# 1. `1+1+1+1+1`
# 2. `1+1+1+2`
# 3. `1+2+2`
# 4. `5`

# Start:
# `dp = [1, 0, 0, 0, 0, 0]`  (indexes 0..5)

# ---

# ## Process coin = 1

# For `a = 1..5`, do `dp[a] += dp[a-1]`

# * a=1: dp[1] += dp[0] → 0+1=1
#   dp = [1,1,0,0,0,0]
# * a=2: dp[2] += dp[1] → 0+1=1
#   dp = [1,1,1,0,0,0]
# * a=3: dp[3] += dp[2] → 0+1=1
#   dp = [1,1,1,1,0,0]
# * a=4: dp[4] += dp[3] → 0+1=1
#   dp = [1,1,1,1,1,0]
# * a=5: dp[5] += dp[4] → 0+1=1
#   dp = [1,1,1,1,1,1]

# Meaning now: using only coin 1, there’s exactly 1 way to make any amount.

# ---

# ## Process coin = 2

# For `a = 2..5`, do `dp[a] += dp[a-2]`

# Current dp before coin 2: `[1,1,1,1,1,1]`

# * a=2: dp[2] += dp[0] → 1+1=2
#   dp = [1,1,2,1,1,1]
#   (ways for 2: `1+1`, `2`)
# * a=3: dp[3] += dp[1] → 1+1=2
#   dp = [1,1,2,2,1,1]
#   (ways for 3: `1+1+1`, `1+2`)
# * a=4: dp[4] += dp[2] → 1+2=3
#   dp = [1,1,2,2,3,1]
#   (ways for 4: `1+1+1+1`, `1+1+2`, `2+2`)
# * a=5: dp[5] += dp[3] → 1+2=3
#   dp = [1,1,2,2,3,3]
#   (ways for 5 using 1 & 2: `1x5`, `1+1+1+2`, `1+2+2`)

# Note the unbounded behavior: for `a=4`, we used `dp[2]=2`, which already includes the combination using `2`. That’s how `2+2` appears.

# ---

# ## Process coin = 5

# For `a = 5..5`, do `dp[5] += dp[0]`

# * a=5: dp[5] += dp[0] → 3+1=4
#   dp = [1,1,2,2,3,4]

# So answer is `dp[5] = 4`, matching the 4 combinations.

# ---

# ## Mental model to remember

# * After processing coin `coin`, `dp[a]` becomes:

#   * ways without coin + ways with coin
# * “ways with coin” comes from `dp[a-coin]`
# * Coin loop outer = avoid permutations
# * Amount loop forward = allow unlimited reuse

# If you want, I can also show what goes wrong if you reverse the loop order (why it starts counting permutations).
