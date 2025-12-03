# 547. Number of Provinces

# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.

# Example 1:

# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2

# Example 2:

# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
 
# Constraints:

# 1 <= n <= 200
# n == isConnected.length
# n == isConnected[i].length
# isConnected[i][j] is 1 or 0.
# isConnected[i][i] == 1
# isConnected[i][j] == isConnected[j][i]

# time complexity: O(N^2)
# space complexity: O(N^2) for adjacency list

from typing import List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False]*n # to keep track of visited nodes
        adj = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i==j:
                    continue
                if isConnected[i][j]==1:
                    adj[i].append(j)

        def DFS(adj, u, visited, parent):
            visited[u]=True
            for v in adj[u]:
                if v == parent: # we don't want to go back to parent
                    continue
                if visited[v]==True:
                    continue # we continue instead of returning because we want to visit all nodes in this component
                DFS(adj, v, visited, u)
            return
        count = 0
        for u in range(n):
            if visited[u]!=True:
                DFS(adj, u, visited, -1) # we pass -1 as parent of starting node
                count+=1 # we increase count when we start a new DFS, meaning we found a new province
        
        return count