# 394. Decode String
# Neetcode 250

# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 105.

# Example 1:

# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"

# Example 2:

# Input: s = "3[a2[c]]"
# Output: "accaccacc"

# Example 3:

# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
 

# Constraints:

# 1 <= s.length <= 30
# s consists of lowercase English letters, digits, and square brackets '[]'.
# s is guaranteed to be a valid input.
# All the integers in s are in the range [1, 300].

# n = len(s) be encoded input size
# L = length of decoded output
# Time complexity: O(n+L) ~ O(L)

# Space complexity: 
# Nesting space is defO(L + d)
# Since usually d <= n, you can say:
# O(L + n)
# If output space is excluded, auxiliary space is mainly:
# O(d)

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i]==']':
                substr = ""
                while stack[-1]!='[': # extracting the substr
                    substr = stack.pop()+substr
                stack.pop() # popping the opening brackets
                k = ""
                while stack and stack[-1].isdigit(): # extracting the multiplied digit
                    k = stack.pop() + k
                stack.append(int(k)*substr)
            else:
                stack.append(s[i])
        return "".join(stack)

class Solution:
    def decodeString(self, s: str) -> str:

        def dfs(i):
            res = ""

            while i < len(s) and s[i] != ']':
                if s[i].isalpha():
                    res += s[i]
                    i += 1

                else:
                    # build the repeat count
                    k = 0
                    while i < len(s) and s[i].isdigit():
                        k = k * 10 + int(s[i])
                        i += 1

                    # skip '['
                    i += 1

                    # recursively decode inside brackets
                    decoded, i = dfs(i)

                    # add repeated decoded string
                    res += decoded * k

                    # skip ']'
                    i += 1

            return res, i

        result, _ = dfs(0)
        return result

# Dry run

# How recursion works

# Take:

# s = "3[a2[c]]"

# At the outer level:

# 3[ ... ]

# we read:

# k = 3

# Then recursively decode:

# "a2[c]"

# Inside that recursive call:

# res = "a"

# Then we encounter:

# 2[c]

# So another recursive call decodes:

# "c"

# which returns:

# "c"

# Then:

# 2 * "c" = "cc"

# So that level becomes:

# "a" + "cc" = "acc"

# Return "acc" to the outer call.

# Then outer call does:

# 3 * "acc" = "accaccacc"

# Final answer:

# "accaccacc"
# Why dfs() returns both string and index

# This part:

# return res, i

# is important because the recursive call needs to tell its caller:

# what substring it decoded
# where it stopped in the original string

# It stops when it reaches:

# ]

# The caller then skips that closing bracket and continues.