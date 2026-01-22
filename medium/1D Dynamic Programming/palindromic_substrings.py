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