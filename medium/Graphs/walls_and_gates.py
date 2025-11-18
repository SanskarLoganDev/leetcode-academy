# 286. Walls and Gates
# Neetcode 150

# You are given an m x n grid rooms initialized with these three possible values.

# -1 A wall or an obstacle.
# 0 A gate.
# INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

# Example 1:
# https://assets.leetcode.com/uploads/2021/01/03/grid.jpg
# Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
# Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

# Example 2:
# Input: rooms = [[-1]]
# Output: [[-1]]

# Constraints:

# m == rooms.length
# n == rooms[i].length
# 1 <= m, n <= 250
# rooms[i][j] is -1, 0, or 231 - 1.


# Why use BFS:
# BFS advantages here

# Guarantees shortest path in an unweighted graph

# BFS explores in layers: all cells at distance 1, then 2, then 3, …

# The first time we reach a gate, the distance is automatically the minimum possible.

# We can early return as soon as we see a gate.

# Simple distance handling

# Just carry dist in the queue or increase per layer.

# No need to keep a global min or explore everything.


# Most efficeient approach is multi-source BFS starting from all gates simultaneously.
# Time complexity O(M*N)
# Space complexity O(M*N) in worst case when all rooms are gates
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        n = len(rooms[0])
        q = deque()
        INF = 2**31 - 1
        directions = [(1,0),(0,1),(-1,0),(0,-1) ]
        for i in range(m):
            for j in range(n):
                if rooms[i][j]==0:
                    q.append((i,j))

        while q:
            i, j = q.popleft()
            for d in directions:
                ni = i+d[0]
                nj = j+d[1]

                if ni<0 or nj<0 or ni>=m or nj>=n:
                    continue

                if rooms[ni][nj]!=INF:
                    continue

                rooms[ni][nj] = rooms[i][j]+1
                q.append((ni, nj))




# Brute force using BFS from each empty room:
from typing import List
from collections import deque
# time complexity O((M*N)^2) in worst case when all cells are INF except one gate at one corner
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        n = len(rooms[0])


        def bfs(i, j):
            q = deque()
            q.append((i,j,0)) # we also add distance to the queue
            directions = [(1,0),(0,1),(-1,0),(0,-1)]
            visited = [[False]*n for _ in range(m)] # we do this instead of marking visited in rooms to avoid modifying original grid
            dist = 0
            while q:
                i, j, dist = q.popleft()
                for d in directions:
                    ni = i + d[0]
                    nj = j + d[1]
                    if ni<0 or ni>=m or nj<0 or nj>=n or rooms[ni][nj]==-1:
                        continue
                    if visited[ni][nj]==True:
                        continue
                    if rooms[ni][nj]==0:
                        return dist+1 # one more step from current cell, distance is added to queue element because each cell can have different distance
                    visited[ni][nj]=True
                    q.append((ni, nj, dist+1))
            return 2147483647 # if no gate is found, return INF

        for i in range(m):
            for j in range(n):
                if rooms[i][j]==2147483647:
                    rooms[i][j] = bfs(i, j) # update the distance to nearest gate

# Explanation of distance calculation:
# Why distance += 1 in the loop is wrong
# Imagine this tiny grid (S = start, G = gate, . = empty):

# Row 0: S . .
# Row 1: . . G

# Coordinates:
# Start S at (0, 0)
# Gate G at (1, 2)

# Shortest path from S to G is 3 steps:

# (0,0) → (0,1) → (0,2) → (1,2) → distance 3.

# Now let’s see what happens with bad code like this:

# distance = 0
# q = deque()
# q.append((0, 0))

# while q:
#     i, j = q.popleft()
#     for di, dj in directions:
#         ni, nj = i + di, j + dj
#         # ... bounds, walls etc ...
#         if rooms[ni][nj] == 0:   # gate
#             return distance
#         distance += 1
#         q.append((ni, nj))

# Let’s simulate:

# Step 1
# q = [(0,0)], distance = 0
# Pop (0,0)

# Its valid neighbors: (0,1) and (1,0)

# For (0,1): not gate → distance = 1, enqueue (0,1)

# For (1,0): not gate → distance = 2, enqueue (1,0)

# End:

# q = [(0,1), (1,0)]

# distance = 2

# Already notice something: both (0,1) and (1,0) are 1 step away from the start,
# but distance is 2 after processing them. So distance is no longer “distance from S”; it’s “how many neighbors we’ve seen so far”.

# Step 2
# Pop (0,1) (distance is still global = 2)
# Neighbors: (0,2) and (1,1) etc.

# (0,2): not gate → distance = 3, enqueue (0,2)

# (1,1): not gate → distance = 4, enqueue (1,1)

# Now:
# q also has (1,0) from earlier + new nodes, and distance = 4

# But what are real distances?
# (0,2) is 2 steps from start.
# (1,1) is also 2 steps from start.
# Yet we have distance = 4 by the time we discover them.

