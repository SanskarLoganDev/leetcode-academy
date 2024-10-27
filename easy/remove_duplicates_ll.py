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
        