# 210. Course Schedule II
# Neetcode 150 (Important)

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

# Example 2:

# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

# Example 3:

# Input: numCourses = 1, prerequisites = []
# Output: [0]
 

# Constraints:

# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= numCourses * (numCourses - 1)
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# ai != bi
# All the pairs [ai, bi] are distinct.

from typing import List
from collections import deque

# time complexity: O(V+E)
# space complexity: O(V+E) for adjacency list

# Using BFS Kahn's algorithm for topological sort
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        stack = []
        indegree = [0]*numCourses # indegree array
        for v, u in prerequisites:
            adj[u].append(v)
            indegree[v]+=1 # calculate indegree of each node

        def bfs(adj, stack, indegree):
            q = deque()
            for i in range(numCourses): # add all nodes with indegree 0 to queue
                if indegree[i]==0:
                    q.append(i)
                    stack.append(i) # add to stack as it can be completed (add to topological sort)
            
            while q:
                u = q.popleft()
                for v in adj[u]:
                    indegree[v]-=1
                    if indegree[v]==0:
                        q.append(v)
                        stack.append(v)
            return stack


        bfs(adj, stack, indegree)
        if len(stack)!=numCourses: # if stack size is not equal to numCourses then there is a cycle
            return []
        else:
            return stack
    
# Combining logic of cycle detection in directed graph using DFS and topological sort    

# time complexity: O(V+E)
# space complexity: O(V+E) for adjacency list
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        stack = []
        visited = [False]*numCourses
        inRecursion = [False]*numCourses # to keep track of nodes in current recursion stack
        for v, u in prerequisites:
            adj[u].append(v)

        def dfs(u):
            visited[u] = True
            inRecursion[u]= True
            for v in adj[u]:
                if visited[v]==False and dfs(v): # if cycle is detected and v is not visited
                    return True
                elif inRecursion[v] == True: # if v is in current recursion stack then cycle is detected. This part of the code is only reached if v is already visited
                    return True
            inRecursion[u]=False # remove u from recursion stack
            stack.append(u) # add to stack as it can be completed (add to topological sort)
            return False

        for u in range(numCourses):
            if visited[u]!=True and dfs(u): # if cycle is detected and u is not visited
                return []
        return stack[::-1] # return reverse of stack to get correct topological order