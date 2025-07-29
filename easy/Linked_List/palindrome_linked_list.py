# 234. PALINDROME LINKED LIST

# Given the head of a singly linked list, return true if it is a 
# palindrome
#  or false otherwise.

 

# Example 1:


# Input: head = [1,2,2,1]
# Output: true
# Example 2:


# Input: head = [1,2]
# Output: false
 

# Constraints:

# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9
 

# Follow up: Could you do it in O(n) time and O(1) space?

# Definition for singly-linked list.

# Solution using list

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        curr = head
        l1 = []
        while curr:
            l1.append(curr.val)
            curr = curr.next
        l2 = l1[::-1]
        return l1==l2

# solution using finding middle and reversing the second half
# Time complexity: O(n)
# Space complexity: O(1)

from typing import Optional
class Solution:
    def reverseLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr =  head
        while curr:
            curr_next = curr.next
            curr.next = prev
            prev = curr
            curr = curr_next
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        # finding middle (slow)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # if fast is not None, it means the length of the linked list is odd
        if fast!=None:
            slow = slow.next
        
        tail = self.reverseLinkedList(slow)
        start = head
        # Comparing values of 2 halves of string
        # start is the head and tail is the reversed second half
        while start and tail:
            if start.val!=tail.val:
                return False
            start = start.next
            tail = tail.next
        return True
        

# Solution using Tortoise and Hare algorithm

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        slow = head
        fast = head
        
        # finding middle (slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # reversing the other half
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
            
        # Comparing values of 2 halves of string
        left = head
        right = prev
        while right:
            if left.val!=right.val:
                return False
            right=right.next
            left=left.next
        return True
        