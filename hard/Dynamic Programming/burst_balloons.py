# 312. Burst Balloons
# Neetcode 150 (Important)

# You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

# If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

# Return the maximum coins you can collect by bursting the balloons wisely.

# Example 1:

# Input: nums = [3,1,5,8]
# Output: 167
# Explanation:
# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

# Example 2:

# Input: nums = [1,5]
# Output: 10
 

# Constraints:

# n == nums.length
# 1 <= n <= 300
# 0 <= nums[i] <= 100

from typing import List
# Brute force solution
# time complexity O(N!) and space complexity O(N)
# Your brute force tries every possible order of bursting balloons:

# At the first level you have 
# n choices (burst any balloon).
# Then n−1 choices.
# Then n−2, …, down to 1.
# n.(n−1).(n−2)…1 = n! possible orders.

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        def solve(arr):
            maxx = float("-inf")
            if  len(arr)==0:
                return 0
            n = len(arr)
            if n==1:
                return 1*arr[0]*1+solve([])
            burst = 0
            for i in range(n):
                if i-1<0:
                    burst = 1*arr[i]*arr[i+1]+solve(arr[i+1:])
                elif i+1==n:
                    burst = arr[i-1]*arr[i]*1+solve(arr[:i])
                else:
                    burst = arr[i-1]*arr[i]*arr[i+1]+solve(arr[:i]+arr[i+1:])
                maxx = max(maxx, burst)
            return maxx
        return solve(nums)
            
# Brute force dry run

# solve([3, 1, 5, 8])
#   i=0 burst 3: coins_now=1*3*1=3 + solve([1, 5, 8])
#     solve([1, 5, 8])
#       i=0 burst 1: coins_now=1*1*5=5 + solve([5, 8])
#         solve([5, 8])
#           i=0 burst 5: coins_now=1*5*8=40 + solve([8])
#             solve([8]) -> 8  (only balloon: 1*8*1)
#             total = 40 + 8 = 48
#             maxx updated -> 48
#           i=1 burst 8: coins_now=5*8*1=40 + solve([5])
#             solve([5]) -> 5  (only balloon: 1*5*1)
#             total = 40 + 5 = 45
#             maxx stays -> 48
#         return 48
#         total = 5 + 48 = 53
#         maxx updated -> 53
#       i=1 burst 5: coins_now=1*5*8=40 + solve([1, 8])
#         solve([1, 8])
#           i=0 burst 1: coins_now=1*1*8=8 + solve([8])
#             solve([8]) -> 8  (only balloon: 1*8*1)
#             total = 8 + 8 = 16
#             maxx updated -> 16
#           i=1 burst 8: coins_now=1*8*1=8 + solve([1])
#             solve([1]) -> 1  (only balloon: 1*1*1)
#             total = 8 + 1 = 9
#             maxx stays -> 16
#         return 16
#         total = 40 + 16 = 56
#         maxx updated -> 56
#       i=2 burst 8: coins_now=5*8*1=40 + solve([1, 5])
#         solve([1, 5])
#           i=0 burst 1: coins_now=1*1*5=5 + solve([5])
#             solve([5]) -> 5  (only balloon: 1*5*1)
#             total = 5 + 5 = 10
#             maxx updated -> 10
#           i=1 burst 5: coins_now=1*5*1=5 + solve([1])
#             solve([1]) -> 1  (only balloon: 1*1*1)
#             total = 5 + 1 = 6
#             maxx stays -> 10
#         return 10
#         total = 40 + 10 = 50
#         maxx stays -> 56
#     return 56
#     total = 3 + 56 = 59
#     maxx updated -> 59

