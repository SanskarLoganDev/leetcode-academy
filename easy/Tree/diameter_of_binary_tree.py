# 543. DIAMETER OF BINARY TREE

# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.


# Example 1:


# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
# Example 2:

# Input: root = [1,2]
# Output: 1

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # here we use self so that we can access it from inside another function
        self.res = 0 # used for calculating diameter
        def dfs(node): # Returns height and not diameter
            if not node:
                return 0
            left = dfs(node.left) # Length of left path
            right = dfs(node.right) # Length of right path
            self.res = max(self.res, left+right) # This is the diameter
            
            return 1+max(left,right) # add one to get length upto current node

        dfs(root)
        return self.res


        


        