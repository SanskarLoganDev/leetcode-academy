# 138. Copy List with Random Pointer
# Medium , Neetcode 150 (Important)

# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

# Return the head of the copied linked list.

# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
# Your code will only be given the head of the original linked list.

# Example 1:

# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Example 2:


# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]
# Example 3:

# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]

# Constraints:

# 0 <= n <= 1000
# -104 <= Node.val <= 104
# Node.random is null or is pointing to some node in the linked list.

# time complexity: O(n)
# space complexity: O(n)
# The solution requires 2 passes through the linked list:
# 1. The first pass creates a mapping from the original nodes to their corresponding new nodes
# 2. The second pass sets the next and random pointers for the new nodes based on the mapping created in the first pass

from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        oldToCopy = {None: None} # we have None as a key to handle the case where the random pointer is null
        while curr:
            node = Node(curr.val)
            oldToCopy[curr] = node
            curr = curr.next

        curr = head
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next
        return oldToCopy[head]
    
    
# Time complexity: O(n)
# Space complexity: O(n)/O(1) debatable as we are not using any extra space for the mapping in the second solution, but we are still creating new nodes, so Space complexity is O(1) but extra space would be O(n) if we consider the new nodes created.

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head==None:
            return None
        curr = head
        # 1) Insert new nodes between the exisiting ones
        while curr:
            curr_next = curr.next         # B
            curr.next = Node(curr.val)    # A -> x
            curr.next.next = curr_next    # A -> x -> B
            curr = curr_next              # curr = B

        # 2) Deep copy of random characters
        curr = head
        while curr and curr.next:
            if curr.random==None:
                curr.next.random = None
            else:
                curr.next.random = curr.random.next # this is the new node that we created in the first step
            curr = curr.next.next
        
        # 3) Separate the linked list

        curr = head
        newHead = head.next
        newCurr = newHead
        while curr and newCurr:
            curr.next = None if curr.next==None else curr.next.next # we are skipping the new nodes and checking if the next node is None or not
            newCurr.next = None if newCurr.next==None else newCurr.next.next
            curr = curr.next
            newCurr = newCurr.next

        return newHead

