# 338. Counting Bits
# Neetcode 150 (Important)

# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

# Example 1:

# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# Example 2:

# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
 

# Constraints:

# 0 <= n <= 105
 

# Follow up:

# It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?

# using in-built functions, time complexity O(N)

# time complexity: O(N log N) where N is the number of digits in the number
# space complexity: O(N) where N is the number of digits in the number
from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(0,n+1):
            res.append(bin(i).count('1'))
        return res
    
    
# Using DP and bitise operators
# time complexity: O(N) where N is the number of digits in the number
# space complexity: O(N) where N is the number of digits in the number
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        
        for i in range(1, n + 1):
            res[i] = res[i >> 1] + (i & 1)
        
        return res

# Understanding res[i] = res[i >> 1] + (i & 1)
# 1. Bitwise Right Shift (i >> 1):
# Purpose: This operation shifts all bits of i to the right by one position.

# Effect: When you right-shift a binary number by one position (i >> 1), you effectively divide the number by 2 in integer arithmetic.

# Example: If i = 5 (binary 101), then i >> 1 gives 2 (binary 10).

# 2. Bitwise AND (i & 1):
# Purpose: This operation checks the least significant bit (LSB) of i.

# Effect: By performing i & 1, you extract the LSB of i.

# Example: If i = 5 (binary 101), then i & 1 gives 1 (because 101 & 001 = 001).

# 3. Combining Both:
# Logic: res[i] = res[i >> 1] + (i & 1) means:

# res[i >> 1]: This fetches the number of 1's in the binary representation of i // 2 (the number obtained by right-shifting i by one bit).

# i & 1: This checks if the LSB of i is 1.

# Effect: By adding these two results together, you determine the number of 1's in the binary representation of i.

# Example Walkthrough
# Let's use an example to illustrate how this works:

# Suppose i = 5.

# Binary Representation of 5:

# 5 in binary is 101.

# Calculating res[5]:

# i >> 1: Right shift 5 by one bit gives 2 (binary 10).

# i & 1: Check LSB of 5, which is 1.

# So, res[5] = res[2] + 1.

# Previous Values (res[2]):

# Calculate res[2]:

# 2 in binary is 10.

# res[2] would have been calculated previously.

# Final Calculation:

# If res[2] (number of 1's in 2) is known from previous calculations, then res[5] = res[2] + 1.

# This process ensures that each res[i] is computed based on the number of 1's in its halved version (i >> 1) and whether its LSB (i & 1) is 1 or 0. This is a direct way to count the number of 1's in binary without explicitly converting i into a binary string.

# Efficiency
# Time Complexity: O(n) — One pass through n elements.

# Space Complexity: O(n) — Space used for the res array.