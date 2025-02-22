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
    

# Let's use **Example 1**:

# - **Input Tree (BST):**

#   ```
#           10
#          /  \
#         5    15
#        / \     \
#       3   7     18
#   ```
  
# - **Parameters:**  
#   `low = 7` and `high = 15`.

# ### **Step 1: Process the Root (Node 10)**

# - **At Node 10:**  
#   - Check if `root` is `None` → **No.**
#   - Check if `10 < 7` → **False.**
#   - Check if `10 > 15` → **False.**
#   - Since 10 is within [7, 15], we include it and recursively process both children.
  
# - **Sum at Node 10:**  
#   \( {sum} = 10 +{rangeSumBST}(root.left, 7, 15) + {rangeSumBST}(root.right, 7, 15) \)

# ### **Step 2: Process the Left Subtree (Node 5)**

# - **At Node 5:**  
#   - Check if `5 < 7` → **True.**
#   - **Action:**  
#     - We skip the left subtree of Node 5 (since all values there are less than 5, and thus less than 7).  
#     - Return \( \text{rangeSumBST}(node 5.right, 7, 15) \).
    
# - **Now process Node 5's right child (Node 7):**

#   - **At Node 7:**  
#     - Check if `7 < 7` → **False** (7 is equal to 7).  
#     - Check if `7 > 15` → **False.**
#     - Node 7 is within range, so include its value.
#     - Both children of Node 7 are `None`, so the recursive calls on Node 7’s left and right return 0.
    
#   - **Sum at Node 7:**  
#     \( \text{sum} = 7 + 0 + 0 = 7 \)
  
# - **Thus, the left subtree of Node 10 contributes:**  
#   \( \text{rangeSumBST}(node 5, 7, 15) = 7 \)

# ### **Step 3: Process the Right Subtree (Node 15)**

# - **At Node 15:**  
#   - Check if `15 < 7` → **False.**
#   - Check if `15 > 15` → **False** (15 equals 15).
#   - Node 15 is within range, so include its value.
#   - Process both children:
  
# - **Left child of Node 15:**  
#   - `None` → returns 0.
  
# - **Right child of Node 15:**  
#   - **At Node 18:**  
#     - Check if `18 < 7` → **False.**
#     - Check if `18 > 15` → **True.**
#     - Since 18 is greater than high, ignore its right subtree and process only its left child.
#     - Node 18’s left is `None` → returns 0.
  
#   - **Thus, Node 18 contributes:**  
#     \( 0 \) (we do not add 18 because it's out of range).
  
# - **Sum at Node 15:**  
#   \( \text{sum} = 15 + 0 + 0 = 15 \)

# ### **Step 4: Aggregate the Results at the Root**

# - **At Node 10:**  
#   - Left subtree sum = **7**  
#   - Right subtree sum = **15**  
#   - Node 10’s value = **10**
  
# - **Total Sum:**  
#   \( 10 + 7 + 15 = 32 \)

# This matches the expected output: **32**.


