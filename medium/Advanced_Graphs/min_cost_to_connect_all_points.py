# 1584. Min Cost to Connect All Points
# Neetcode 150 (Important)

# You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

# Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

# Example 1:
# https://assets.leetcode.com/uploads/2020/08/26/d.png
# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20
# Explanation: 
# https://assets.leetcode.com/uploads/2020/08/26/c.png
# We can connect the points as shown above to get the minimum cost of 20.
# Notice that there is a unique path between every pair of points.

# Example 2:

# Input: points = [[3,12],[-2,5],[-4,1]]
# Output: 18

# Constraints:

# 1 <= points.length <= 1000
# -106 <= xi, yi <= 106
# All pairs (xi, yi) are distinct.

# Complexity Analysis
# Time complexity O(n^2.logn)
# Space complexity O(n^2) (due to adjacency list and heap growth)

# This is Prim’s algorithm with a min-heap but on a dense graph.

# Number of edges in the complete graph: 

# E=Θ(n^2).

# In your implementation, you potentially heappush an entry for many edges; in the worst case it is 
# Θ(E) pushes and 
# Θ(E) pops (many pops are “stale” because you skip nodes already in MST).

# Each heap op costs 
# O(logH), and 
# H can grow to 

# Θ(E), so each op is 

# O(logE)=O(logn).

import heapq
from typing import List
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = [[] for _ in range(len(points))]
        for i in range(len(points)): # build adjacency list
            for j in range(i+1, len(points)): # for calculating manhattan distance for each point
                if i==j:
                    continue
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]) # Manhattan distance
                adj[j].append([i, dist]) # add edge j->i with weight dist
                adj[i].append([j, dist]) # add edge i->j with weight dist

        heap = [[0,0]]
        inMST = [False]*len(points) # to check if a node is included in MST
        sum = 0
        while heap:
            w, u = heapq.heappop(heap) # get the edge with minimum weight

            if inMST[u]==True:
                continue

            sum+=w # include weight
            inMST[u] = True # include u in MSTq
            for v, w in adj[u]: # traverse all adjacent nodes of u
                if inMST[v]==False:
                    heapq.heappush(heap, [w, v])

        return sum