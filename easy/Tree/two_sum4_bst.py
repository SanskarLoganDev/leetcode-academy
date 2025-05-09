# 653. Two Sum IV - Input is a BST

# Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.

 

# Example 1:

# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true

# Example 2:

# Input: root = [5,3,6,2,4,null,7], k = 28
# Output: false

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        seen = set()
        def inorder(node):
            if not node:
                return False
            if (k-node.val) in seen:
                return True
            seen.add(node.val)
            return inorder(node.left) or inorder(node.right)
            
        return inorder(root)

        
        
 