# 102. Binary Tree Level Order Traversal
# Neetcode 150 (Important)

# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

# Example 2:

# Input: root = [1]
# Output: [[1]]

# Example 3:

# Input: root = []
# Output: []
 
# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# time complexity: O(N) where N is the number of nodes in the tree        
# space complexity: O(N) where N is the number of nodes in the tree

from typing import List, Optional
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:                # empty tree ⇒ no levels
            return []
        q = deque([root])           # FIFO queue, start with root
        levels = []                 # final [[level1], [level2], ...]
        while q:                    # each loop processes ONE level
            size = len(q)           # how many nodes are currently in this level
            cur = []                # values for this level
            for _ in range(size):   # pop exactly 'size' nodes
                node = q.popleft()  # take next node in this level
                cur.append(node.val)
                if node.left:       # enqueue children for NEXT level
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            levels.append(cur)      # finish level
        return levels
    
# Example:    
#         1
#       /   \
#      2     3
#     / \     \
#    4   5     6
#       / \
#      7   8
# Expected output: [[1], [2, 3], [4, 5, 6], [7, 8]]

# Step-by-step queue trace
# I’ll show the queue (q) before each level, then what we pop/push.

# Level 0
# Start: q = [1], levels = []

# size = 1

# Pop 1 → cur = [1]

# Enqueue children: push 2, 3 → q = [2, 3]

# End level: levels = [[1]]

# Level 1
# q = [2, 3]

# size = 2

# Pop 2 → cur = [2]

# push 4, 5 → q = [3, 4, 5]

# Pop 3 → cur = [2, 3]

# push (right) 6 → q = [4, 5, 6]

# End level: levels = [[1], [2, 3]]

# Level 2
# q = [4, 5, 6]

# size = 3

# Pop 4 → cur = [4] (no kids)

# Pop 5 → cur = [4, 5]

# push 7, 8 → q = [6, 7, 8]

# Pop 6 → cur = [4, 5, 6] (no kids)

# End level: levels = [[1], [2, 3], [4, 5, 6]]

# Level 3
# q = [7, 8]

# size = 2

# Pop 7 → cur = [7]

# Pop 8 → cur = [7, 8]

# End level: levels = [[1], [2, 3], [4, 5, 6], [7, 8]]

# q empty ⇒ stop

# Return [[1], [2, 3], [4, 5, 6], [7, 8]].