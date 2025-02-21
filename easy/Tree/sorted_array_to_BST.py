# 108. CONVERT SORTED ARRAY TO BINARY SEARCH TREE
# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

# Example 1:
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:

# Example 2:
# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        if not nums:
            return None
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
    
# Example 1: nums = [-10, -3, 0, 5, 9]

# Initial Call:

# nums = [-10, -3, 0, 5, 9]
# mid = 5 // 2 = 2
# root = TreeNode(0)
# Left subtree call: nums[:2] = [-10, -3]
# Right subtree call: nums[3:] = [5, 9]
# Left Subtree ([-10, -3]):

# mid = 2 // 2 = 1
# root = TreeNode(-3)
# Left subtree call: [-10]
# Right subtree call: []
# For [-10]: mid = 0, create node -10, both subtrees are empty → returns TreeNode(-10)
# Right subtree: returns None
# So left subtree becomes:
# markdown
# Copy
#     -3
#    /
#  -10
# Right Subtree ([5, 9]):

# mid = 2 // 2 = 1
# root = TreeNode(9)
# Left subtree call: [5]
# Right subtree call: []
# For [5]: mid = 0, create node 5, both subtrees are empty → returns TreeNode(5)
# Right subtree: returns None
# So right subtree becomes:
# markdown
# Copy
#     9
#    /
#   5
# Final BST Structure:

# markdown
# Copy
#          0
#         / \
#      -3     9
#      /     /
#    -10    5
# This tree is height-balanced and is a valid BST.
