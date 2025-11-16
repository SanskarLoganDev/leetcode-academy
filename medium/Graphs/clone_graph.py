# 133. Clone Graph
# Neetcode 150

# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.

# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }
 

# Test case format:

# For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

# An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

# The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

# Example 1:

# Image: https://assets.leetcode.com/uploads/2019/11/04/133_clone_graph_question.png
# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]
# Explanation: There are 4 nodes in the graph.
# 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

# Example 2:

# Input: adjList = [[]]
# Output: [[]]
# Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

# Example 3:

# Input: adjList = []
# Output: []
# Explanation: This an empty graph, it does not have any nodes.
 

# Constraints:

# The number of nodes in the graph is in the range [0, 100].
# 1 <= Node.val <= 100
# Node.val is unique for each node.
# There are no repeated edges and no self-loops in the graph.
# The Graph is connected and all nodes can be visited starting from the given node.



# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# time complexity: O(N + M) where N is number of nodes and M is number of edges:
# Each original node is enqueued/dequeued once → O(N).

# For each node, you iterate over its neighbors. Across the whole traversal, each (undirected) edge is seen at most twice → O(M).

# space complexity: O(N) for the hashmap and the recursion stack
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: # Handle empty input
            return None
        clone_node = Node(node.val) # create clone of the starting node, 
        # clone_node will be the current pointer to the cloned graph
        self.mp = {} # to map original node to cloned node
        self.mp[node] = clone_node # map original node to its clone, storing the inital clone in a list to avoid overwriting in case of multiple references

        def dfs(node, clone_node):
            for n in node.neighbors:
                if n not in self.mp: # if neighbor not cloned yet
                    clone = Node(n.val)
                    self.mp[n]=clone # map original neighbor to its clone
                    clone_node.neighbors.append(clone) # add the cloned neighbor to the current cloned node's neighbors
                    dfs(n, clone) # DFS on the neighbor and the neighbor's clone (new current pointer)
                else:
                    clone_node.neighbors.append(self.mp[n]) # if already cloned, just add the reference to the cloned neighbor
        dfs(node, clone_node)

        return clone_node
    
# Using BFS

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# time complexity: O(N + M) where N is number of nodes and M is number of edges:
# Each original node is enqueued/dequeued once → O(N).

# For each node, you iterate over its neighbors. Across the whole traversal, each (undirected) edge is seen at most twice → O(M).


# space complexity: O(N) for the hashmap and the recursion stack
from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        clone_node = Node(node.val)
        mp = {}
        mp[node] = clone_node
        q = deque([node])
        while q:
            nodeq = q.popleft() # nodeq is the current node from original graph
            clone_nodeq = mp[nodeq] # clone_nodeq is the corresponding cloned node
            for n in nodeq.neighbors:
                if n not in mp:
                    clone = Node(n.val)
                    mp[n] = clone
                    clone_nodeq.neighbors.append(clone) # add the cloned neighbor to the current cloned node's neighbors
                    q.append(n)
                else:
                    clone_nodeq.neighbors.append(mp[n]) # if already cloned, just add the reference to the cloned neighbor

        return clone_node