# 323. Number of Connected Components in an Undirected Graph
# Neetcode 150 (Important)

# You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

# Return the number of connected components in the graph.

# Example 1:
# https://assets.leetcode.com/uploads/2021/03/14/conn1-graph.jpg
# Input: n = 5, edges = [[0,1],[1,2],[3,4]]
# Output: 2

# Example 2:
# https://assets.leetcode.com/uploads/2021/03/14/conn2-graph.jpg
# Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
# Output: 1
 

# Constraints:

# 1 <= n <= 2000
# 1 <= edges.length <= 5000
# edges[i].length == 2
# 0 <= ai <= bi < n
# ai != bi
# There are no repeated edges.

from typing import List
from collections import deque

# time complexity: O(V+E)
# space complexity: O(V+E) for adjacency list
# Using BFS to count connected components
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [False]*n
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def bfsCycle(u):
            visited[u]=True
            q = deque()
            q.append((u, -1))
            while q:
                source, parent = q.popleft() # dequeue front element
                for v in adj[source]:
                    if v == parent: # skip the parent node
                        continue
                    if visited[v]==True:
                        continue # usually we return True for cycle detection, here we just continue as we only need connected components count
                    visited[v] = True
                    q.append((v, source))

        count=0
        for u in range(n):
            if visited[u]!=True:
                count+=1
                bfsCycle(u)

        return count
    
# time complexity: O(V+E)
# space complexity: O(V+E) for adjacency list
# Using DFS to count connected components  
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [False]*n
        adj = [[] for _ in range(n)]
        for u, v in edges: # build adjacency list
            adj[u].append(v)
            adj[v].append(u)

        def dfsCycle(u, parent):
            visited[u]=True
            for v in adj[u]: # traverse all adjacent nodes
                if v == parent: # skip the parent node
                    continue
                if visited[v]==True:
                    continue # usually we return True for cycle detection, here we just continue as we only need connected components count
                dfsCycle(v, u)

        count=0
        for u in range(n):
            if visited[u]!=True:
                count+=1
                dfsCycle(u, -1) # usually we have if checks and return for cycle detection, here we just call dfs as we only need connected components count

        return count