# 680. Valid Palindrome II
# Neetcode 250

# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

# Example 1:

# Input: s = "aba"
# Output: true

# Example 2:

# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.

# Example 3:

# Input: s = "abc"
# Output: false
 

# Constraints:

# 1 <= s.length <= 105
# s consists of lowercase English letters.

# Time complexity: O(N^2)
# Space complexity: O(N)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(words): # O(N)
            l = 0
            r = len(words)-1
            while l<=r:
                if words[l]!=words[r]:
                    return False
                l+=1
                r-=1
            return True

        if isPalindrome(s):
            return True
        
        for i in range(len(s)):
            new = s[:i]+s[i+1:] # O(N)
            if isPalindrome(new): # O(N)
                return True
        return False
    
# Optimised solution
# time complexity: O(N) because the slicing happens at most once
# space complexity: O(N)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while l<r:
            if s[l]!=s[r]: # once they are unequal, you get one more chance to remove each left and right value and check if they are palindrome. This happens at most once
                skipLeft = s[l+1:r+1] # remove left value and check palindrome: skipLeft == skipLeft[::-1]
                skipRight = s[l:r]
                if skipLeft == skipLeft[::-1] or skipRight == skipRight[::-1]:
                    return True
                else:
                    return False
            l+=1
            r-=1
        return True # return true if s[l] and s[r] are always equal