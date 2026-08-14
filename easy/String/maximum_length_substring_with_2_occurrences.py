# 3090. Maximum Length Substring With Two Occurrences

# Given a string s, return the maximum length of a substring such that it contains at most two occurrences of each character.

# Example 1:

# Input: s = "bcbbbcba"

# Output: 4

# Explanation:

# The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".
# Example 2:

# Input: s = "aaaa"

# Output: 2

# Explanation:

# The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".
 

# Constraints:

# 2 <= s.length <= 100
# s consists only of lowercase English letters.

# at most 2 occurrences can mean 0 occurrence for a character is fine, its only the upper limit of 2 that needs to be checked
# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        counter = [0]*26
        i=0
        j=0
        result = 0
        while j<len(s):
            idx = ord(s[j]) - ord('a')
            counter[idx]+=1

            while counter[idx]>2: # subtract when an occurrence is more than 2
                counter[ord(s[i]) - ord('a')]-=1
                i+=1
            result = max(result, j-i+1)
            j+=1
        return result
        