# 392. Is Subsequence

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false
 

# Constraints:

# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.

# Let m = len(s) and n = len(t). So the time complexity is O(n·m)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in range(len(t)):
            if t[i] in s and s[0]==t[i]:  # t[i] in s: a substring‐search over s ⇒ O(m) worst‐case, 
                #s.replace(t[i], "", 1) (when the if fires): scanning s to find the first match + building a new string of length ≲ m ⇒ O(m)
                s=s.replace(t[i],"",1)
        if len(s)==0:
            return True
        return False
    

# Using 2 pointer: time complexity O(n+m)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)>len(t):
            return False
        i=j=0
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                i+=1
            j+=1
        return i==len(s)
        
            
