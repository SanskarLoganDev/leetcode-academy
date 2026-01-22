# 5. Longest Palindromic Substring

# Neetcode 150 (Important)
# Given a string s, return the longest palindromic substring in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"

# Brute force iterative solution

# Time complexity is O(n²) in worst case (e.g., "aaaaa...") because for each i you may expand O(n).
# Space complexity is O(1) as we only use a constant number of variables (res, res_len, l, r)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res= ""
        res_len = 0
        for i in range(len(s)):
            # odd length substring
            l=i
            r=i
            while l>=0 and r<len(s) and s[l]==s[r]: # expand while characters are equal
                if (r-l+1)>res_len:
                    res_len=r-l+1
                    res=s[l:r+1]
                l-=1
                r+=1
            
            # even length substring
            l=i
            r=i+1
            while l>=0 and r<len(s) and s[l]==s[r]: # expand while characters are equal
                if (r-l+1)>res_len:
                    res_len=r-l+1
                    res=s[l:r+1]
                l-=1
                r+=1
        return res

# Brute force recursive solution
# time complexity O(N^3) as for each substring we are checking if it is palindrome or not which takes O(N) time and there are O(N^2) substrings
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res= ""
        res_len = 0
        def isPalindrome(i, j):
            if i>=j:
                return True

            if s[i]==s[j]:
                return isPalindrome(i+1, j-1)

            return False

        for i in range(n):
            for j in range(i, n):
                if isPalindrome(i, j):

                    if (j-i+1)>res_len:
                        res_len = j-i+1
                        res = s[i:j+1]

        return res
    
# Using top down memoization
# Issue with this approach:
# fails for the following input:
s = "dsqspnkrvrhqzqvovbofdzqishgtcrvckluzpwesvartjhljqdphdupktoxdffvoqupuxmehikegjnwuheoafgqrtvuzphkikaixnjmhepeqorzjzgnrxxxirhjvboijbzftxhvtrdmbcvysxscvqmgifipwujvvktithqthujpxwwgamwqkxnnxiymtuvtyzafbxybalnjboaiyrxedviesmzzwgagilndguylskdikiocvqmjmfykakuiihuqurgqqirjoccqoixegyspftktguitqtixcsywycutcaedusndombnfzpgoklqzzqlkogpzfnbmodnsudeactucywyscxitqtiugtktfpsygexioqccojriqqgruquhiiukakyfmjmqvcoikidkslyugdnligagwzzmseivdexryiaobjnlabyxbfazytvutmyixnnxkqwmagwwxpjuhtqhtitkvvjuwpifigmqvcsxsyvcbmdrtvhxtfzbjiobvjhrixxxrngzjzroqepehmjnxiakikhpzuvtrqgfaoehuwnjgekihemxupuqovffdxotkpudhpdqjlhjtravsewpzulkcvrctghsiqzdfobvovqzqhrvrknpsqsd"

# You are hitting Memory Limit Exceeded because this approach memoizes palindrome status for (almost) every substring.

# Why it blows up

# Your outer loops iterate over all pairs (i, j) with i ≤ j, which is:
# n(n+1)/2 =O(n^2)
# With memoization, memo[(i, j)] stores a boolean for each of those pairs (worst case, nearly all pairs get stored).

# In Python, a dict entry is extremely expensive because it stores:

# the dict hash table entry overhead,

# a tuple object (i, j),

# two int objects i and j (Python ints are objects),

# the boolean.

# Even if you roughly estimate 100–200+ bytes per entry, then:

# if n = 2000, pairs ≈ 2,001,000 → easily 200MB–400MB+

# plus Python runtime overhead → MLE

# That’s exactly what happens on long strings like the one you provided.

# Key point

# Memoization reduces time from ~O(n³) to O(n²), but it does so by storing O(n²) states, and in Python a dict of O(n²) tuple keys is often too large.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res= ""
        res_len = 0
        memo = {}
        def isPalindrome(i, j):
            if i>=j:
                return True

            key = (i, j)
            if key in memo:
                return memo[key]

            if s[i] == s[j]:
                memo[key] = isPalindrome(i+1, j-1)
            else:
                memo[key] = False
            return memo[key]


        for i in range(n):
            for j in range(i, n):
                if isPalindrome(i, j):

                    if (j-i+1)>res_len:
                        res_len = j-i+1
                        res = s[i:j+1]

        return res