#   i=1 burst 1: coins_now=3*1*5=15 + solve([3, 5, 8])
#     solve([3, 5, 8])
#       i=0 burst 3: coins_now=1*3*5=15 + solve([5, 8])
#         solve([5, 8])
#           i=0 burst 5: coins_now=1*5*8=40 + solve([8])
#             solve([8]) -> 8  (only balloon: 1*8*1)
#             total = 40 + 8 = 48
#             maxx updated -> 48
#           i=1 burst 8: coins_now=5*8*1=40 + solve([5])
#             solve([5]) -> 5  (only balloon: 1*5*1)
#             total = 40 + 5 = 45
#             maxx stays -> 48
#         return 48
#         total = 15 + 48 = 63
#         maxx updated -> 63
#       i=1 burst 5: coins_now=3*5*8=120 + solve([3, 8])
#         solve([3, 8])
#           i=0 burst 3: coins_now=1*3*8=24 + solve([8])
#             solve([8]) -> 8  (only balloon: 1*8*1)
#             total = 24 + 8 = 32
#             maxx updated -> 32
#           i=1 burst 8: coins_now=3*8*1=24 + solve([3])
#             solve([3]) -> 3  (only balloon: 1*3*1)
#             total = 24 + 3 = 27
#             maxx stays -> 32
#         return 32
#         total = 120 + 32 = 152
#         maxx updated -> 152
#       i=2 burst 8: coins_now=5*8*1=40 + solve([3, 5])
#         solve([3, 5])
#           i=0 burst 3: coins_now=1*3*5=15 + solve([5])
#             solve([5]) -> 5  (only balloon: 1*5*1)
#             total = 15 + 5 = 20
#             maxx updated -> 20
#           i=1 burst 5: coins_now=3*5*1=15 + solve([3])
#             solve([3]) -> 3  (only balloon: 1*3*1)
#             total = 15 + 3 = 18
#             maxx stays -> 20
#         return 20
#         total = 40 + 20 = 60
#         maxx stays -> 152
#     return 152
#     total = 15 + 152 = 167
#     maxx updated -> 167

#   i=2 burst 5: coins_now=1*5*8=40 + solve([3, 1, 8])
#     solve([3, 1, 8])
#       i=0 burst 3: coins_now=1*3*1=3 + solve([1, 8])
#         solve([1, 8])
#           i=0 burst 1: coins_now=1*1*8=8 + solve([8])
#             solve([8]) -> 8  (only balloon: 1*8*1)
#             total = 8 + 8 = 16
#             maxx updated -> 16
#           i=1 burst 8: coins_now=1*8*1=8 + solve([1])
#             solve([1]) -> 1  (only balloon: 1*1*1)
#             total = 8 + 1 = 9
#             maxx stays -> 16
#         return 16
#         total = 3 + 16 = 19
#         maxx updated -> 19
#       i=1 burst 1: coins_now=3*1*8=24 + solve([3, 8])
#         solve([3, 8])
#           i=0 burst 3: coins_now=1*3*8=24 + solve([8])
#             solve([8]) -> 8  (only balloon: 1*8*1)
#             total = 24 + 8 = 32
#             maxx updated -> 32
#           i=1 burst 8: coins_now=3*8*1=24 + solve([3])
#             solve([3]) -> 3  (only balloon: 1*3*1)
#             total = 24 + 3 = 27
#             maxx stays -> 32
#         return 32
#         total = 24 + 32 = 56
#         maxx updated -> 56
#       i=2 burst 8: coins_now=1*8*1=8 + solve([3, 1])
#         solve([3, 1])
#           i=0 burst 3: coins_now=1*3*1=3 + solve([1])
#             solve([1]) -> 1  (only balloon: 1*1*1)
#             total = 3 + 1 = 4
#             maxx updated -> 4
#           i=1 burst 1: coins_now=3*1*1=3 + solve([3])
#             solve([3]) -> 3  (only balloon: 1*3*1)
#             total = 3 + 3 = 6
#             maxx updated -> 6
#         return 6
#         total = 8 + 6 = 14
#         maxx stays -> 56
#     return 56
#     total = 40 + 56 = 96
#     maxx stays -> 167

