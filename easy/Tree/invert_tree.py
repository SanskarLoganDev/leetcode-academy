# 226. INVERT BINARY TREE 
# Given the root of a binary tree, invert the tree, and return its root.

# Example 1:
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

# Example 2:
# Input: root = [2,1,3]
# Output: [2,3,1]

# Example 3:
# Input: root = []
# Output: []

class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None
        self.invertTree(root.left)
        self.invertTree(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp
        return root
    
# Let's use Example 1:

# Input Tree (before inversion):

# markdown
# Copy
#        4
#       / \
#      2   7
#     / \ / \
#    1  3 6  9
# Step-by-Step Process:
# Start at Root (Node 4):

# Call invertTree(4).
# Since node 4 is not None, proceed with recursive calls.
# Invert Left Subtree of 4 (Node 2):

# Call invertTree(2).
# For node 2, recursively invert its left and right subtrees.
# 2.1. Invert Left Subtree of 2 (Node 1): - Call invertTree(1). - Node 1 is a leaf (both children are None): - The recursive calls on 1.left and 1.right return 0 (or None). - No swap is needed. - Return node 1.

# 2.2. Invert Right Subtree of 2 (Node 3): - Call invertTree(3). - Node 3 is also a leaf: - Both children are None, so nothing changes. - Return node 3.

# 2.3. Swap Children at Node 2: - After inverting both subtrees, node 2's left child is still node 1 and right child is node 3. - Swap:
# - Now, node 2.left becomes node 3, and node 2.right becomes node 1. - Subtree at Node 2 becomes: 2 / \ 3 1

# Invert Right Subtree of 4 (Node 7):

# Call invertTree(7).
# For node 7, recursively invert its left and right subtrees.
# 3.1. Invert Left Subtree of 7 (Node 6): - Call invertTree(6). - Node 6 is a leaf; its children are None. - Return node 6.

# 3.2. Invert Right Subtree of 7 (Node 9): - Call invertTree(9). - Node 9 is a leaf; its children are None. - Return node 9.

# 3.3. Swap Children at Node 7: - After inverting, node 7.left is node 6 and node 7.right is node 9. - Swap:
# - Now, node 7.left becomes node 9, and node 7.right becomes node 6. - Subtree at Node 7 becomes: 7 / \ 9 6

# Swap Children at Root (Node 4):

# Now, the left subtree of node 4 is the inverted subtree rooted at node 2:
# Copy
#    2
#   / \
#  3   1
# The right subtree of node 4 is the inverted subtree rooted at node 7:
# Copy
#    7
#   / \
#  9   6
# Swap at Node 4:
# Node 4.left becomes node 7 (inverted right subtree) and node 4.right becomes node 2 (inverted left subtree).
# Final Inverted Tree:

# markdown
# Copy
#        4
#       / \
#      7   2
#     / \ / \
#    9  6 3  1
# Output:
# The root of the inverted tree (node 4) is returned, representing the tree above.