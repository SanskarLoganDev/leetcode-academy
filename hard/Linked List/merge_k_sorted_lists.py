# 23. Merge k Sorted Lists
# Neetcode 150 (Important)

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted linked list:
# 1->1->2->3->4->4->5->6
# Example 2:

# Input: lists = []
# Output: []
# Example 3:

# Input: lists = [[]]
# Output: []
 

# Constraints:

# k == lists.length
# 0 <= k <= 104
# 0 <= lists[i].length <= 500
# -104 <= lists[i][j] <= 104
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 104.

from typing import List, Optional

# time complexity: O(n log k), where n is the total number of nodes in all lists and k is the number of lists
# space complexity: O(1) if we ignore the space used by the output linked list


# the following solution uses recursion to merge k sorted linked lists

# Example 1: lists = [[1,4,5], [1,3,4], [2,6]]

# Indices:
# 0: 1→4→5
# 1: 1→3→4
# 2: 2→6

# Your top-level call:
# partitionAndMerge(0, 2, lists)

# Recursion tree
# partitionAndMerge(0, 2)
# ├─ partitionAndMerge(0, 1)
# │  ├─ partitionAndMerge(0, 0)  → returns L0 = [1,4,5]
# │  └─ partitionAndMerge(1, 1)  → returns L1 = [1,3,4]
# │  └─ merge(L0, L1) → M01 = [1,1,3,4,4,5]
# └─ partitionAndMerge(2, 2)      → returns L2 = [2,6]
# └─ merge(M01, L2) → M012 = [1,1,2,3,4,4,5,6]

# Example 2 (even number of lists): lists = [[1,4,5],[1,3,4],[2,6],[0,7]]

# Indices 0-3

# partitionAndMerge(0, 3)
# ├─ partitionAndMerge(0, 1)
# │  ├─ (0,0) → [1,4,5]
# │  └─ (1,1) → [1,3,4]
# │  └─ merge → M01 = [1,1,3,4,4,5]
# └─ partitionAndMerge(2, 3)
#    ├─ (2,2) → [2,6]
#    └─ (3,3) → [0,7]
#    └─ merge → M23 = [0,2,6,7]
# └─ merge(M01, M23) → [0,1,1,2,3,4,4,5,6,7]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        head = ListNode() # dummy node
        itr = head
        while list1 and list2:
            if list1.val>list2.val:
                itr.next = list2
                list2 = list2.next
            else:
                itr.next = list1
                list1 = list1.next
            itr = itr.next
        if list1:
            itr.next = list1
        if list2:
            itr.next = list2
        return head.next

    def partitionAndMerge(self, start: int, end: int, lists: List[Optional[ListNode]]):
        if start>end:
            return None
        if start==end:
            return lists[start]
        
        mid = (start+end)//2
        l1 = self.partitionAndMerge(start, mid, lists)
        l2 = self.partitionAndMerge(mid+1, end, lists)

        return self.mergeTwoLists(l1,l2)
        

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None

        return self.partitionAndMerge(0, len(lists)-1, lists)
        

# same complexity solution using iterative approach

class Solution:
    def mergeTwoLists(self, list1, list2):
        head = ListNode() # dummy node
        itr = head
        while list1 and list2:
            if list1.val>list2.val:
                itr.next = list2
                list2 = list2.next
            else:
                itr.next = list1
                list1 = list1.next
            itr = itr.next
        if list1:
            itr.next = list1
        if list2:
            itr.next = list2
        return head.next
        

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0:
            return None

        while len(lists)>1:
            mergedlists = []

            for i in range(0, len(lists), 2): # if we do range(0, len(lists)-1, 2), we will miss the last list if the number of lists is odd
                l1 = lists[i]
                l2 = lists[i+1] if (i+1)<len(lists) else None # here we handle the case when the number of lists is odd
                mergedlists.append(self.mergeTwoLists(l1,l2))
            lists = mergedlists
        return lists[0]