#   i=3 burst 8: coins_now=5*8*1=40 + solve([3, 1, 5])
#     solve([3, 1, 5])
#       i=0 burst 3: coins_now=1*3*1=3 + solve([1, 5])
#         solve([1, 5])
#           i=0 burst 1: coins_now=1*1*5=5 + solve([5])
#             solve([5]) -> 5  (only balloon: 1*5*1)
#             total = 5 + 5 = 10
#             maxx updated -> 10
#           i=1 burst 5: coins_now=1*5*1=5 + solve([1])
#             solve([1]) -> 1  (only balloon: 1*1*1)
#             total = 5 + 1 = 6
#             maxx stays -> 10
#         return 10
#         total = 3 + 10 = 13
#         maxx updated -> 13
#       i=1 burst 1: coins_now=3*1*5=15 + solve([3, 5])
#         solve([3, 5])
#           i=0 burst 3: coins_now=1*3*5=15 + solve([5])
#             solve([5]) -> 5  (only balloon: 1*5*1)
#             total = 15 + 5 = 20
#             maxx updated -> 20
#           i=1 burst 5: coins_now=3*5*1=15 + solve([3])
#             solve([3]) -> 3  (only balloon: 1*3*1)
#             total = 15 + 3 = 18
#             maxx stays -> 20
#         return 20
#         total = 15 + 20 = 35
#         maxx updated -> 35
#       i=2 burst 5: coins_now=1*5*1=5 + solve([3, 1])
#         solve([3, 1])
#           i=0 burst 3: coins_now=1*3*1=3 + solve([1])
#             solve([1]) -> 1  (only balloon: 1*1*1)
#             total = 3 + 1 = 4
#             maxx updated -> 4
#           i=1 burst 1: coins_now=3*1*1=3 + solve([3])
#             solve([3]) -> 3  (only balloon: 1*3*1)
#             total = 3 + 3 = 6
#             maxx updated -> 6
#         return 6
#         total = 5 + 6 = 11
#         maxx stays -> 35
#     return 35
#     total = 40 + 35 = 75
#     maxx stays -> 167

# return 167


# Optimized solution using memoization
# time complexity O(N^3) and space complexity O(N^2)


# solve(l, r) returns:

# the maximum coins you can get by bursting all balloons with indices in [l..r], assuming balloons outside this interval remain unburst for now.

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1]+nums+[1]
        memo = {}
        def solve(l, r):
            if l>r:
                return 0
            key = (l, r)
            if key in memo:
                return memo[key]
            memo[key] = 0
            for i in range(l, r+1):
                coins = nums[l-1]*nums[i]*nums[r+1]
                coins+= solve(l, i-1)+solve(i+1, r)
                memo[key] = max(memo[key], coins)
            return memo[key]

        return solve(1, len(nums)-2)
    
    
# Dry run (end-to-end, actual call order)

# I’ll format as:

# solve(l,r) called

# loop over i

# compute coins_last = nums[l-1] * nums[i] * nums[r+1]

# then it needs:

# left = solve(l, i-1)

# right = solve(i+1, r)

# total = coins_last + left + right

# update memo[(l,r)] = max(...)

# Base case: if l > r return 0 immediately.

# Call 1: solve(1,4)

# l<=r, not in memo → initialize memo[(1,4)] = 0.

# Loop i = 1..4.

# In solve(1,4), try i = 1 last

# coins_last = nums[0]*nums[1]*nums[5] = 1*3*1 = 3

# Need:

# left = solve(1,0) (since i-1 = 0)

# right = solve(2,4)

# Call 2: solve(1,0)

# Here l > r → return 0.

# Call 3: solve(2,4)

# Not in memo → set memo[(2,4)] = 0.
# Loop i = 2..4.

# In solve(2,4), try i = 2 last

# coins_last = nums[1]*nums[2]*nums[5] = 3*1*1 = 3
# Need:

# left = solve(2,1)

# right = solve(3,4)

# Call 4: solve(2,1)

# l > r → return 0

# Call 5: solve(3,4)

