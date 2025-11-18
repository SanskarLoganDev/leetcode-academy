# 1791. Find Center of Star Graph

# There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

# You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.

 

# Example 1:


# Input: edges = [[1,2],[2,3],[4,2]]
# Output: 2
# Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.
# Example 2:

# Input: edges = [[1,2],[5,1],[1,3],[1,4]]
# Output: 1
 

# Constraints:
# 3 <= n <= 105
# edges.length == n - 1
# edges[i].length == 2
# 1 <= ui, vi <= n
# ui != vi
# The given edges represent a valid star graph.

# My solution O(N):

from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges)+1 # n is number of nodes
        indegree = [0]*(n+1) # since nodes are 1 indexed to n. Indegree is number of edges coming into a node
        outdegree = [0]*(n+1) # outdegree is number of edges going out of a node
         # in a star graph, the center node will have indegree + outdegree = n-1 as it is connected to every other node
        for a, b in edges:
            outdegree[a]+=1
            indegree[b]+=1
        for i in range(1, n+1):
            if outdegree[i]+indegree[i]==n-1:
                return i
        return -1
    
# Sometimes best solution is the simplest one
# the centre has to be a part of every pair, so we just compare the 1st and second pair and return the common element
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if edges[0][0] in edges[1]: # check if first element of first pair is in second pair
            return edges[0][0] 
        return edges[0][1]