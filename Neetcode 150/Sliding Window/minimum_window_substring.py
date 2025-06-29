# 76. Minimum Window Substring (NeetCode 150) Important

# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
 

# Constraints:

# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s and t consist of uppercase and lowercase English letters.
 

# Follow up: Could you find an algorithm that runs in O(m + n) time?

# Time complexity: O(m + n), where m is the length of s and n is the length of t. We traverse both strings once.
# Space complexity: O(m + n), for storing the character counts in countT and window dictionaries.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        countT, window = {}, {} # here we use dictionaries to count the characters in t and the current window in s
        for c in t:
            countT[c] = 1+countT.get(c, 0)
        
        have, need = 0, len(countT)
        res, reslen = [-1,-1], float("inf") # Here we use res to store the result (as we have to return the min string and not just its length) and reslen to store the length of the result window
        # l is the left pointer and r is the right pointer of the sliding window
        l=0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r],0)
            if s[r] in countT and window[s[r]] == countT[s[r]]: # here we check if the current character in s is in t and if its count in the window matches the count in t
                have+=1
            
            while have == need:
                # updating the result if the current window is smaller than the previous one
                if (r-l+1)<reslen:
                    res = [l,r]
                    reslen = r-l+1
                # removing the leftmost character from the window
                window[s[l]]-=1
                if s[l] in countT and window[s[l]] < countT[s[l]]: # here we check if the leftmost character is in t and if its count in the window is less than the count in t
                    have-=1
                l+=1
        l, r = res[0], res[1]
        
        return s[l:r+1] if reslen != float("inf") else ""