# Given an integer x, return true if x is a palindrome, and false otherwise.

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Basic solution

# def isPalindrome(x):
#     num = str(x)
#     if num[::-1] == num:
#         return True
#     else:
#         return False
# print(isPalindrome(-121))

# Follow up: Could you solve it without converting the integer to a string?

def isPalindrome(x):
    if x<0:
        return False
    org = x
    rev = 0
    while x>0:
        last_digit = x%10
        rev = rev*10 + last_digit
        x=x//10
    if org==rev:
        return True
    else:
        return False
print(isPalindrome(9))