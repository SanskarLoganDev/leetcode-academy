# 171. Excel Sheet Column Number

# Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

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

# Input: columnTitle = "A"
# Output: 1
# Example 2:

# Input: columnTitle = "AB"
# Output: 28
# Example 3:

# Input: columnTitle = "ZY"
# Output: 701
 
# Constraints:

# 1 <= columnTitle.length <= 7
# columnTitle consists only of uppercase English letters.
# columnTitle is in the range ["A", "FXSHRXW"].

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        val = 0
        for char in columnTitle: # here 65 is the ASCII value of 'A'
            # ord(char) gives the ASCII value of char, and we subtract 65 to convert 'A' to 0, 'B' to 1, ..., 'Z' to 25`
            val = val*26+(ord(char)-65)+1 # here +1 is used to convert 0-25 to 1-26
        return val