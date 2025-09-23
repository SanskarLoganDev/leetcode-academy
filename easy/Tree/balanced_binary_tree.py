# 110. Balanced Binary Tree
# Neetcode 150 (Important)

# Given a binary tree, determine if it is height-balanced.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: true

# Example 2:
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false

# Example 3:
# Input: root = []
# Output: true

# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from typing import Optional        
class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        self.flag = True
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if abs(left-right)>1:
                self.flag= False
            return 1+max(left, right)
        dfs(root)
        return self.flag

# Important obervation:
# use the depth function to allow for recursion adn have a global flag to check if the tree is balanced or not and ultimately return that, in the same way as diameter of binary tree problem where we used a global variable to store the diameter and returned that at the end. Here we use a global flag to check if the tree is balanced or not and return that at the end.