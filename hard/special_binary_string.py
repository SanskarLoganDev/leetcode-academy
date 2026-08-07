# 761. Special Binary String

# Special binary strings are binary strings with the following two properties:

# The number of 0's is equal to the number of 1's.
# Every prefix of the binary string has at least as many 1's as 0's.
# You are given a special binary string s.

# A move consists of choosing two consecutive, non-empty, special substrings of s, and swapping them. Two strings are consecutive if the last character of the first string is exactly one index before the first character of the second string.

# Return the lexicographically largest resulting string possible after applying the mentioned operations on the string.
 

# Example 1:

# Input: s = "11011000"
# Output: "11100100"
# Explanation: The strings "10" [occuring at s[1]] and "1100" [at s[3]] are swapped.
# This is the lexicographically largest string possible after some number of swaps.

# Example 2:

# Input: s = "10"
# Output: "10"
 

# Constraints:

# 1 <= s.length <= 50
# s[i] is either '0' or '1'.
# s is a special binary string.

# We solve using a recursive divide-and-conquer approach. It scans the string tracking a running balance 
# (total) where 1 = +1 and 0 = -1; every time the balance hits 0, it has found one complete "special" substring (which always has the form 1 + <inner> + 0).
# It recursively solves the inner part of each such substring, collects all these special substrings at the current level, 
# sorts them in descending order (to maximize lexicographic value), and concatenates them.

class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        def solve(strs):
            specials = []
            start = 0
            total = 0
            for i in range(len(strs)):
                total = total + 1 if strs[i]=="1" else total - 1
                if total == 0:
                    # no matter what, sepcial string will start with 1 and end with 0
                    inner = strs[start+1:i]
                    special = "1" + solve(inner) + "0"
                    specials.append(special)
                    start = i+1 # next start would be right next to previous special end
            specials.sort(reverse = True) # descending order to sort it lexicographically

            res = ""
            for special in specials:
                res+=special

            return res

        return solve(s)
    

# solve("11011000")
# │
# │  Scanning: 1(+1=1) 1(+1=2) 0(-1=1) 1(+1=2) 1(+1=3) 0(-1=2) 0(-1=1) 0(-1=0) ← balance hits 0 at i=7
# │  → found special: start=0, i=7, inner = strs[1:7] = "101100"
# │
# └── solve("101100")
#     │
#     │  Scanning: 1(+1=1) 0(-1=0) ← balance hits 0 at i=1
#     │  → found special #1: start=0, i=1, inner = strs[1:1] = ""
#     │
#     ├── solve("")
#     │   │  empty string, loop doesn't run
#     │   │  specials = [], sorted = []
#     │   └── returns ""
#     │
#     │   special #1 = "1" + "" + "0" = "10"
#     │   specials so far = ["10"]
#     │   start moves to 2
#     │
#     │  Scanning continues: 1(+1=1) 1(+1=2) 0(-1=1) 0(-1=0) ← balance hits 0 at i=5
#     │  → found special #2: start=2, i=5, inner = strs[3:5] = "10"
#     │
#     ├── solve("10")
#     │   │
#     │   │  Scanning: 1(+1=1) 0(-1=0) ← balance hits 0 at i=1
#     │   │  → found special: start=0, i=1, inner = strs[1:1] = ""
#     │   │
#     │   ├── solve("")
#     │   │   └── returns ""
#     │   │
#     │   │   special = "1" + "" + "0" = "10"
#     │   │   specials = ["10"]
#     │   │   sort descending = ["10"]
#     │   │   res = "10"
#     │   └── returns "10"
#     │
#     │   special #2 = "1" + "10" + "0" = "1100"
#     │   specials so far = ["10", "1100"]
#     │
#     │   sort descending: compare "1100" vs "10" → '1'='1', '1'>'0' → "1100" wins
#     │   sorted = ["1100", "10"]
#     │   res = "1100" + "10" = "110010"
#     └── returns "110010"

#     special (outer) = "1" + "110010" + "0" = "11100100"
#     specials = ["11100100"]
#     sort descending = ["11100100"] (only one element)
#     res = "11100100"

# returns "11100100"
# ✅ Final Output: "11100100" — matches expected!