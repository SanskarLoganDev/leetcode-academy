# 1957. Delete Characters to Make Fancy String

# A fancy string is a string where no three consecutive characters are equal.

# Given a string s, delete the minimum possible number of characters from s to make it fancy.

# Return the final string after the deletion. It can be shown that the answer will always be unique.

# Example 1:

# Input: s = "leeetcode"
# Output: "leetcode"
# Explanation:
# Remove an 'e' from the first group of 'e's to create "leetcode".
# No three consecutive characters are equal, so return "leetcode".
# Example 2:

# Input: s = "aaabaaaa"
# Output: "aabaa"
# Explanation:
# Remove an 'a' from the first group of 'a's to create "aabaaaa".
# Remove two 'a's from the second group of 'a's to create "aabaa".
# No three consecutive characters are equal, so return "aabaa".
# Example 3:

# Input: s = "aab"
# Output: "aab"
# Explanation: No three consecutive characters are equal, so return "aab".

# Constraints:

# 1 <= s.length <= 105
# s consists only of lowercase English letters.

# Brute force solution O(N^2)
class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s)<3:
            return s
        ans = s[0]
        i=1
        while i<len(s):
            count=1
            if s[i]==s[i-1]:
                while i<len(s) and s[i]==s[i-1]:
                    if count==2:
                        i+=1
                        continue
                    ans+=s[i]
                    i+=1
                    count+=1
            else:
                ans+=s[i]
                i+=1
        return ans
    
# The outer while and the inner “skip‐to‐next” loops together advance i from 1 to n exactly once, so you only ever process each character a constant number of times—structurally that part is O(n).

# However, because ans is a Python string and you do
# ans += s[i]
# inside those loops, each concatenation takes time proportional to the length of ans so far. In the worst case ans grows to size ~n, and you perform ~n concatenations, giving a total of


# 1+2+3+⋯+n=O(n^2)
# character‑copies.

# So as written, time complexity = O(n²).
# (If you instead accumulated into a list and did one "".join(...) at the end, the algorithmic logic would run in O(n).)

#Optimised Solution O(N)

class Solution:
    def makeFancyString(self, s: str) -> str:
        r=[]
        for i in range(len(s)):
            if len(r)>=2 and r[-1]==r[-2]==s[i]:
                continue
            r.append(s[i])
        return "".join(r)