# Not in memo → set memo[(3,4)] = 0
# Loop i = 3..4

# In solve(3,4), try i = 3 last

# coins_last = nums[2]*nums[3]*nums[5] = 1*5*1 = 5
# Need:

# left = solve(3,2)

# right = solve(4,4)

# Call 6: solve(3,2)

# l > r → return 0

# Call 7: solve(4,4)

# Not in memo → set memo[(4,4)] = 0
# Loop i = 4..4 only

# In solve(4,4), try i = 4 last

# coins_last = nums[3]*nums[4]*nums[5] = 5*8*1 = 40
# Need:

# solve(4,3) and solve(5,4)

# Call 8: solve(4,3) → l>r return 0
# Call 9: solve(5,4) → l>r return 0

# Total = 40 + 0 + 0 = 40
# Update memo[(4,4)] = 40
# Return from solve(4,4) → 40

# Back to solve(3,4) at i=3:
# Total = coins_last(5) + left(0) + right(40) = 45
# Update memo[(3,4)] = max(0,45) = 45

# In solve(3,4), try i = 4 last

# coins_last = nums[2]*nums[4]*nums[5] = 1*8*1 = 8
# Need:

# left = solve(3,3)

# right = solve(5,4)

# Call 10: solve(3,3)

# Not in memo → set memo[(3,3)] = 0
# Loop i=3..3

# coins_last = nums[2]*nums[3]*nums[4] = 1*5*8 = 40

# solve(3,2) (Call 11) → 0

# solve(4,3) (Call 12) → 0
# Total = 40
# Update memo[(3,3)] = 40
# Return solve(3,3) → 40

# Call 13: solve(5,4) → l>r return 0

# Back to solve(3,4) at i=4:
# Total = 8 + 40 + 0 = 48
# Update memo[(3,4)] = max(45,48) = 48

# End solve(3,4) → return 48

# Back to solve(2,4) at i=2:

# left = 0

# right = 48
# Total = 3 + 0 + 48 = 51
# Update memo[(2,4)] = max(0,51) = 51

# In solve(2,4), try i = 3 last

# coins_last = nums[1]*nums[3]*nums[5] = 3*5*1 = 15
# Need:

# left = solve(2,2)

# right = solve(4,4) (already computed)

# Call 14: solve(2,2)

# Not in memo → set memo[(2,2)] = 0
# Loop i=2..2:

# coins_last = nums[1]*nums[2]*nums[3] = 3*1*5 = 15

# solve(2,1) (Call 15) → 0

# solve(3,2) (Call 16) → 0
# Total = 15
# Update memo[(2,2)] = 15
# Return solve(2,2) → 15

# Call 17: solve(4,4)

# Memo hit → return 40

# Back to solve(2,4) at i=3:
# Total = 15 + 15 + 40 = 70
# Update memo[(2,4)] = max(51,70) = 70

# In solve(2,4), try i = 4 last

# coins_last = nums[1]*nums[4]*nums[5] = 3*8*1 = 24
# Need:

# left = solve(2,3)

# right = solve(5,4)

# Call 18: solve(2,3)

# Not in memo → set memo[(2,3)] = 0
# Loop i=2..3

# i=2 last in solve(2,3)

# coins_last = nums[1]*nums[2]*nums[4] = 3*1*8 = 24
# Need:

# solve(2,1) (Call 19) → 0

# solve(3,3) (Call 20) → memo hit = 40
# Total = 24 + 0 + 40 = 64
# Update memo[(2,3)] = 64

# i=3 last in solve(2,3)

# coins_last = nums[1]*nums[3]*nums[4] = 3*5*8 = 120
# Need:

# solve(2,2) (Call 21) → memo hit = 15

# solve(4,3) (Call 22) → 0
# Total = 120 + 15 + 0 = 135
# Update memo[(2,3)] = max(64,135) = 135

# Return solve(2,3) → 135

# Call 23: solve(5,4) → 0

