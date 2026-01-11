# 787. Cheapest Flights Within K Stops
# Neetcode 150 (Important)

# There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

# You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

# Example 1:
# https://assets.leetcode.com/uploads/2022/03/18/cheapest-flights-within-k-stops-3drawio.png
# Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
# Output: 700
# Explanation:
# The graph is shown above.
# The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
# Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

# Example 2:
# https://assets.leetcode.com/uploads/2022/03/18/cheapest-flights-within-k-stops-1drawio.png
# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
# Output: 200
# Explanation:
# The graph is shown above.
# The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.

# Example 3:
# https://assets.leetcode.com/uploads/2022/03/18/cheapest-flights-within-k-stops-2drawio.png
# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
# Output: 500
# Explanation:
# The graph is shown above.
# The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.

# Constraints:

# 2 <= n <= 100
# 0 <= flights.length <= (n * (n - 1) / 2)
# flights[i].length == 3
# 0 <= fromi, toi < n
# fromi != toi
# 1 <= pricei <= 104
# There will not be any multiple flights between two cities.
# 0 <= src, dst, k < n
# src != dst

# time complexity: O(kE) where E is the number of edges
# space complexity: O(n+E) here n is the number of nodes (cities) and E is the number of edges
from typing import List
from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # We can't use min-heap here 
        # as with a min-heap, newly pushed nodes can be popped within the same layer, 
        # because they might have smaller cost than others already in the heap.
        adj = [[] for _ in range(n)]
        result = [float("inf")]*n
        for u, v, cost in flights: # making the adjacency list
            adj[u].append((v, cost))
        # print(adj)
        result[src] = 0
        q = deque()
        q.append((0, src)) # adding the source node with cost 0
        steps = 0
        while q and steps<=k:
            size = len(q)
            for _ in range(size): # process all nodes in the current layer (this for loop is basically used whenever we do BFS level order traversal)
                cost, u = q.popleft()
                for v, weight in adj[u]: # here weight is the cost to reach v from u
                    if cost+weight<result[v]:
                        result[v] = cost+weight
                        q.append((cost+weight, v))
            steps+=1
        if result[dst]==float("inf"): # if the destination is not reasched and its result is still infinity
            return -1
        return result[dst]

# Why plain Dijkstra (min-heap) is not directly appropriate here

# Dijkstra’s core correctness property is:
# When you pop a node u from the min-heap, the cost you popped is the final shortest distance to u (no later path can beat it).
# That property holds when the “state” is just the node, because Dijkstra explores in increasing cost order and edge weights are non-negative.

# But this problem’s “state” is not just the node
# Here, reaching the same city with different numbers of stops are different situations:
# A cheap way to reach city X using too many stops might be invalid for reaching dst within the limit.
# A more expensive way to reach city X with fewer stops could be the only path that still allows you to reach dst within k stops.

# So the correct state is effectively (city, stops_used) (or (city, flights_used)), not just city.
# If you try to run Dijkstra with only dist[city], you can get incorrect pruning:
# You might set dist[v] to a cheap value achieved with many stops,
# then reject a slightly higher-cost path that uses fewer stops,
# even though the fewer-stops path is the one that leads to a valid solution.