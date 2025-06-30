# 7. Reverse Integer

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
 

# Constraints:

# -2^31 <= x <= 2^31 - 1

# time complexity: O(n), where n is the number of digits in the integer x.
# space complexity: O(n), for the intermediate strings.
class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if x[0]=="-":
            x=x[1::]
            rev = -int(x[::-1])
            if rev not in range(-2**31, 2**31):
                return 0
            else:
                return rev
        else:
            rev = int(x[::-1])
            if rev not in range(-2**31, 2**31):
                return 0
            else:
                return rev