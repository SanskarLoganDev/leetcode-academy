# 876. MIDDLE OF THE LINKED LIST

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None:
            return None
        count = 0
        curr = head
        while curr:
            count+=1
            curr = curr.next
        mid_index = count//2
        print(mid_index)

        index = 0
        while head:
            if index == mid_index:
                break
            head = head.next
            index+=1
        return head
            
        