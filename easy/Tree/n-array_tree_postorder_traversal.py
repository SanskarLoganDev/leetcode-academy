# 590. N-ARRAY TREE POSTORDER TRAVERSAL
# Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

# Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

# Example 1:

# Input: root = [1,null,3,2,4,null,5,6]
# Output: [5,6,3,2,4,1]

# Example 2:

# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]

"""
# Definition for a Node.
class Node(object):
	def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        elements = []
        if root is None:
            return []
        for child in root.children: # here since children is a list, you have to go one by one for each child in children at that level
            elements+=self.postorder(child)
        elements.append(root.val)
        return elements
    
# Let’s walk through the code with Example 1:

# Tree Structure:
# markdown
# Copy
#          1
#        / | \
#       3  2  4
#      / \
#     5   6
# Step-by-Step Execution:
# Call postorder(root) where root is node 1:

# elements = [] is initialized.
# Node 1 is not None, so we proceed to the loop.
# root.children is the list: [node 3, node 2, node 4].
# Process First Child: Node 3

# Call postorder(node 3).

# For node 3, initialize elements = [].
# Its children: [node 5, node 6].
# 2.1 Process Child of Node 3: Node 5 - Call postorder(node 5). - Node 5 has no children.
# - Base case: returns [] for children. - Append node 5's value: elements = [5]. - Return [5].

# 2.2 Process Next Child of Node 3: Node 6 - Call postorder(node 6). - Node 6 has no children. - Append node 6's value: elements = [6]. - Return [6].

# 2.3 At Node 3, after Processing Children: - Now, for node 3, elements is extended by the results from its children: - Start with elements = []. - Extend with [5] → elements = [5]. - Extend with [6] → elements = [5, 6]. - Append node 3's value: elements = [5, 6, 3]. - Return [5, 6, 3].

# Process Second Child: Node 2

# Call postorder(node 2).
# Node 2 has no children.
# Base Case:
# Initialize elements = [], then append node 2's value: elements = [2].
# Return [2].
# Process Third Child: Node 4

# Call postorder(node 4).
# Node 4 has no children.
# Initialize elements = [], append node 4's value: elements = [4].
# Return [4].
# At the Root Node (Node 1):

# Start with elements = [].
# Process children one by one:
# First child (node 3) returns [5, 6, 3] → now, elements = [5, 6, 3].
# Second child (node 2) returns [2] → now, elements = [5, 6, 3, 2].
# Third child (node 4) returns [4] → now, elements = [5, 6, 3, 2, 4].
# Append the root node's value (node 1) → elements = [5, 6, 3, 2, 4, 1].
# Final Result:

# The method returns [5, 6, 3, 2, 4, 1], which is the postorder traversal of the tree.