# 105. Construct Binary Tree from Preorder and Inorder Traversal
# Neetcode 150 (Important)

# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

# Example 1:
# https://assets.leetcode.com/uploads/2021/02/19/tree.jpg
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]

# Example 2:

# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
 
# Constraints:

# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from typing import List, Optional

# time complexity: O(N) where N is the number of nodes in the tree
# space complxity: Auxiliary space: O(N) for the recursion stack

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.idx = 0 # to keep track of the index in preorder array
        def traversal(preorder, inorder, start, end):
            if start>end: # no nodes/ leaf node reached
                return
            rootVal = preorder[self.idx]
            i = start
            while True:
                if (inorder[i] == rootVal):
                    break
                i+=1 # find the index of rootVal in inorder array
            self.idx+=1 # increment the index in preorder array to point to the next root node
            root = TreeNode(rootVal)
            root.left = traversal(preorder, inorder, start, i-1) # elements to the left of i in inorder array belong to the left subtree
            root.right = traversal(preorder, inorder, i+1, end) # elements to the right of i in inorder array belong to the right subtree

            return root
        return traversal(preorder, inorder, 0, len(inorder)-1)
    
# Exammple usage:

# Example

# preorder = [3, 9, 20, 15, 7]
# inorder = [9, 3, 15, 20, 7]

# Call / return trace

# I’ll write each call as traversal(start,end) and show:
# idx (position in preorder) before reading the root
# chosen rootVal = preorder[idx]
# found index i in inorder
# the left and right ranges for the next calls
# when a subtree returns, what node it returns

# Start: self.idx = 0
# Call traversal(0, 4)
#   idx=0 → rootVal=3
#   inorder index i=1 (inorder[1]=3)
#   self.idx ← 1
#   build node(3)
#   ├─ Call traversal(0, 0)        # left: inorder[0..0]
#   │    idx=1 → rootVal=9
#   │    i=0
#   │    self.idx ← 2
#   │    build node(9)
#   │    ├─ Call traversal(0, -1)  # left empty → return None
#   │    └─ Call traversal(1, 0)   # right empty → return None
#   │    Return node(9)
#   └─ Call traversal(2, 4)        # right: inorder[2..4]
#        idx=2 → rootVal=20
#        i=3
#        self.idx ← 3
#        build node(20)
#        ├─ Call traversal(2, 2)   # left: inorder[2..2]
#        │    idx=3 → rootVal=15
#        │    i=2
#        │    self.idx ← 4
#        │    build node(15)
#        │    ├─ Call traversal(2, 1)  # empty → None
#        │    └─ Call traversal(3, 2)  # empty → None
#        │    Return node(15)
#        └─ Call traversal(4, 4)   # right: inorder[4..4]
#             idx=4 → rootVal=7
#             i=4
#             self.idx ← 5
#             build node(7)
#             ├─ Call traversal(4, 3)  # empty → None
#             └─ Call traversal(5, 4)  # empty → None
#             Return node(7)
#        Return node(20) with left=15, right=7
# Return node(3) with left=9, right=20
        