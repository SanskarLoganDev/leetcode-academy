# 344. REVERSE STRING

# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

 

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]


# General method

# def reverseString(s):
#     print(s)
#     return s[::-1]
# print(reverseString(s = ["h","e","l","l","o","x"]))

def reverseString(s):
    left = 0
    right = len(s)-1
    while left<right:
        temp = s[left]
        s[left]=s[right]
        s[right]=temp
        left+=1
        right-=1
    return s

print(reverseString(s = ["h","e","l","l","o","x"]))

# Alternate way of swapping

# s[left] = chr(ord(s[left]) + ord(s[right]))
# s[right] = chr(ord(s[left]) - ord(s[right]))
# s[left] = chr(ord(s[left]) - ord(s[right]))
