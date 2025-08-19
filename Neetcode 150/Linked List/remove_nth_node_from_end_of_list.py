# 19. Remove Nth Node From End of List
# Neetcode 150 (Important)

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]

# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
 
# Follow up: Could you do this in one pass?

from typing import Optional

# time complexity: O(N) where N is the number of nodes in the linked list
# space complexity: O(1) as we are not using any extra space

# This solution uses reversing the linked list to simplify the removal of the nth node from the end and thus is not a one-pass solution.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            curr_next = curr.next
            curr.next = prev
            prev = curr
            curr = curr_next
        return prev
            
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        rev = self.reverse(head)
        dummy = ListNode(0, rev)
        curr = dummy
        count = 1
        while count<n and curr:
            curr = curr.next
            count+=1
        if curr.next:
            curr.next = curr.next.next

        return self.reverse(dummy.next)
        
        
# Same time and space complexity as the above solution but this is a one-pass solution.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n>0 and right:
            right = right.next
            n-=1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next # here we return dummy.next instead of head as dummy is a placeholder node to simplify the logic and dummy.next is the actual head of the modified linked list.
