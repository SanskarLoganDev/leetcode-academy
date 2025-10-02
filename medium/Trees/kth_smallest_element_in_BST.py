# 230. Kth Smallest Element in a BST
# Neetcode 150 (Important)

# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree. 

# Example 1:
# https://assets.leetcode.com/uploads/2021/01/28/kthtree1.jpg
# Input: root = [3,1,4,null,2], k = 1
# Output: 1

# Example 2:
# https://assets.leetcode.com/uploads/2021/01/28/kthtree2.jpg
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
 

# Constraints:

# The number of nodes in the tree is n.
# 1 <= k <= n <= 104
# 0 <= Node.val <= 104
 

# Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
import heapq
from typing import Optional

# Time complexity O((n + k) log n), which simplifies to O(n log n) since k ≤ n
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def bfs(node):
            heap = []
            q = [node]
            while q: # O(n) for n nodes
                n = q.pop()
                heapq.heappush(heap, n.val) # O(log n) operation for heap push
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            return heap
        res = bfs(root)
        for _ in range(k-1): # O(k) for k iterations
            heapq.heappop(res) # O(log n) operation for heap pop
        return heapq.heappop(res)
