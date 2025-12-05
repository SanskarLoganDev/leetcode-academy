# 207. Course Schedule
# Neetcode 150 (Important)
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.

# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

# Constraints:

# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.

from typing import List
from collections import deque

# time complexity: O(V+E)
# space complexity: O(V+E) for adjacency list

# Using BFS Kahn's algorithm for topological sort
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # It is a problem of cycle detection in directed graph
        # if topological sort of DG is possible then there is no graph
        # BFS Kahn's algorithm
        adj = [[] for _ in range(numCourses)]
        stack = []
        indegree = [0]*numCourses
        for v, u in prerequisites:
            adj[u].append(v)
            indegree[v]+=1

        def bfs_kahns(stack, adj, indegree):
            q = deque()
            for i in range(numCourses):
                if indegree[i]==0:
                    stack.append(i) # add to stack as it can be completed (add to topological sort)
                    q.append(i) # add all nodes with indegree 0 to queue and stack

            while q:
                u = q.popleft()
                for v in adj[u]:
                    indegree[v]-=1 # decrease indegree of all neighbors
                    if indegree[v]==0:
                        q.append(v)
                        stack.append(v) # add to stack as it can be completed


        bfs_kahns(stack, adj, indegree) # perform BFS Kahn's algorithm
        return len(stack)==numCourses # if stack size is equal to numCourses then all courses can be completed

# Using the concept of topological sort with DFS
# time complexity: O(V+E)
# space complexity: O(V+E) for adjacency list + O(V) for recursion stack
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # It is a problem of cycle detection in directed graph
        # if topological sort of DG is possible then there is no graph
        # DFS
        adj = [[] for _ in range(numCourses)]
        inRecursion = [False]*numCourses # to keep track of nodes in current recursion stack
        visited = [False]*numCourses # to keep track of visited nodes
        for v, u in prerequisites:
            adj[u].append(v)

        def dfs(u, inRecursion, adj, visited):
            visited[u]=True
            inRecursion[u]=True
            for v in adj[u]:
                if visited[v]==False and dfs(v, inRecursion, adj, visited): # if visited[v] is False and a cycle is found in DFS in subtree
                    return True
                if inRecursion[v]==True: # if v is already in recursion stack then a cycle is found. This part of code is only reached if visited[v] is True
                    return True
            inRecursion[u]=False

        for u in range(numCourses):
            if visited[u]!=True and dfs(u, inRecursion, adj, visited):
                return False

        return True
