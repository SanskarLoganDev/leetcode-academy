# 25. Reverse Nodes in k-Group
# Neetcode 150 (Important)

# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.

# Example 1:
# image URL: https://assets.leetcode.com/uploads/2020/10/03/reverse_ex1.jpg

# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]

# Example 2:
# image URL: https://assets.leetcode.com/uploads/2020/10/03/reverse_ex2.jpg

# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]
 

# Constraints:

# The number of nodes in the list is n.
# 1 <= k <= n <= 5000
# 0 <= Node.val <= 1000
 

# Follow-up: Can you solve the problem in O(1) extra memory space?


from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse(self, head: Optional[ListNode], k: int):
        """
        Reverse exactly k nodes starting at head.
        Precondition: there are at least k nodes available.
        Returns (new_head, new_tail, next_group_start).
        """
        curr = head
        prev = None
        i = 0
        while i < k:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            i += 1
        return prev, head, curr  # new head, new tail, node after the block (new group start)

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        # link dummy to head
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # Find the k-th node ahead (or stop if fewer than k remain)
            # this is just to check if we have enough nodes to reverse
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    # fewer than k remain; leave them as-is
                    return dummy.next

            group_start = group_prev.next
            # Reverse the k nodes starting at group_start
            new_head, new_tail, next_group_start = self.reverse(group_start, k)

            # Stitch: prev part -> reversed block -> remainder
            group_prev.next = new_head
            new_tail.next = next_group_start

            # Move group_prev to the tail of the reversed block for next iteration
            group_prev = new_tail
