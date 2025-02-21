# 101. SYMMETRIC TREE
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Example 1:

# Input: root = [1,2,2,3,4,4,3]
# Output: true

# Example 2:

# Input: root = [1,2,2,null,3,null,3]
# Output: false

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root): # in this problem we are traversing both the branches at the same time
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def isMirror(left_node, right_node): # here left_node refers to left branch and right_node is right branch
            if left_node is None and right_node is None:
                return True
            if left_node is None or right_node is None:
                return False
            return (left_node.val==right_node.val) and (isMirror(left_node.left, right_node.right)) and (isMirror(left_node.right, right_node.left))
        return isMirror(root.left, root.right)