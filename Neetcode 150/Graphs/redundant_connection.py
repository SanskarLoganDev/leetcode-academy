# 684. Redundant Connection
# Neetcode 150 (Important)

# In this problem, a tree is an undirected graph that is connected and has no cycles.

# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

# Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

# Example 1:

# Input: edges = [[1,2],[1,3],[2,3]]
# Output: [2,3]

# Example 2:

# Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
# Output: [1,4]
 
# Constraints:

# n == edges.length
# 3 <= n <= 1000
# edges[i].length == 2
# 1 <= ai < bi <= edges.length
# ai != bi
# There are no repeated edges.
# The given graph is connected.

# time complexity: O(N^2)
# space complexity: O(N)
# Using DFS to detect cycle

from typing import List
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)+1
        adj = [[] for _ in range(n)]
        uniq = set() # to keep track of unique nodes added so far
        def dfs(u, v): # here u is the current node and v is the target node we want to find to detect cycle; 
            # therefore inside we create neighbor variable for adjacent nodes (which is usually v in other problems)
            visited[u] = True
            if u==v:
                return True
            for neighbor in adj[u]:
                if visited[neighbor]==True:
                    continue
                if dfs(neighbor, v):
                    return True
            return False
        
        for u, v in edges:
            visited = [False]*n # here we have to reinitialize visited for every edge because we are checking for cycle for every new edge
            if u in uniq and v in uniq:
                if dfs(u, v):
                    return [u, v]
            adj[u].append(v) # build the adjacency list after checking for cycle
            adj[v].append(u)
            uniq.add(u)
            uniq.add(v)
        
# time complexity: O(N^2)
# space complexity: O(N)

# Using BFS to detect cycle
from collections import deque        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)+1
        adj = [[] for _ in range(n)]
        uniq = set() # to keep track of unique nodes added so far
        def bfs(u, v):
            visited[u] = True
            q = deque()
            q.append(u)
            while q:
                source = q.popleft()
                if source == v:
                    return True
                for neighbor in adj[source]:
                    if visited[neighbor]==True:
                        continue
                    visited[neighbor]=True # mark as visited when enqueuing to avoid multiple enqueuing
                    q.append(neighbor)
            return False
        
        for u, v in edges:
            visited = [False]*n # reinitialize visited for every edge
            if u in uniq and v in uniq:
                if bfs(u, v):
                    return [u, v]
            adj[u].append(v) # build the adjacency list after checking for cycle
            adj[v].append(u)
            uniq.add(u) # add nodes to the set of unique nodes
            uniq.add(v)
        
