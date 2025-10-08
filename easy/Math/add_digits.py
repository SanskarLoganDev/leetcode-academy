# 258. Add Digits

# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

# Example 1:

# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2 
# Since 2 has only one digit, return it.

# Example 2:

# Input: num = 0
# Output: 0
 
# Constraints:

# 0 <= num <= 231 - 1
 

# Follow up: Could you do it without any loop/recursion in O(1) runtime?

# time complexity: O(logN) where N is the input number
# space complexity: O(1)
class Solution:
    def addDigits(self, num: int) -> int:
        while True:
            if num//10==0:
                return num
            total = 0
            while num:
                total = total+ num%10
                num = num//10
            num = total
            
            
# Optimised approach using digital root concept
# time complexity: O(1)

class Solution:
    def addDigits(self, num: int) -> int:
        while True:
            if num == 0:
                return 0
            if num % 9 == 0:
                return 9
            return num % 9

# Concept of digital root:

# The digital root is found by repeatedly summing the digits of a number until a single-digit result is obtained. For example, the digital root of 3456 is 3+4+5+6=18, then 1+8=9. The digital root is a useful way to check divisibility by 9 and verify the accuracy of arithmetic calculations. 

# How to Find a Digital Root
# Sum the digits: Add all the individual digits of the number. 
# Check if the sum is single-digit: If the sum has more than one digit, repeat the process. 
# Continue until single-digit: Keep adding the digits of the resulting number until you get a number between 1 and 9. 

# Examples
# Digital Root of 25: 2 + 5 = 7 
# Digital Root of 673: 6 + 7 + 3 = 16; 1 + 6 = 7 
# Digital Root of 1959: 1 + 9 + 5 + 9 = 24; 2 + 4 = 6 

# Key Characteristics
# The digital root is always a single digit. 
# In base 10, the digital root is the same as the remainder when the number is divided by 9, except when the digital root is 9, in which case the remainder is 0. 
# A digital root of 9 indicates the number is divisible by 9. 
