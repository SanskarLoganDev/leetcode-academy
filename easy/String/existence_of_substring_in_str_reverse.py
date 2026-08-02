# 3083. Existence of a Substring in a String and Its Reverse

# Given a string s, find any substring of length 2 which is also present in the reverse of s.

# Return true if such a substring exists, and false otherwise.

# Example 1:

# Input: s = "leetcode"

# Output: true

# Explanation: Substring "ee" is of length 2 which is also present in reverse(s) == "edocteel".

# Example 2:

# Input: s = "abcba"

# Output: true

# Explanation: All of the substrings of length 2 "ab", "bc", "cb", "ba" are also present in reverse(s) == "abcba".

# Example 3:

# Input: s = "abcd"

# Output: false

# Explanation: There is no substring of length 2 in s, which is also present in the reverse of s.

# Constraints:

# 1 <= s.length <= 100
# s consists only of lowercase English letters.

# Brute force solution
# Time complexity: O(N^3)
# Space complexity: O(N)

class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        rev = s[::-1]
        for i in range(len(s)): # O(N)
            for j in range(i+2, len(s)+1): # O(N)
                substr = s[i:j]
                if substr in rev: # O(N)
                    return True
        return False

# Further optimised, we do not need to check substr of every length, minimum length of 2 is fine
# Time complexity: O(N^2)
# Space complexity: O(N)
class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        rev = s[::-1]
        for i in range(len(s)-1):
            substr = s[i:i+2]
            if substr in rev:
                return True
        return False
    
# Optimised solution
# consider xy in string s
# "xy" is a substring of reverse(s) ⟺ "yx" is a substring of s
# therefore look for yx in s too, and have a check for when adjacent elements are same

# Time complexity: O(N)
# Space: O(1) — the seen set holds pairs from a 26-letter alphabet, so it's bounded by 26×26 = 676 entries regardless of n

class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        seen = set()
        for i in range(len(s)-1):
            a = s[i]
            b = s[i+1]
            if a == b or (b, a) in seen:
                return True
            seen.add((a, b))
        return False