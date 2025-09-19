# 543. DIAMETER OF BINARY TREE
# Neetcode 150 (Important)

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
        self.res = 0 # used for calculating diameter, we have added self. to res so that we can access it from inside another function
        def dfs(node): # Returns height and not diameter
            if not node:
                return 0
            left = dfs(node.left) # Length of left path
            right = dfs(node.right) # Length of right path
            self.res = max(self.res, left+right) # This is the diameter, this is the main thing that needs to be returned
            
            return 1+max(left,right) # add one to get length upto current node. This is not returned but required for moving forward in the tree

        dfs(root)
        return self.res

# Example explanation:

    #         1
    #      /     \
    #     2       3
    #    / \       \
    #   4   5       6
    #      / \     / \
    #     7   8   9  10
    #          \
    #          11

# dfs(1)
#   dfs(2)
#     dfs(4)
#       dfs(None) -> 0
#       dfs(None) -> 0
#       self.res = max(0, 0+0) = 0
#       return 1
#     dfs(5)
#       dfs(7)
#         dfs(None) -> 0
#         dfs(None) -> 0
#         self.res = max(0, 0+0) = 0
#         return 1
#       dfs(8)
#         dfs(None) -> 0
#         dfs(11)
#           dfs(None) -> 0
#           dfs(None) -> 0
#           self.res = max(0, 0+0) = 0
#           return 1
#         self.res = max(0, 0+1) = 1        # through node 8 (to 11)
#         return 1 + max(0,1) = 2
#       self.res = max(1, 1+2) = 3          # through node 5 (7–5–8–11)
#       return 1 + max(1,2) = 3
#     self.res = max(3, 1+3) = 4            # through node 2 (4–2–5–8–11)
#     return 1 + max(1,3) = 4

#   dfs(3)
#     dfs(None) -> 0
#     dfs(6)
#       dfs(9)
#         dfs(None) -> 0
#         dfs(None) -> 0
#         self.res = max(4, 0+0) = 4
#         return 1
#       dfs(10)
#         dfs(None) -> 0
#         dfs(None) -> 0
#         self.res = max(4, 0+0) = 4
#         return 1
#       self.res = max(4, 1+1) = 4          # through node 6
#       return 1 + max(1,1) = 2
#     self.res = max(4, 0+2) = 4            # through node 3
#     return 1 + max(0,2) = 3

# self.res = max(4, 4+3) = 7                # through node 1 (11 … 10)
# return 1 + max(4,3) = 5                   # height of whole tree (unused)



        