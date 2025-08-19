# 206. REVERSE LINKED LIST Neetcode 150 (Important)

# Given the head of a singly linked list, reverse the list, and return the reversed list.


# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:


# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        curr = head
        while curr:
            next_node = curr.next  # Storing the next of the original linked list as the next is reversed in the next line
            curr.next = prev # connecting the current node to previous node
            prev = curr # moving previous ahead
            curr = next_node # moving current ahead
        return prev # here we return the previous node which is the new head of the reversed linked list
         