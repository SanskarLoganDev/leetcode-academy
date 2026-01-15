# 743. Network Delay Time
# Neetcode 150 (Important)

# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

# We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

# Example 1:
# https://assets.leetcode.com/uploads/2019/05/23/931_example_1.png
# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# Output: 2

# Example 2:

# Input: times = [[1,2,1]], n = 2, k = 1
# Output: 1

# Example 3:

# Input: times = [[1,2,1]], n = 2, k = 2
# Output: -1
 

# Constraints:

# 1 <= k <= n <= 100
# 1 <= times.length <= 6000
# times[i].length == 3
# 1 <= ui, vi <= n
# ui != vi
# 0 <= wi <= 100
# All the pairs (ui, vi) are unique. (i.e., no multiple edges.)

from typing import List
import heapq

# Dijkstra's Algorithm
# Time Complexity: O(E log V) where E is the number of edges and V is the number of vertices
# Space Complexity: O(V+E)
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n+1)] # adjacency list
        result = [float("inf")]*(n+1) # distance array
        result[k]=0 # distance to source is 0
        for u, v, time in times:
            adj[u].append((v, time)) # build the adjacency list only with u as source as this is a directed graph
        heap = []
        heapq.heappush(heap, (0, k)) # (time, node)
        while heap:
            time, u = heapq.heappop(heap) # get the node with the smallest time
            if time > result[u]: # if we have already found a better path, skip (This is a non-mandatory optimization, but does not change the time complexity)
                continue
            for v, weight in adj[u]:
                if weight+time<result[v]: # if we found a better path to v
                    result[v] = weight+time # update the distance
                    heapq.heappush(heap, (weight+time, v)) # push the new distance to the heap
        for res in result[1:]: # skip index 0 as nodes are 1-indexed
            if res == float("inf"):
                return -1 # if any node is unreachable, return -1

        return max(result[1:]) # return the maximum distance as the network delay time