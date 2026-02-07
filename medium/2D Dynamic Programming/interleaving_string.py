# 97. Interleaving String
# Neetcode 150

# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

# An interleaving of two strings s and t is a configuration where s and t are divided into n and m substrings respectively, such that:

# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1
# The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
# Note: a + b is the concatenation of strings a and b.

 

# Example 1:


# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
# Explanation: One way to obtain s3 is:
# Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
# Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
# Since s3 can be obtained by interleaving s1 and s2, we return true.

# Example 2:

# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
# Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.

# Example 3:

# Input: s1 = "", s2 = "", s3 = ""
# Output: true
 

# Constraints:

# 0 <= s1.length, s2.length <= 100
# 0 <= s3.length <= 200
# s1, s2, and s3 consist of lowercase English letters.
 

# Follow up: Could you solve it using only O(s2.length) additional memory space?

# using recursion
# time complexity O(2^(n+m)) as for each character we have 2 choices and 
# space complexity O(n+m) for recursion stack
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3)!=len(s1)+len(s2): # early return when lengths don't match
            return False
        def solve(s, i, j):
            if len(s)==len(s3) and s==s3: # the formed string length matches s3
                return True
            if i>=len(s1) and j>=len(s2): # both strings are exhausted
                return False

            # take from s1
            take_s1 = False # initialize to false because we may not take from s1
            if i<len(s1):
                take_s1 = solve(s+s1[i], i+1, j) # take from s1 thereby increasing i

            # take from s2
            take_s2 = False # initialize to false because we may not take from s2
            if j<len(s2):
                take_s2 = solve(s+s2[j], i, j+1) # take from s2 thereby increasing j

            return take_s1 or take_s2 # return true if either taking from s1 or s2 leads to a solution
        return solve("", 0, 0)

# In the above solution we are forming the string s and comparing with s3 which is not efficient. We can directly compare characters of s1 and s2 with s3 without forming the string.

# Using memoization to optimize the above solution
# time complexity O(n*m) as we are storing results for each index combination of s1 and s2 and 
# space complexity O(n*m) for memoization table and O(n+m) for recursion stack

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3)!=len(s1)+len(s2):
            return False

        memo = {}
        def solve(i, j):
            k = i+j # index for s3 is sum of indices of s1 and s2 as we are interleaving
            if i==len(s1) and j==len(s2): # both strings are exhausted and we have formed s3 successfully
                return True

            key = (i, j)
            if key in memo:
                return memo[key]
            
            # take from s1
            take_s1 = False
            if i<len(s1) and s3[k]==s1[i]:
                take_s1 = solve(i+1, j) # take from s1 thereby increasing i

            # take from s2
            take_s2 = False
            if j<len(s2) and s3[k]==s2[j]:
                take_s2 = solve(i, j+1) # take from s2 thereby increasing j

            memo[key] = take_s1 or take_s2
            return memo[key]
        return solve(0, 0)
    

            