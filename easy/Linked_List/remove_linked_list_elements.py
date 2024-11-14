# 203. REMOVE LINKED LIST ELEMENTS

# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Example 1:


# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
# Example 2:

# Input: head = [], val = 1
# Output: []
# Example 3:

# Input: head = [7,7,7,7], val = 7
# Output: []

# 1st Solution using the concept provided by neetcode for remove_duplicates_II.py problem

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0, head)
        curr = dummy
        while curr:
            while curr.next and curr.next.val==val:
                curr.next = curr.next.next
            curr = curr.next
        return dummy.next
    
# Neetcode's solution for this problem using 2 pointers

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next
