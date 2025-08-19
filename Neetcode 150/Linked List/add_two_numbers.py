# 2. Add Two Numbers
# Neetcode 150, Important

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Example 4:

# Input: l1 = [0,8,6,5,6,8,3,5,7], l2 = [6,7,8,0,8,5,8,9,7]
# Output: [6,5,5,6,4,4,2,5,5,1]

# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# time complexity: O(n^2 + m^2) where n and m are the lengths of the two linked lists
# space complexity: O(D) where D is the number of digits in the sum                         

# 1) Unit-cost model (every arithmetic op costs O(1))
# This is the “classroom” model where num = num*10 + d is treated as constant time regardless of how big num gets.

# Breakdown:

# Reverse both lists: touches each node once
# → O(n + m)

# Convert each list to an int (number) by iterating its nodes once and doing constant work each step
# → O(n + m)

# Build the output:

# num1 + num2: O(1) (by unit-cost assumption)

# str(sum): converts an L-digit number to a string → O(L)

# num[::-1]: reverses that string → O(L)

# Build L nodes from the reversed string → O(L)
# Together this step is O(L).

# Since L ≤ max(n, m) + 1 ≤ n + m + 1, we have O(L) ⊆ O(n + m).

# Put together:
# O(n + m) + O(n + m) + O(L) = O(n + m).
# That’s why the unit-cost summary says O(n + m).

# 2) Bit-complexity model (big-int ops get slower as numbers grow)
# This is more realistic for Python, because Python integers are arbitrary precision. Now, the cost of num = num*10 + d depends on how many digits num already has.

# Think step-by-step for number(head) on a k-digit list:

# At step 1, num has ~1 digit → cost ~O(1)
# At step 2, num has ~2 digits → cost ~O(2)
# At step k, num has ~k digits → cost ~O(k)
# Total cost is 1 + 2 + … + k = k(k+1)/2 = O(k²).

# Apply that to both lists:

# First list: O(n²)

# Second list: O(m²)

# The rest of the steps:
# Addition of two big integers: adding two L-digit numbers is O(L)
# str(sum), string reverse, build nodes: each is O(L)
# Reversals of the lists are still O(n + m)

# Now compare magnitudes:
# Quadratic terms: O(n² + m²)
# Linear terms: O(n + m) and O(L) with L ≤ max(n, m) + 1

# For large inputs, O(n² + m²) dwarfs O(L) and O(n + m), so the overall runtime is
# O(n² + m²).

class Solution:
    def reverse(self, head: Optional[ListNode]) -> int:
        prev = None
        curr = head
        while curr:
            curr_next = curr.next
            curr.next = prev
            prev = curr
            curr = curr_next

        return prev

    def number(self, head: Optional[ListNode]) -> int:  # fixed annotation
        curr = head
        num = 0
        while curr:
            num = num * 10 + curr.val
            curr = curr.next
        return num

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = int(self.number((self.reverse(l1)))) # reversing the linked list and getting the number
        num2 = int(self.number((self.reverse(l2))))
        
        num = str(num1 + num2)
        
        dummy = ListNode(0)
        curr = dummy
        for n in num[::-1]:
            curr.next = ListNode(int(n))
            curr = curr.next
        return dummy.next


# More efficient solution
# time complexity: O(max(n, m))
# space complexity: O(max(n, m))

from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0)
        head = dummy
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            s = v1+v2+carry
            carry = s//10 # integer division to get the carry
            head.next = ListNode(s%10) # modulo to get the last digit
            head = head.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            head.next = ListNode(carry) # if there's a carry left, add it as a new node

        return dummy.next
