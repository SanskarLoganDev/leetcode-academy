# 98. Validate Binary Search Tree
# Neetcode 150 (Important)

# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys strictly less than the node's key.
# The right subtree of a node contains only nodes with keys strictly greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 

# Example 1:

# Input: root = [2,1,3]
# Output: true

# Example 2:

# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
 
# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from typing import Optional

# time complexity: O(n)
# space complexity: O(n) in worst case for skewed tree, O(log n) or O(h) for balanced tree

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode], low: int, high: int):
            if not node:
                return True
            if not low<node.val<high: # here we have not used return True because if we do that then it will return True for left and right subtree even if one of them is False
                return False # So: we use if not ...: return False to only short-circuit on failure; we don’t return True until both subtrees have been verified as well.
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
        return dfs(root, float("-inf"), float("inf"))