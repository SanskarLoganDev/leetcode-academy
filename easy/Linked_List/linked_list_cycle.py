# 141. LINKED LIST CYCLE Neetcode 150 (Important)

# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# Example 1:

# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# Example 2:

# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
# Example 3:


# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head==None:
            return False
        set1 = set() # use set instead of list as traversing is faster
        while head:
            if head in set1:
                return True
            set1.add(head) # add the head to set instead of just head.val
            head=head.next
        return False
    
# Floyd's tortoise and hare algorithm

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head==None:
            return False
        fast = head
        slow = head

        while fast and fast.next: # fast pointer moves two steps, slow pointer moves one step, we check both fast and fast.next to avoid NoneType errors as fast.next can be None
            slow = slow.next # we put slow.next and fast.next.next before checking for equality as initally both slow and fast point to the same node
            fast = fast.next.next
            if slow == fast:
                return True
        return False

