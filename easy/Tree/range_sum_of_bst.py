# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

# Example 1:


# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32
# Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
# Example 2:


# Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# Output: 23
# Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.

# Brute Force solution

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: int
        """
        sum = 0
        if root is None:
            return 0
        if root.val in range(low,high+1):
            sum+=root.val
        if root.left:
            sum+=self.rangeSumBST(root.left,low,high)
        if root.right:
            sum+=self.rangeSumBST(root.right,low,high)
        return sum

    def rangeSumBST2(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: int
        """
        if not root:
            return 0
        
        # If the current node's value is less than low,
        # then all nodes in its left subtree are also less than low.
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        
        # If the current node's value is greater than high,
        # then all nodes in its right subtree are also greater than high.
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        
        # Otherwise, the current node's value is in the range,
        # so include it and recursively search both subtrees.
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
