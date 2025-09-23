# 100. Same Tree
# Neetcode 150 (Important)

# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Example 1:

# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Example 2:

# Input: p = [1,2], q = [1,null,2]
# Output: false

# Example 3:

# Input: p = [1,2,1], q = [1,1,2]
# Output: false
 
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if p is None and q is None:
            return True
        # If only one of the nodes is None, they are not identical
        if p is None or q is None:
            return False
        # Check if values are equal and recursively check left and right subtrees
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # Values are not equal, they are not identical that is for handling p.val!=q.val
        return False
        
# Example 1:
# Input:
# p = [1,2,3], q = [1,2,3]

# Tree Structures:

# css
# Copy
#     p:       1           q:     1
#            /   \              /   \
#           2     3            2     3
# Execution:

# Compare root: 1 == 1 → Continue.
# Compare left subtrees: p.left.val = 2 and q.left.val = 2.
# Both have no children → Return True.
# Compare right subtrees: p.right.val = 3 and q.right.val = 3.
# Both have no children → Return True.
# Since both left and right comparisons are True, overall result is True.
# Example 2:
# Input:
# p = [1,2], q = [1,null,2]

# Tree Structures:

# css
# Copy
#     p:       1            q:  1
#            /                  \
#           2                    2
# Execution:

# Compare root: 1 == 1 → Continue.
# Compare left subtrees:
# For p: p.left is node 2.
# For q: q.left is None.
# The condition if p is None or q is None: is met → Return False.
# Function returns False.

# an alternate solution but above one is cleaner

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.flag = True
        def dfs(node1, node2):
            if not node1 and not node2:
                return 0
            if not node1 or not node2:
                self.flag = False
                return 0
            if node1.val!=node2.val:
                self.flag = False
                return 0
            left = dfs(node1.left, node2.left)
            right = dfs(node1.right, node2.right)

            return 1+max(left,right)
        dfs(p,q)
        return self.flag
