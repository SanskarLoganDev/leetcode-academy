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


#### PRIMS ALGO ####


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
    
    
    
#### KRUSKAL'S ALGO ####

from typing import List

# Complexity Analysis
# Time complexity O(n^2.logn)
# Space complexity O(n^2) (due to edge list)
class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n  # union by size

    def find(self, x: int) -> int:
        # Path compression (path halving)
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False

        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return 0

        # 1) Build all edges in the complete graph
        edges = []
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                w = abs(x1 - x2) + abs(y1 - y2)
                edges.append((w, i, j))

        # 2) Sort edges by weight
        edges.sort(key=lambda x: x[0])

        # 3) Kruskal: add edges that connect different components
        dsu = DSU(n)
        mst_cost = 0
        used = 0

        for w, u, v in edges:
            if dsu.union(u, v):
                mst_cost += w
                used += 1
                if used == n - 1:
                    break

        return mst_cost

# How DSU prevents cycles (the “why”)

# When considering an edge (u, v):

# If find(u) == find(v), u and v are already connected by previously chosen edges → adding this edge would create a cycle → skip.

# Otherwise, union(u, v) merges the components → safe to add.

# Dry run (Example 1)

# points = [[0,0],[2,2],[3,10],[5,2],[7,0]]

# Index them:

# 0:(0,0)

# 1:(2,2)

# 2:(3,10)

# 3:(5,2)

# 4:(7,0)

# Compute key Manhattan distances (not all shown, but enough to see Kruskal decisions):

# (1,3): |2-5|+|2-2| = 3

# (0,1): 4

# (3,4): |5-7|+|2-0| = 4

# (0,3): 7

# (0,4): 7

# (1,4): 7

# (1,2): 9

# (2,3): 10

# (0,2): 13

# (2,4): 14

# Sorted (smallest first):

# w=3 edge (1,3)

# w=4 edge (0,1)

# w=4 edge (3,4)

# w=7 edge (0,3)

# w=7 edge (0,4)

# w=7 edge (1,4)

# w=9 edge (1,2)
# ... (others larger)

# Now Kruskal:

# Start: components = {0},{1},{2},{3},{4}, cost=0

# Take (1,3) w=3

# find(1)!=find(3) → union → cost=3

# components: {1,3}, {0}, {2}, {4}

# Take (0,1) w=4

# 0 is separate, 1 is in {1,3} → union → cost=7

# components: {0,1,3}, {2}, {4}

# Take (3,4) w=4

# 3 in {0,1,3}, 4 separate → union → cost=11

# components: {0,1,3,4}, {2}

# Next edges w=7 like (0,3), (0,4), (1,4)

# all connect nodes already inside {0,1,3,4} → would create cycle → skip

# Take (1,2) w=9

# 2 is separate → union → cost=20

# components: {0,1,2,3,4} (all connected)

# We used n-1 = 4 edges, stop.
# Answer = 20.

# Time and space complexity

# Let n = len(points).

# Number of edges in complete graph:
# E = n(n-1)/2 = O(n^2)

# Building edges: O(n^2)

# Sorting edges: O(E log E) = O(n^2 log n^2) = O(n^2 log n)

# DSU operations across all edges: O(E α(n)) ~ O(n^2) (almost constant per op)

# Total time: O(n^2 log n)
# Space: storing edges dominates: O(n^2)

# Important practical note: for n = 1000, E ≈ 499,500 edges—this is large but typically still workable in Python; 
# Prim’s approach is often preferred because it avoids storing/sorting all edges, but Kruskal is still valid and commonly accepted.