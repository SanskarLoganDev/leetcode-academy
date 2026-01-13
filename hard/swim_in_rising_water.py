# 778. Swim in Rising Water
# Neetcode 150 (Important)

# You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

# It starts raining, and water gradually rises over time. At time t, the water level is t, meaning any cell with elevation less than equal to t is submerged or reachable.

# You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

# Return the minimum time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).


# Example 1:
# https://assets.leetcode.com/uploads/2021/06/29/swim1-grid.jpg
# Input: grid = [[0,2],[1,3]]
# Output: 3
# Explanation:
# At time 0, you are in grid location (0, 0).
# You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
# You cannot reach point (1, 1) until time 3.
# When the depth of water is 3, we can swim anywhere inside the grid.

# Example 2:
# https://assets.leetcode.com/uploads/2021/06/29/swim2-grid-1.jpg
# Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
# grid = [
#  [0, 1, 2, 3, 4],
#  [24,23,22,21,5],
#  [12,13,14,15,16],
#  [11,17,18,19,20],
#  [10, 9, 8, 7, 6]
# ]
# Output: 16
# Explanation: The final route is shown.
# We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
 
# Constraints:

# n == grid.length
# n == grid[i].length
# 1 <= n <= 50
# 0 <= grid[i][j] < n2
# Each value grid[i][j] is unique.

# time complexity O(n^2 log(n^2)) = O(n^2 log(n)),  due to binary search and DFS/BFS
# space complexity O(n^2) due to visited array

from typing import List
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        l = grid[0][0]
        r = n*n-1
        res = 0
        def possibleToReach(i, j, t):
            if i<0 or j<0 or i>=n or j>=n: # boundary check
                return False

            if visited[i][j]==True: # already visited
                return False

            if grid[i][j]>t: # height check
                return False

            visited[i][j] = True # mark visited

            if i==n-1 and j==n-1: # destination reached
                return True

            for d in directions:
                ni = i+d[0]
                nj = j+d[1]

                if possibleToReach(ni, nj, t): # if 1 direction returns false here, we check other directions. If any direction returns true, we return true
                    return True 

            return False

        while l<=r:
            mid = (l+r)//2
            visited = [[False] * n for _ in range(n)]
            if possibleToReach(0,0,mid):
                res = mid # we do it so that we can return the minimum time
                r = mid-1 # try to find a smaller time
            else:
                l = mid+1 # increase time

        return res        


# BFS Solution:
from collections import deque
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        l = grid[0][0]
        r = n*n-1
        res = 0
        def possibleToReachBFS(i, j, t):
            q = deque()
            q.append((i, j))
            while q:
                i, j = q.popleft()
                if i<0 or j<0 or i>=n or j>=n:
                    continue

                if visited[i][j]==True:
                    continue

                if grid[i][j]>t:
                    continue

                visited[i][j] = True

                if i==n-1 and j==n-1:
                    return True

                for d in directions:
                    ni = i+d[0]
                    nj = j+d[1]

                    q.append((ni, nj)) # we can also add all the checks before adding to queue, but then we have to check for destination before marking visited

            return False

        while l<=r:
            mid = (l+r)//2
            visited = [[False] * n for _ in range(n)]
            if possibleToReachBFS(0,0,mid):
                res = mid
                r = mid-1
            else:
                l = mid+1

        return res
# Why return False instead of just return in DFS?

# Because in your code, the DFS is used as a boolean question:

# “Is it possible to reach the destination from here?”

# So every call must return a True/False answer to its caller.

# Dry run for DFS, following the code precisely
# Binary search iteration 1
# Line: mid = (l+r)//2

# mid = (0 + 24)//2 = 12

# Line: visited = [[False]*n for _ in range(n)]

# visited becomes a 5×5 matrix of False

# Line: if possibleToReach(0,0,mid):

# Call:

# possibleToReach(i=0, j=0, t=12)

# Enter possibleToReach(0,0,12)
# 1) Boundary check
# if i<0 or j<0 or i>=n or j>=n: return False


# (0,0) is valid → continue

# 2) Visited check
# if visited[i][j]==True: return False


# visited[0][0] is False → continue

# 3) Height check
# if grid[i][j] > t: return False


# grid[0][0] = 0, and 0 > 12? No → continue

# 4) Mark visited
# visited[0][0] = True

