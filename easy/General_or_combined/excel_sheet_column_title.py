# 168. Excel Sheet Column Title

# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

# For example:

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
 

# Example 1:

# Input: columnNumber = 1
# Output: "A"
# Example 2:

# Input: columnNumber = 28
# Output: "AB"
# Example 3:

# Input: columnNumber = 701
# Output: "ZY"
 

# Constraints:

# 1 <= columnNumber <= 231 - 1

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        num = columnNumber
        while num>0:
            rem = (num-1)%26
            char = chr(65+rem) # here 65 is the ASCII value of 'A'
            # ord(char) gives the ASCII value of char, and we subtract 65 to convert 'A' to 0, 'B' to 1, ..., 'Z' to 25`
            res.append(char)
            num = (num-1)//26
        return "".join(reversed(res))