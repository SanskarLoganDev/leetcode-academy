# 143. Reorder Linked List 
# Neetcode 150 (Important)

# You are given the head of a singly linked-list.

# The positions of a linked list of length = 7 for example, can intially be represented as:

# [0, 1, 2, 3, 4, 5, 6]

# Reorder the nodes of the linked list to be in the following order:

# [0, 6, 1, 5, 2, 4, 3]

# Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:

# [0, n-1, 1, n-2, 2, n-3, ...]

# You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.

# Example 1:

# Input: head = [2,4,6,8]

# Output: [2,8,4,6]
# Example 2:

# Input: head = [2,4,6,8,10]

# Output: [2,10,4,8,6]
# Constraints:

# 1 <= Length of the list <= 1000.
# 1 <= Node.val <= 1000

# implmenting the solution if it was a list instead of a linked list
class Solution:
    def reorderList(self, l1) -> None:
        res = []
        i = 0
        j = len(l1) - 1
        while i<j:
            res.append(l1[i])
            res.append(l1[j])
            i += 1
            j -= 1
        if i == j:
            res.append(l1[i])
        return res
    
sol = Solution()
head = [2,4,6,8,10]
l1 = sol.reorderList(head)
print(l1)  # Output: [2, 8, 4, 6]
        
        