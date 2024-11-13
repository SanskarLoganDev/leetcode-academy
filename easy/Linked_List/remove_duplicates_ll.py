# 83. REMOVE DUPLICATES FROM SORTED LIST

# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
# Return the linked list sorted as well.

# Example 1:
# Input: head = [1,1,2]
# Output: [1,2]

# Example 2:
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        list1 = head
        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else: # here else is required to handle cases where duplicates occur more than twice, directly increasing itr to itr.next will skip comparisons
                head = head.next
        return list1

# Neetcode concept solution, the outer loop iterates using the current pointer and inner loop is used to identify and delete duplicates
      
def deleteDuplicates(head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head
        while curr:
            while curr.next and curr.val == curr.next.val: # This loop will continue in case of more than 2 duplicates as well
                curr.next = curr.next.next
            curr = curr.next
        return head