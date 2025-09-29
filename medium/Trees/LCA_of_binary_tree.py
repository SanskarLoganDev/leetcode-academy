# 236. Lowest Common Ancestor of a Binary Tree
# Neetcode 150 (Important)

# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Example 1:

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.

# Example 2:

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

# Example 3:

# Input: root = [1,2], p = 1, q = 2
# Output: 1

# Constraints:

# The number of nodes in the tree is in the range [2, 105].
# -109 <= Node.val <= 109
# All Node.val are unique.
# p != q
# p and q will exist in the tree.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# time complexity: O(N) where N is the number of nodes in the tree
# space complexity: O(H) where H is the height of the tree
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root==p or root==q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left!=None and right!=None:
            return root
        if left!=None:
            return left
        return right
    
# Brute force approach
# time complexity: O(N) where N is the number of nodes in the tree
# space complexity: O(N)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # build path from target up to root by appending on unwind (nearest-first)
        def dfs(node: 'TreeNode', target: 'TreeNode', acc: list) -> bool:
            if not node:
                return False
            if node is target:            # use identity, not value
                acc.append(node)          # include the target itself
                return True
            if dfs(node.left, target, acc) or dfs(node.right, target, acc):
                acc.append(node)          # append ancestor on the way back up
                return True               # <— propagate True so parents can append
            return False

        path_p, path_q = [], []
        dfs(root, p, path_p)
        dfs(root, q, path_q)

        # path_p and path_q are [target, parent, grandparent, ..., root]
        seen = set(path_p)                # TreeNode objects are hashable by identity
        for node in path_q:               # scan q's path from lowest upward
            if node in seen:
                return node               # first intersection is the LCA
        return None                       # (shouldn't happen if p,q are in the tree)

            