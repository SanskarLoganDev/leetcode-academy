# 371. Sum of Two Integers
# Neetcode 150 (Important)

# Given two integers a and b, return the sum of the two integers without using the operators + and -.

# Example 1:

# Input: a = 1, b = 2
# Output: 3

# Example 2:

# Input: a = 2, b = 3
# Output: 5
 
# Constraints:

# -1000 <= a, b <= 1000

# Simplest approach
# time complexity: O(1)
# space complexity: O(1)
class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = [a,b]
        return sum(res)

# Bit Manipulation approach
# time complexity: O(1)
# space complexity: O(1)   
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff # we have to use mask to get last 32 bits as in python integer is of infinite bits (there is no bound)
        while (mask&b)>0:
            temp = a
            a = a^b # sum without carry
            b = (temp&b)<<1 # carry
        return (mask&a) if b>0 else a # if b>0 then it is negative number so we have to return last 32 bits only

# How the algorithm works (intuition)

# In binary:

# Sum without carry is XOR (^).
# e.g., 1 ^ 1 = 0 (with a carry), 1 ^ 0 = 1, 0 ^ 0 = 0.

# Carry bits are AND (&) shifted left (<< 1).
# e.g., 1 & 1 = 1 (carry out from that bit), then move that carry to the next higher bit.

# We repeat:

# a = a ^ b → add the bits where there’s no carry.

# b = (old_a & b) << 1 → the carries to add next round.

# Stop when there is no carry left (i.e., the lower 32 bits of b are zero).

# Python integers are unbounded, so we use a 32-bit mask (mask = 0xFFFFFFFF) to simulate 32-bit two’s complement:

# The loop condition uses (mask & b) > 0 to keep going while any carry exists in the lower 32 bits.

# At the end, if b > 0, it means we stopped because the carry “escaped” past 32 bits; we then return the lower 32 bits of a (mask & a). Otherwise we can return a directly.

# Your code:

# mask = 0xffffffff
# while (mask & b) > 0:
#     temp = a
#     a = a ^ b
#     b = (temp & b) << 1
# return (mask & a) if b > 0 else a

# Example 1: a = 5, b = 7

# Binary (4 bits just for readability):

# a = 0101₂ (5)

# b = 0111₂ (7)

# Iter 1

# sum = a ^ b = 0101 ^ 0111 = 0010 (2)

# carry = (a & b) << 1 = (0101 & 0111) << 1 = 0101 << 1 = 1010 (10)

# Update: a = 2, b = 10

# Iter 2

# sum = 0010 ^ 1010 = 1000 (8)

# carry = (0010 & 1010) << 1 = 0010 << 1 = 0100 (4)

# Update: a = 8, b = 4

# Iter 3

# sum = 1000 ^ 0100 = 1100 (12)

# carry = (1000 & 0100) << 1 = 0000 << 1 = 0000 (0)

# Update: a = 12, b = 0

# Loop stops ((mask & b) == 0), return a = 12. ✅


# Example 2: a = -2, b = 3 (32-bit view)

# In 32-bit two’s complement:

# a = -2 → 0xFFFFFFFE

# b = 3 → 0x00000003

# mask = 0xFFFFFFFF

# We’ll show the first few and the last steps (there are up to ~32 carry shifts here):

# Iter 1

# sum = a ^ b = 0xFFFFFFFE ^ 0x00000003 = 0xFFFFFFFD

# carry = (a & b) << 1 = (0xFFFFFFFE & 0x00000003) << 1 = 0x00000002 << 1 = 0x00000004

# Update: a = 0xFFFFFFFD, b = 0x00000004

# Iter 2

# sum = 0xFFFFFFFD ^ 0x00000004 = 0xFFFFFFF9

# carry = (0xFFFFFFFD & 0x00000004) << 1 = 0x00000004 << 1 = 0x00000008

# Update: a = 0xFFFFFFF9, b = 0x00000008

# Iter 3

# sum = 0xFFFFFFF9 ^ 0x00000008 = 0xFFFFFFF1

# carry = (0xFFFFFFF9 & 0x00000008) << 1 = 0x00000008 << 1 = 0x00000010

# Update: a = 0xFFFFFFF1, b = 0x00000010

# … You can see the carry keeps shifting left (4, 8, 16, …). In a true 32-bit register, once the carry shifts past bit 31, the lower 32 bits become 0, i.e., (mask & b) == 0, and the loop stops.

# At that moment:

# The lower 32 bits of a equal 0x00000001 (which is 1).

# b is still positive (because in Python it kept shifting beyond 32 bits), so your final line returns mask & a → 1.

# So -2 + 3 = 1, as expected. ✅

# Why does this take many iterations here? Because adding a small positive to a negative number in two’s complement can push a carry through a long run of 1 bits. With the mask in the condition, it still completes in at most 32 iterations, since carries leave the 32-bit window.

# Why the mask and the final return check matter

# Python ints don’t overflow; they grow arbitrarily. But two’s complement arithmetic assumes fixed width.
# Using mask to check (mask & b) > 0 means “do I still have any carry within 32 bits?”

# When the carry leaves the 32-bit window, (mask & b) == 0, we stop. If b itself is still positive (because it kept shifting), that’s our cue to return only the lower 32 bits of a (mask & a). Otherwise, return a (already a correct Python int).
