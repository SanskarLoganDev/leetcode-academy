# 104. MAXIMUM DEPTH OF BINARY TREE

# Neetcode 150 (Important)

# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Example 2:
# Input: root = [1,null,2]
# Output: 2

# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            return 1+max(left,right)
        return dfs(root)

# Example explanation:

#             1
#          /     \
#         2       3
#        / \       \
#       4   5       6
#          / \     / \
#         7   8   9  10
#              \
#              11

# dfs(1)
#   dfs(2)
#     dfs(4)
#       dfs(None) -> 0
#       dfs(None) -> 0
#       return 1 + max(0, 0) = 1          # depth at node 4
#     dfs(5)
#       dfs(7)
#         dfs(None) -> 0
#         dfs(None) -> 0
#         return 1 + max(0, 0) = 1        # depth at node 7
#       dfs(8)
#         dfs(None) -> 0
#         dfs(11)
#           dfs(None) -> 0
#           dfs(None) -> 0
#           return 1 + max(0, 0) = 1      # depth at node 11
#         return 1 + max(0, 1) = 2        # depth at node 8
#       return 1 + max(1, 2) = 3          # depth at node 5 (via 5→8→11)
#     return 1 + max(1, 3) = 4            # depth at node 2 (via 2→5→8→11)

#   dfs(3)
#     dfs(None) -> 0
#     dfs(6)
#       dfs(9)
#         dfs(None) -> 0
#         dfs(None) -> 0
#         return 1 + max(0, 0) = 1        # depth at node 9
#       dfs(10)
#         dfs(None) -> 0
#         dfs(None) -> 0
#         return 1 + max(0, 0) = 1        # depth at node 10
#       return 1 + max(1, 1) = 2          # depth at node 6
#     return 1 + max(0, 2) = 3            # depth at node 3 (via 3→6→9/10)

# return 1 + max(4, 3) = 5                # depth at node 1 (overall answer)

# same as above but one liner
from typing import Optional
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))
    
# using bfs


from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([root])
        level = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level+=1
        return level

# using iterative dfs
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        res = 0
        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])

        return res
        