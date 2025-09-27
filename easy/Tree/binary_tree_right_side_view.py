# 199. Binary Tree Right Side View

# Neetcode 150 (Important)

# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Example 1:
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
# Explanation: https://assets.leetcode.com/uploads/2024/11/24/tmpd5jn43fs-1.png

# Example 2:
# Input: root = [1,2,3,4,null,null,null,5]
# Output: [1,3,4,5]
# Explanation: https://assets.leetcode.com/uploads/2024/11/24/tmpkpe40xeh-1.png

# Example 3:
# Input: root = [1,null,3]
# Output: [1,3]
# Example 4:
# Input: root = []
# Output: []

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from typing import List, Optional
from collections import deque

# Used BFS to solve this problem

# time complexity: O(N) where N is the number of nodes in the tree
# space complexity: O(W) where W is the maximum width of the tree

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([root])
        out = []
        while q:
            curr = []
            for _ in range(len(q)):
                node = q.popleft()
                curr.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            out.append(curr[-1])
        return out