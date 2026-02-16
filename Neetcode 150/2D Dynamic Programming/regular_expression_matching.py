# 10. Regular Expression Matching
# Neetcode 150 (Important)

# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

# Example 1:

# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".

# Example 2:

# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

# Example 3:

# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
 
# Constraints:

# 1 <= s.length <= 20
# 1 <= p.length <= 20
# s contains only lowercase English letters.
# p contains only lowercase English letters, '.', and '*'.
# It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.


# Using recursion
# time complexity: O(2^(m+n)) where m and n are the lengths of s and p respectively, due to the branching caused by '*' operator.
# space complexity: O(m+n) due to the recursion stack in the worst case.
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def solve(st: str, pattern: str) -> bool:
            # if pattern is empty, st must also be empty
            if len(pattern) == 0:
                return len(st) == 0

            # handle "x*" case (works even if st is empty because we can take 0 occurrences)
            if len(pattern) >= 2 and pattern[1] == "*":
                # zero occurrences of pattern[0]
                not_take = solve(st, pattern[2:])

                # one or more occurrences (only if st has a char and it matches pattern[0] or pattern[0] is '.')
                take = False
                if len(st) > 0 and (st[0] == pattern[0] or pattern[0] == "."):
                    take = solve(st[1:], pattern)

                return take or not_take

            # normal single-character match (must have st non-empty)
            if len(st) == 0:
                return False

            if st[0] == pattern[0] or pattern[0] == ".":
                return solve(st[1:], pattern[1:])

            return False
        return solve(s,p)
            
        
# Recursive solution using indexes instead of slicing (to avoid creating new strings)
# time complexity: O(2^(m+n))
# space complexity: O(m+n) due to the recursion stack in the worst case.

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n1 = len(s)
        n2 = len(p)
        def solve(i,  j):
            # if pattern is empty, st must also be empty
            if j==n2:
                return i==n1

            # handle "x*" case (works even if st is empty because we can take 0 occurrences)
            if n2-j >= 2 and p[j+1] == "*":
                # zero occurrences of pattern[0]
                not_take = solve(i, j+2)

                # one or more occurrences (only if st has a char and it matches pattern[0] or pattern[0] is '.')
                take = False
                if i<n1 and (s[i] == p[j] or p[j] == "."):
                    take = solve(i+1, j)

                return take or not_take

            # normal single-character match (must have st non-empty)
            if i==n1:
                return False

            if s[i] == p[j] or p[j] == ".":
                return solve(i+1, j+1)

            return False
        return solve(0,0)
            
        
# solution using memoization
# time complexity: O(m*n) where m and n are the lengths of s and p respectively, due to the memoization avoiding redundant calculations.
# space complexity: O(m*n) due to the memoization table and recursion stack in the worst case.

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n1 = len(s)
        n2 = len(p)
        memo = {}
        def solve(i,  j):
            # if pattern is empty, st must also be empty
            key = (i, j)
            if j==n2:
                return i==n1

            if key in memo:
                return memo[key]

            # handle "x*" case (works even if st is empty because we can take 0 occurrences)
            if n2-j >= 2 and p[j+1] == "*":
                # zero occurrences of pattern[0]
                not_take = solve(i, j+2)

                # one or more occurrences (only if st has a char and it matches pattern[0] or pattern[0] is '.')
                take = False
                if i<n1 and (s[i] == p[j] or p[j] == "."):
                    take = solve(i+1, j)

                memo[key] = take or not_take
                return memo[key]

            # normal single-character match (must have st non-empty)
            if i==n1:
                memo[key] = False
                return memo[key]

            # match current characters
            if s[i] == p[j] or p[j] == ".":
                memo[key] = solve(i+1, j+1)
                return memo[key]

            # no match
            memo[key] = False
            return memo[key]
        return solve(0,0)
            
        