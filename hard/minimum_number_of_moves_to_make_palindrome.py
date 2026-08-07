# 2193. Minimum Number of Moves to Make Palindrome

# You are given a string s consisting only of lowercase English letters.

# In one move, you can select any two adjacent characters of s and swap them.

# Return the minimum number of moves needed to make s a palindrome.

# Note that the input will be generated such that s can always be converted to a palindrome.

# Example 1:

# Input: s = "aabb"
# Output: 2
# Explanation:
# We can obtain two palindromes from s, "abba" and "baab". 
# - We can obtain "abba" from s in 2 moves: "aabb" -> "abab" -> "abba".
# - We can obtain "baab" from s in 2 moves: "aabb" -> "abab" -> "baab".
# Thus, the minimum number of moves needed to make s a palindrome is 2.

# Example 2:

# Input: s = "letelt"
# Output: 2
# Explanation:
# One of the palindromes we can obtain from s in 2 moves is "lettel".
# One of the ways we can obtain it is "letelt" -> "letetl" -> "lettel".
# Other palindromes such as "tleelt" can also be obtained in 2 moves.
# It can be shown that it is not possible to obtain a palindrome in less than 2 moves.
 

# Constraints:

# 1 <= s.length <= 2000
# s consists only of lowercase English letters.
# s can be converted to a palindrome using a finite number of moves.

# Time complexity: O(N^2)
# Space complexity: O(N)
class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        s = list(s)
        res = 0
        while s: # O(N)
            i = s.index(s[-1]) # O(N)
            if i==len(s)-1: # if there is only instance of it at the end, for example: abbac, here c needs to move to centreand will need i//2 swaps
                res+=(i//2)
            else: # if there is another instance if the last element, move it to front. For example: abab -> baab, and then pop the front and the back
                res+=i
                s.pop(i) # O(N)
            s.pop()
        return res