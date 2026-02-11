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
