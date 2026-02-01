# 647. Palindromic Substrings
# Neetcode 150 (Important)

# Given a string s, return the number of palindromic substrings in it.

# A string is a palindrome when it reads the same backward as forward.

# A substring is a contiguous sequence of characters within the string.

# Example 1:

# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".

# Example 2:

# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

# Constraints:

# 1 <= s.length <= 1000
# s consists of lowercase English letters.

# Brute force recursive solution
# time complexity O(N^3) as for each substring we are checking if it is palindrome or not which takes O(N) time and there are O(N^2) substrings
class Solution:
    def countSubstrings(self, s: str) -> int:
        def isPalindrome(i, j):
            if i>=j: # when indices cross each other meaning all characters have been checked
                return True

            if s[i]==s[j]: # when characters are equal
                return isPalindrome(i+1, j-1) # check for inner substring
            return False
        count = 0
        for i in range(len(s)): # iterate for all substrings
            for j in range(i, len(s)): # j starts from i to consider all substrings starting from i
                    if isPalindrome(i, j):
                        count+=1
        return count
    
    
# Brute force recursive solution with memoization
# time complexity O(N^2) as we are storing already computed results of isPalindrome in a dictionary to avoid recomputation
# space complexity O(N^2) for the memoization dictionary

class Solution:
    def countSubstrings(self, s: str) -> int:
        memo = {} # to store already computed results of isPalindrome
        def isPalindrome(i, j):
            if i>=j:
                return True
            key = (i, j)
            if key in memo:
                return memo[key]
            if s[i]==s[j]:
                memo[key] = isPalindrome(i+1, j-1) # memoize the result
                return memo[key]
            memo[key] = False # we mark as false if characters are not equal
            return memo[key] # memoize the result
        count = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                    if isPalindrome(i, j): # check if substring s[i:j+1] is palindrome
                        count+=1
        return count
    
    
# Dry run using recursion
# Example 1: s = "abc"

# Indices:
# 0:'a', 1:'b', 2:'c'
# We loop all substrings using (i, j):

# i = 0

# j = 0 → substring "a"

# isPalindrome(0,0) → i>=j True → palindrome ✅

# count = 1

# j = 1 → substring "ab"

# isPalindrome(0,1)

# compare s[0]='a' vs s[1]='b' mismatch → False ❌

# count stays 1

# j = 2 → substring "abc"

# isPalindrome(0,2)

# compare s[0]='a' vs s[2]='c' mismatch → False ❌

# count stays 1

# i = 1

# j = 1 → substring "b"

# isPalindrome(1,1) → base True ✅

# count = 2

# j = 2 → substring "bc"

# isPalindrome(1,2)

# compare s[1]='b' vs s[2]='c' mismatch → False ❌

# count stays 2

# i = 2

# j = 2 → substring "c"

# isPalindrome(2,2) → base True ✅

# count = 3

# ✅ Final output: 3 ("a","b","c")


# Example 2: s = "aaa"
# Indices:
# 0:'a', 1:'a', 2:'a'

# All substrings:

# i = 0

# j = 0 → "a"

# isPalindrome(0,0) → True ✅

# count = 1

# j = 1 → "aa"

# isPalindrome(0,1)

# s[0] == s[1] ('a'=='a') → call isPalindrome(1,0)

# isPalindrome(1,0) base i>=j True

# so isPalindrome(0,1) True ✅

# count = 2

# j = 2 → "aaa"

# isPalindrome(0,2)

# compare s[0] and s[2] ('a'=='a') → call isPalindrome(1,1)

# isPalindrome(1,1) base True

# so isPalindrome(0,2) True ✅

# count = 3

# i = 1

# j = 1 → "a"

# isPalindrome(1,1) True ✅

# count = 4

# j = 2 → "aa"

# isPalindrome(1,2)

# s[1]==s[2] → call isPalindrome(2,1) base True

# so True ✅

# count = 5

# i = 2

# j = 2 → "a"

# isPalindrome(2,2) True ✅

# count = 6

# ✅ Final output: 6 ("a","a","a","aa","aa","aaa")


# Dry run using memoization
# Part B — Memoized recursion solution

# The loop is the same, but isPalindrome(i,j) stores results in:

# memo[(i,j)] = True/False


# So if the same (i,j) is checked again, we return instantly.

# Important: In these examples, most (i,j) pairs are only checked once by the loop, but memo helps a lot on bigger strings because recursive calls like (i+1, j-1) get reused across different outer checks.

# Example 1: s = "abc"

# We will see memo entries for non-trivial pairs; base cases (i>=j) are not stored (your code returns True directly).

# Start: memo = {}, count = 0

# i=0

# j=0: isPalindrome(0,0) → base True ✅ count=1

# j=1: isPalindrome(0,1)

# key (0,1) not in memo

# s[0]!=s[1] → memo[(0,1)] = False

# return False ❌

# j=2: isPalindrome(0,2)

# key (0,2) not in memo

# s[0]!=s[2] → memo[(0,2)] = False

# return False ❌

# i=1

# j=1: base True ✅ count=2

# j=2: isPalindrome(1,2)

# key (1,2) not in memo

# s[1]!=s[2] → memo[(1,2)] = False

# return False ❌

# i=2

# j=2: base True ✅ count=3

# Final:

# count = 3

# memo = {(0,1):False, (0,2):False, (1,2):False}

# Example 2: s = "aaa"

# Start: memo = {}, count=0

# i=0

# j=0: base True ✅ count=1

# j=1: isPalindrome(0,1)

# (0,1) not in memo

# s[0]==s[1] → need isPalindrome(1,0)

# (1,0) is base True

# memo[(0,1)] = True

# return True ✅ count=2

# j=2: isPalindrome(0,2)

# (0,2) not in memo

# s[0]==s[2] → need isPalindrome(1,1)

# base True

# memo[(0,2)] = True

# return True ✅ count=3

# i=1

# j=1: base True ✅ count=4

# j=2: isPalindrome(1,2)

# (1,2) not in memo

# s[1]==s[2] → need isPalindrome(2,1) base True

# memo[(1,2)] = True

# return True ✅ count=5

# i=2

# j=2: base True ✅ count=6

# Final:

# count = 6

# memo = {(0,1):True, (0,2):True, (1,2):True}