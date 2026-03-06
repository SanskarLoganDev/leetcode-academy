# 1784. Check if Binary String Has at Most One Segment of Ones

# Given a binary string s ​​​​​without leading zeros, return true​​​ if s contains at most one contiguous segment of ones. Otherwise, return false.

# Example 1:

# Input: s = "1001"
# Output: false
# Explanation: The ones do not form a contiguous segment.
# Example 2:

# Input: s = "110"
# Output: true
 

# Constraints:

# 1 <= s.length <= 100
# s[i]​​​​ is either '0' or '1'.
# s[0] is '1'.

# time complexity: O(N)
# space complexity: O(1)

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        seen = False
        i = 0
        while i<len(s):
            if seen and s[i]=='1':
                return False
            if s[i]=="1":
                seen = True
                while i<len(s) and s[i]=="1":
                    i+=1
            else:
                i+=1
        return seen