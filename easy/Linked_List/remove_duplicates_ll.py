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
            else: # here else is reauired to handle cases where duplicates occur more than twice, directly increasing itr to itr.next will skip comparisons
                head = head.next
        return list1
        