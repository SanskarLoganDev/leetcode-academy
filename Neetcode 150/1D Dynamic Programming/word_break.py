# 139. Word Break
# Neetcode 150 (Important)

# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

# Example 1:
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".

# Example 2:
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.

# Example 3:
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
 

# Constraints:

# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.

from typing import List
# Recursive solution
# Time complexity O[(N^2)*(2^N)] in worst case as for each character we are trying to split the string in two parts and 
# “Two choices” reinterpretation (this matches your intuition)
# At each gap between characters, you can conceptually decide:
# Cut here (end the current word), or
# Don’t cut here (keep extending the current word)
# Your code implements this indirectly:
# You “don’t cut” by doing st += rem[i] and continuing the loop
# You “cut” when st in word_set and you recurse on the suffix
# So the “binary choice” exists, but it’s implicit in how the recursion branches when a prefix forms a word.

# 1) Slicing cost
# When you call:
# solve("", rem[i+1:])
# the expression rem[i+1:] creates a new string of length about 
# O(n) in the worst case.
# Along a single deep recursion path, you may slice strings of lengths:
# n+(n−1)+(n−2)+⋯+1=O(n^2)
# So even one path can create O(n^2) total characters across slices.

# space complexity O(N) for recursion stack, Including substring allocations: can be as high as O(N^2)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        def solve(st, rem): # st is current substring being formed, rem is remaining string
            if rem=="": # base case where remaining string is empty
                return True
            for i in range(len(rem)):
                st+=rem[i] # extend current substring
                if st in word_set:
                    if solve("", rem[i+1:]): # slicing is O(N). Here we are slicing rem from i+1 to end
                        return True # found a valid segmentation
            return False
            
        return solve("", s)

# Optmized memoization solution
# Time complexity O(N^3) as for each index we are trying to split the string in two parts and slicing takes O(N)
# Space complexity O(N) for recursion stack + O(N) for memoization dictionary
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        memo = {}  # i -> bool

        def solve(i):
            if i==n: # base case: reached end of string
                return True

            if i in memo:
                return memo[i]

            for j in range(i+1, n+1): # j is the end index of the current substring
                if s[i:j] in word_set and solve(j): # check if substring s[i:j] is in word set and recursively check for remaining string from j to end
                    memo[i] = True
                    return True
            memo[i] = False
            return False

        return solve(0)


# Dry run (every step)
# Setup

# s = "aab"

# indices: 0:'a', 1:'a', 2:'b'

# n = 3

# word_set = {"a", "aa"}

# memo = {}

# Start: solve(0)

# 1) solve(0)

# i = 0

# i == n? 0 == 3 → No

# i in memo? No

# Loop: for j in range(1, 4) → j = 1, 2, 3

# j = 1

# substring s[0:1] = "a"

# "a" in word_set? ✅ Yes

# So evaluate solve(1) (must do this because condition is ... and solve(1))

# ➡️ Call solve(1)

# 2) solve(1)

# i = 1

# i == n? 1 == 3 → No

# i in memo? No

# Loop: for j in range(2, 4) → j = 2, 3

# j = 2

# substring s[1:2] = "a"

# "a" in word_set? ✅ Yes

# Evaluate solve(2)

# ➡️ Call solve(2)

# 3) solve(2)

# i = 2

# i == n? 2 == 3 → No

# i in memo? No

# Loop: for j in range(3, 4) → j = 3 only

# j = 3

# substring s[2:3] = "b"

# "b" in word_set? ❌ No

# Condition fails → do NOT call solve(3)

# Loop ends (no successful split found)

# So:

# memo[2] = False

# return False

# ✅ memo is now: {2: False}

# ⬅️ Back to solve(1) at j=2

# Back to 2) solve(1) (continuing loop)

# We were at:

# j = 2, substring "a" valid, but solve(2) returned False
# So the if condition fails, continue.

# j = 3

# substring s[1:3] = "ab"

# "ab" in word_set? ❌ No

# Condition fails → do NOT call solve(3)

# Loop ends.

# So:

# memo[1] = False

# return False

# ✅ memo now: {2: False, 1: False}

# ⬅️ Back to solve(0) at j=1

# Back to 1) solve(0) (continuing loop)

# We were at:

# j = 1, substring "a" valid, but solve(1) returned False
# So continue to next j.

# j = 2

# substring s[0:2] = "aa"

# "aa" in word_set? ✅ Yes

# Evaluate solve(2)

# ➡️ Call solve(2) again

# 4) solve(2) again (this is where memo is used)

# i = 2

# i == n? No

# i in memo? ✅ YES (memo[2] = False)

# So it executes:

# return memo[2]


# Returns False immediately (memo hit)

# ⬅️ Back to solve(0) at j=2

# Back to 1) solve(0) (continuing loop)

# At j=2:

# "aa" valid but solve(2) is False → condition fails

# j = 3

# substring s[0:3] = "aab"

# "aab" in word_set? ❌ No

# condition fails, no call

# Loop ends.

# So:

# memo[0] = False

# return False

# ✅ Final memo: {2: False, 1: False, 0: False}
# ✅ Final answer: False