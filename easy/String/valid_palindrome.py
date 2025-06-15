# 125. Valid Palindrome (Neetcde 150)

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

# Time Complexity: O(n), space complexity: O(n)
# Solution 1: Using string manipulation
def isPalindrome(s):
    if not s:
        return False
    str1=""
    s=s.lower()
    for i in range(len(s)):
        if s[i].isalnum():
            str1+=s[i]
    return str1==str1[::-1]
print(isPalindrome("0P"))

# Optimised solu using 2 pointer method. time complexity: O(n), space complexity: O(1)

def isPalindrome(s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False

        return True

# if the interviewer asks us not  to use the isalnum() method, we can use the following code to check if a character is alphanumeric
def is_alphanumeric(c):
    return (ord('a') <= ord(c) <= ord('z') or
            ord('A') <= ord(c) <= ord('Z') or
            ord('0') <= ord(c) <= ord('9'))
 