# Back to solve(2,4) at i=4:
# Total = 24 + 135 + 0 = 159
# Update memo[(2,4)] = max(70,159) = 159

# End solve(2,4) → return 159

# Back to top solve(1,4) at i=1:

# left = solve(1,0) = 0

# right = solve(2,4) = 159
# Total = coins_last(3) + 0 + 159 = 162
# Update memo[(1,4)] = max(0,162) = 162

# In solve(1,4), try i = 2 last

# coins_last = nums[0]*nums[2]*nums[5] = 1*1*1 = 1
# Need:

# left = solve(1,1)

# right = solve(3,4) (memo hit)

# Call 24: solve(1,1)

# Not in memo → set memo[(1,1)] = 0
# Loop i=1..1:

# coins_last = nums[0]*nums[1]*nums[2] = 1*3*1 = 3

# solve(1,0) (Call 25) → 0

# solve(2,1) (Call 26) → 0
# Total = 3
# Update memo[(1,1)] = 3
# Return solve(1,1) → 3

# Call 27: solve(3,4) memo hit → 48

# Back to solve(1,4) at i=2:
# Total = 1 + 3 + 48 = 52
# Update memo[(1,4)] stays 162 (since 162 > 52)

# In solve(1,4), try i = 3 last

# coins_last = nums[0]*nums[3]*nums[5] = 1*5*1 = 5
# Need:

# left = solve(1,2)

# right = solve(4,4) memo hit

# Call 28: solve(1,2)

# Not in memo → set memo[(1,2)] = 0
# Loop i=1..2

# i=1 last in solve(1,2)

# coins_last = nums[0]*nums[1]*nums[3] = 1*3*5 = 15
# Need:

# solve(1,0) (Call 29) → 0

# solve(2,2) (Call 30) → memo hit = 15
# Total = 15 + 0 + 15 = 30
# Update memo[(1,2)] = 30

# i=2 last in solve(1,2)

# coins_last = nums[0]*nums[2]*nums[3] = 1*1*5 = 5
# Need:

# solve(1,1) (Call 31) → memo hit = 3

# solve(3,2) (Call 32) → 0
# Total = 5 + 3 + 0 = 8
# memo[(1,2)] stays 30

# Return solve(1,2) → 30

# Call 33: solve(4,4) memo hit → 40

# Back to solve(1,4) at i=3:
# Total = 5 + 30 + 40 = 75
# memo[(1,4)] stays 162

# In solve(1,4), try i = 4 last

# coins_last = nums[0]*nums[4]*nums[5] = 1*8*1 = 8
# Need:

# left = solve(1,3)

# right = solve(5,4) (0)

# Call 34: solve(1,3)

# Not in memo → set memo[(1,3)] = 0
# Loop i=1..3

# i=1 last in solve(1,3)

# coins_last = nums[0]*nums[1]*nums[4] = 1*3*8 = 24
# Need:

# solve(1,0) (Call 35) → 0

# solve(2,3) (Call 36) → memo hit = 135
# Total = 24 + 0 + 135 = 159
# Update memo[(1,3)] = 159

# i=2 last in solve(1,3)

# coins_last = nums[0]*nums[2]*nums[4] = 1*1*8 = 8
# Need:

# solve(1,1) (Call 37) → 3

# solve(3,3) (Call 38) → 40
# Total = 8 + 3 + 40 = 51
# memo[(1,3)] stays 159

# i=3 last in solve(1,3)

# coins_last = nums[0]*nums[3]*nums[4] = 1*5*8 = 40
# Need:

# solve(1,2) (Call 39) → memo hit = 30

# solve(4,3) (Call 40) → 0
# Total = 40 + 30 + 0 = 70
# memo[(1,3)] stays 159

# Return solve(1,3) → 159

# Call 41: solve(5,4) → 0

# Back to solve(1,4) at i=4:
# Total = 8 + 159 + 0 = 167
# Update memo[(1,4)] = max(162,167) = 167

# End of solve(1,4)

# Return 167.