# 261. Graph Valid Tree
# Neetcode 150 (Important)
# You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

# Return true if the edges of the given graph make up a valid tree, and false otherwise.

# Example 1:
# https://assets.leetcode.com/uploads/2021/03/12/tree1-graph.jpg
# Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
# Output: true

# Example 2:
# https://assets.leetcode.com/uploads/2021/03/12/tree2-graph.jpg
# Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
# Output: false
 
# Constraints:

# 1 <= n <= 2000
# 0 <= edges.length <= 5000
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# There are no self-loops or repeated edges.

from typing import List

# time complexity: O(V+E)
# space complexity: O(V+E) for adjacency list

# Using the concept of cycle detection in undirected graph using DFS
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = [False]*n
        adj = [[] for _ in range(n)] # adjacency list
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfsCycle(u, parent): # detect cycle in undirected graph using DFS
            visited[u]=True
            for v in adj[u]:
                if v == parent: # skip the parent node
                    continue
                if visited[v]==True: # if already visited and not parent then cycle is there
                    return True
                if dfsCycle(v, u): # if cycle is found in subtree
                    return True
            return False
        count=0
        for u in range(n):
            if visited[u]!=True:
                count+=1 # count connected components, if more than 1 then not a tree
                if dfsCycle(u, -1):
                    return False
        if count>1: # if more than 1 connected component then not a tree
            return False
        return True
    
from collections import deque
# time complexity: O(V+E)
# space complexity: O(V+E) for adjacency list

# Using the concept of cycle detection in undirected graph using BFS
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
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
                source, parent = q.popleft() # parent to avoid counting the immediate parent as a cycle
                for v in adj[source]:
                    if v == parent: # skip the parent node
                        continue
                    if visited[v]==True: # if already visited and not parent then cycle is there
                        return True
                    visited[v] = True
                    q.append((v, source)) # append child with current node as parent
            return False
        count=0
        for u in range(n):
            if visited[u]!=True: # if not visited, then new component
                count+=1 # count connected components, if more than 1 then not a tree
                if bfsCycle(u):
                    return False
        if count>1: # if more than 1 connected component then not a tree
            return False
        return True