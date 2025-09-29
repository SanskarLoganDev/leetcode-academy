# 1448. Count Good Nodes in Binary Tree
# Neetcode 150 (Important)

# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

# Return the number of good nodes in the binary tree.

# Example 1:
# https://assets.leetcode.com/uploads/2020/04/02/test_sample_1.png
# Input: root = [3,1,4,3,null,1,5]
# Output: 4
# Explanation: Nodes in blue are good.
# Root Node (3) is always a good node.
# Node 4 -> (3,4) is the maximum value in the path starting from the root.
# Node 5 -> (3,4,5) is the maximum value in the path
# Node 3 -> (3,1,3) is the maximum value in the path.

# Example 2:
# https://assets.leetcode.com/uploads/2020/04/02/test_sample_2.png
# Input: root = [3,3,null,4,2]
# Output: 3
# Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

# Example 3:

# Input: root = [1]
# Output: 1
# Explanation: Root is considered as good.
 
# Constraints:

# The number of nodes in the binary tree is in the range [1, 10^5].
# Each node's value is between [-10^4, 10^4].

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# time complexity: O(N) where N is the number of nodes in the tree
# space complexity: O(H) where H is the height of the tree

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxVal):
            if not node:
                return 0
            if node.val>=maxVal: # here we use >= because if the value is same as maxVal then also it is a good node
                res = 1
            else:
                res = 0
            maxVal = max(maxVal, node.val)
            res+= dfs(node.left, maxVal) # we pass the updated maxVal to the left and right subtree
            res+= dfs(node.right, maxVal)
            return res
        return dfs(root, root.val) # we can also choose float("-inf") here but root.val will woek as well
    
    
# Example explanation:

#             3
#           /   \
#          1     4
#         / \     \
#        3   2     5
#           /
#          4

# dfs(3, 3)                          # 3 >= 3 → GOOD (res=1), maxVal stays 3
#   dfs(1, 3)                        # 1 < 3  → BAD  (res=0), maxVal stays 3
#     dfs(3, 3)                      # 3 >= 3 → GOOD (res=1), maxVal=3
#       dfs(None, 3) → 0
#       dfs(None, 3) → 0
#       return 1
#     dfs(2, 3)                      # 2 < 3  → BAD  (res=0), maxVal=3
#       dfs(4, 3)                    # 4 >= 3 → GOOD (res=1), maxVal becomes 4
#         dfs(None, 4) → 0
#         dfs(None, 4) → 0
#         return 1
#       dfs(None, 3) → 0
#       return 1                     # from node 2: 0 (self) + 1 (left) + 0 (right)
#     return 2                       # from node 1: 0 + 1 + 1
#   dfs(4, 3)                        # 4 >= 3 → GOOD (res=1), maxVal becomes 4
#     dfs(1, 4)                      # 1 < 4  → BAD  (res=0), maxVal=4
#       dfs(None, 4) → 0
#       dfs(None, 4) → 0
#       return 0
#     dfs(5, 4)                      # 5 >= 4 → GOOD (res=1), maxVal becomes 5
#       dfs(None, 5) → 0
#       dfs(None, 5) → 0
#       return 1
#     return 2                       # from node 4(right): 1 (self) + 0 + 1
# return 5                           # root: 1 (self) + 2 (left) + 2 (right)
