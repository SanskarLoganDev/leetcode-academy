# MERGE TWO SORTED LISTS

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.



class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        head = ListNode() # here this wroks as self.head
        itr = head        # a pointer for the sorted final array
        while list1 and list2: # here list1 and list2 also serve as pointers inside list1 and list2 respectively
            if list1.val>list2.val:
                itr.next = list2
                list2 = list2.next
            else:
                itr.next=list1
                list1=list1.next
            itr = itr.next
        if list1:          # dealing with any remaining elements in list1, happens when list1 is longer than list2
            itr.next=list1
        else:
            itr.next=list2
        return head.next
    
        