# 5) Destination check
# if i==n-1 and j==n-1: return True


# (0,0) is not (4,4) → continue

# 6) Explore neighbors in order of directions

# Directions order: Right, Down, Up, Left.

# Neighbor 1: Right → (0,1)

# Call possibleToReach(0,1,12)

# Valid bounds

# Not visited

# grid[0][1]=1 ≤ 12

# mark visited[0][1]=True

# not destination

# explore its neighbors…

# This continues similarly along the top row because all are ≤ 12:

# You will visit:

# (0,2) value 2

# (0,3) value 3

# (0,4) value 4

# Now at (0,4):

# Explore neighbors from (0,4):

# Right → (0,5) out of bounds → returns False immediately

# Down → (1,4) value 5 ≤ 12 → can enter

# So DFS enters (1,4).

# At (1,4) (value 5):

# Explore neighbors:

# Right → (1,5) out of bounds → False

# Down → (2,4) value 16 → check grid[2][4] > 12 is True → returns False

# Up → (0,4) already visited → False

# Left → (1,3) value 21 → 21 > 12 → False

# No neighbor returns True, so:

# return False


# for (1,4).

# That means DFS backtracks to (0,4), tries remaining directions there:

# Up is invalid

# Left is (0,3) visited
# So (0,4) returns False.

# Backtracking continues up the chain: (0,3), (0,2), (0,1), (0,0), but crucially, DFS at each point also tries Down (and other directions) where possible.

# Now from the top row, trying to go down:

# (1,0) is 24 > 12 → blocked

# (1,1) is 23 > 12 → blocked

# (1,2) is 22 > 12 → blocked

# (1,3) is 21 > 12 → blocked

# Only (1,4)=5 was allowed, but it led to dead end because (2,4)=16 is blocked at t=12.

# So the DFS will end without reaching (4,4).

# Therefore:

# possibleToReach(0,0,12) -> False

# Back to binary search:
# if possibleToReach(...):
#     ...
# else:
#     l = mid + 1


# So:

# l = 12 + 1 = 13

# Binary search iteration 2

# l=13, r=24

# mid = (13+24)//2 = 18

# reset visited all False again

# Call possibleToReach(0,0,18)

# Key difference at t=18

# Now (2,4)=16 is allowed, and also (2,1)=13, (2,2)=14, (2,3)=15, etc. That opens the “bridge” into the middle.

# DFS path (one of the first successful ones given your direction order):

# It again goes right across the top row:
# (0,0) → (0,1) → (0,2) → (0,3) → (0,4)

# Down to (1,4)=5

# Down to (2,4)=16 (NOW allowed because 16 ≤ 18)

# From (2,4), DFS tries neighbors in order:

# Right (2,5) invalid

# Down (3,4)=20 blocked at t=18

# Up (1,4) visited

# Left (2,3)=15 allowed → go left

# Then it can traverse left across row 2: (2,3)=15 → (2,2)=14 → (2,1)=13 → (2,0)=12

# From (2,0), Down (3,0)=11 allowed

# From (3,0), Down (4,0)=10 allowed

# From (4,0), Right along bottom: 9 → 8 → 7 → 6 reaching (4,4)

# When it reaches (4,4):

# if i==n-1 and j==n-1:
#     return True


# That True returns back up the recursion chain immediately:

# The call that moved into (4,4) returns True,

# then its caller returns True,

# … until the initial call returns True.

# So:

# possibleToReach(0,0,18) -> True

# Back to binary search

# Since True:

# res = mid   # res = 18
# r = mid - 1 # r = 17

# Binary search iteration 3

# l=13, r=17

# mid = (13+17)//2 = 15

# reset visited again

# Call possibleToReach(0,0,15).

# At t=15, note:

# (2,4)=16 is blocked again.
# So the earlier “bridge” is closed, DFS gets stuck at (1,4)=5 again (exactly like t=12 case).

# Hence:

# DFS returns False

# Update: l = 16

# Binary search iteration 4

# l=16, r=17

# mid = (16+17)//2 = 16

# reset visited

# Call possibleToReach(0,0,16)

# Now (2,4)=16 is allowed again, so the same successful route works.

# returns True

# Update: res = 16, r = 15

# Now loop ends because l=16 > r=15.

# Return res = 16.

