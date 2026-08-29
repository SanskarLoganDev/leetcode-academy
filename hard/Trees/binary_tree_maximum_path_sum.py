# 124. Binary Tree Maximum Path Sum
# Neetcode 150 (Important)
# Difficulty: Hard

# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

# The path sum of a path is the sum of the node's values in the path.

# Given the root of a binary tree, return the maximum path sum of any non-empty path.

 

# Example 1:
# https://assets.leetcode.com/uploads/2020/10/13/exx1.jpg
# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

# Example 2:
# https://assets.leetcode.com/uploads/2020/10/13/exx2.jpg
# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 3 * 104].
# -1000 <= Node.val <= 1000

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from typing import Optional

# time complexity: O(N) where N is the number of nodes in the tree
# The only extra space is the recursion stack.
# space complexity: O(H) where H is the height of the tree
# In the worst case, the tree is skewed and the height is O(N).

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = root.val

        def dfs(node):
            if not node:
                return 0 # if no node, then sum is 0

            left = dfs(node.left)
            right = dfs(node.right)

            both_are_good = left + right + node.val # Case 1: if both left and right below return good values

            only_one_good = max(left, right) + node.val # Case 2: if either left or right is good

            neither_good = node.val # Case 3: both left and right are bad results

            self.maxSum = max(self.maxSum, both_are_good, only_one_good, neither_good)

            # most important part: when returning to parent, we can only choose one path (either left or right)
            # We cannot return both paths to parent because that would form a fork which is not allowed in a path
            return max(only_one_good, neither_good)
        
        dfs(root)
        return self.maxSum

