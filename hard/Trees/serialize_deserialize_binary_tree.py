# 297. Serialize and Deserialize Binary Tree
# Neetcode 150 (Important)
# Difficulty: Hard

# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

# Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
 
# Example 1:
# https://assets.leetcode.com/uploads/2020/09/15/serdeser.jpg
# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]

# Example 2:
# Input: root = []
# Output: []

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -1000 <= Node.val <= 1000

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

# time complexity: O(N) where N is the number of nodes in the tree
# space complexity: O(N) where N is the number of nodes in the tree
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        out = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node: # having this check just so that we can insert node if it exists else add null to string
                out.append(str(node.val))
                q.append(node.left) # we even add the null nodesas we want those values in string
                q.append(node.right)
            else:
                out.append("null")
        # removing trailing nulls
        while out and out[-1]=="null":
            out.pop()
        print(out)
        return ",".join(out) # returning a comma separated string of all the values in the tree so that we can split it later
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        # creating the root node

        vals = data.split(",")

        root = TreeNode(vals[0])
        q = deque([root])
        i = 1
        while q and i<len(vals):
            parent = q.popleft()
            # handling the left side
            if i<len(vals) and vals[i]!="null":
                left_child = TreeNode(vals[i])
                parent.left = left_child
                q.append(left_child)
            i+=1
            # handling the right child
            if i<len(vals) and vals[i]!="null":
                right_child = TreeNode(vals[i])
                parent.right = right_child
                q.append(right_child)
            i+=1
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
