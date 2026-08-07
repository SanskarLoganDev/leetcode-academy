# 2981. Find Longest Special Substring That Occurs Thrice I
# 2982. Find Longest Special Substring That Occurs Thrice II

# You are given a string s that consists of lowercase English letters.

# A string is called special if it is made up of only a single character. For example, the string "abc" is not special, whereas the strings "ddd", "zz", and "f" are special.

# Return the length of the longest special substring of s which occurs at least thrice, or -1 if no special substring occurs at least thrice.

# A substring is a contiguous non-empty sequence of characters within a string.

# Example 1:

# Input: s = "aaaa"
# Output: 2
# Explanation: The longest special substring which occurs thrice is "aa": substrings "aaaa", "aaaa", and "aaaa".
# It can be shown that the maximum length achievable is 2.

# Example 2:

# Input: s = "abcdef"
# Output: -1
# Explanation: There exists no special substring which occurs at least thrice. Hence return -1.
# Example 3:

# Input: s = "abcaba"
# Output: 1
# Explanation: The longest special substring which occurs thrice is "a": substrings "abcaba", "abcaba", and "abcaba".
# It can be shown that the maximum length achievable is 1.
 

# Constraints for 1:

# 3 <= s.length <= 50
# s consists of only lowercase English letters.

# Constraints for 2:

# 3 <= s.length <= 5 * 105
# s consists of only lowercase English letters.



# time complexity: O(N^3)
# space complexity: O(N^3)

class Solution:
    def maximumLength(self, s: str) -> int:
        special_substrings = []
        ss_counter = {}
        for i in range(len(s)): # O(N)
            ss = s[i]
            special_substrings.append(ss) # O(N)
            for j in range(i+1, len(s)):
                if s[j]!=s[i]:
                    break
                ss+=s[j] # O(current length)
                special_substrings.append(ss) # O(current length)
                
        for strs in special_substrings:
            ss_counter[strs] = ss_counter.get(strs, 0) + 1
        ans = -1
        for ss, count in ss_counter.items():
            if count >= 3:
                ans = max(ans, len(ss)) # the special substring must appear 3 or more times in the string s
        return ans

# Why ss += s[j] costs O(current length)
# The key fact: strings in Python are immutable

# Once a string object is created, it cannot be modified in place. There is no "add a character to the end" operation on the actual memory. So when you write:

# python
# ss = "aaa"
# ss += "a"

# Python does NOT find the existing "aaa" in memory and stick an "a" onto the end of it. Instead, it:

# Allocates a brand new block of memory big enough for "aaaa" (4 characters)
# Copies all 4 characters ('a', 'a', 'a', 'a') into that new memory block
# Points ss at this new object
# The old "aaa" object becomes garbage (eventually collected)

# Space:
# Space complexity tracks how much memory is simultaneously alive/stored, not how much work was done. The critical difference from time: 
#     every one of those intermediate strings gets stored in special_substrings (not discarded), so all those copies persist.

# Further Optimised Solution

# Time: O(N^2)
# Sapce: O(N)

class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        ss_counter = {} # {(char, length): count}
        for i in range(len(s)):
            ch = s[i]
            l = 0
            for j in range(i, len(s)):
                if s[j]!=s[i]:
                    break
                l+=1
                ss_counter[(ch, l)] = ss_counter.get((ch, l), 0) + 1
                
        res = -1
        for char_len, count in ss_counter.items():
            if count>=3:
                res = max(res, char_len[1])

        return res

# Space complexity discussion
# Space Complexity: O(n)

# This is the more interesting part, and it's a great follow-up to your earlier questions about distinguishing "how much work is done" vs "how much is stored."

# Distinct keys, not total insertions
# ss_counter[(ch, l)] = ss_counter.get((ch, l), 0) + 1

# Even though the inner loop runs O(n²) times total (across all i), most of those operations are updating the same key repeatedly, not creating new entries. 
# A dict only grows in size when a new, previously-unseen key is inserted — repeated updates to an existing key just increment the value in place.

# How many distinct (char, length) keys can exist?
# char has at most 26 possible values (lowercase English letters, per typical constraints) — a constant
# length (l) ranges from 1 to at most n (the longest possible run)

# So the maximum number of distinct keys is:
# 26×n=O(n)


# EVEN MORE OPTIMISED !!@!!!@!
# Time complexity: Total time: O(n) + O(26n) = O(26n) = O(n) — since 26 is a fixed constant (bounded by the lowercase English alphabet), 
# it drops out of the asymptotic notation entirely.

# Space complexity: O(n)
# matrix = [[0]*(n+1) for _ in range(26)]

# This allocates a fixed 26 rows, each of length n+1. Total cells: 26 * (n+1). Since 26 is constant: O(26n) = O(n).

class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)

        # matrix[ch][j] = how many times a run of character ch (ord(ch) - ord('a')) reached EXACTLY length j at some position while scanning left to right.
        # (Not the same as "how many times a substring of length j occurs" --
        # that gets reconstructed later via a suffix sum. This just records,
        # per position, the running-length milestone that position completed.)
        matrix = [[0]*(n+1) for _ in range(26)] # 26 alphabets, we have n+1 columns to store the count of character

        # single left-to-right pass, tracking the length of the CURRENT run only
        prev = s[0]
        length = 0
        for i in range(n):
            curr = s[i]
            if curr == prev:
                # still inside the same run -> extend it by one
                length += 1
                matrix[ord(curr)-ord('a')][length] += 1
            else:
                # run broke -> a brand new run of length 1 starts here
                length = 1
                matrix[ord(curr)-ord('a')][length] += 1
                prev = curr
        # this loop is O(n) total: exactly one increment per index, never revisited

        res = -1
        for i in range(26):
            # walk j from the largest possible run length down to 1.
            # cumulativeSum accumulates matrix[i][j] + matrix[i][j+1] + ... + matrix[i][n],
            # which reconstructs "how many occurrences of a length-j substring of
            # this character exist in total" -- because a run of length R contributes
            # exactly (R - j + 1) such occurrences, and it turns out that's exactly
            # how many recorded milestones land at j or above within that run.
            cumulativeSum = 0
            for j in range(n, 0, -1):
                cumulativeSum += matrix[i][j]
                if cumulativeSum >= 3:
                    # found 3+ occurrences at this length -- since we're scanning
                    # from LARGEST j downward, this is the biggest valid length
                    # for this character, so lock it in and stop early.
                    res = max(res, j)
                    break

        return res
    
# Dry run: s = "aaabbbaaa" (n=9)

# i=0: s[0]='a', first char -> length=1, matrix['a'][1] -> 1
# i=1: s[1]='a', same as prev -> length=2, matrix['a'][2] -> 1
# i=2: s[2]='a', same as prev -> length=3, matrix['a'][3] -> 1
# i=3: s[3]='b', new run -> length=1, matrix['b'][1] -> 1
# i=4: s[4]='b', same as prev -> length=2, matrix['b'][2] -> 1
# i=5: s[5]='b', same as prev -> length=3, matrix['b'][3] -> 1
# i=6: s[6]='a', new run -> length=1, matrix['a'][1] -> 2
# i=7: s[7]='a', same as prev -> length=2, matrix['a'][2] -> 2
# i=8: s[8]='a', same as prev -> length=3, matrix['a'][3] -> 2

# Matrix:
# matrix[26][n+1] for s = "aaabbbaaa" (n=9)

#         j=0  j=1  j=2  j=3  j=4  j=5  j=6  j=7  j=8  j=9
# 'a'      0    2    2    2    0    0    0    0    0    0
# 'b'      0    1    1    1    0    0    0    0    0    0
# 'c'      0    0    0    0    0    0    0    0    0    0
#  ...     0    0    0    0    0    0    0    0    0    0
# 'z'      0    0    0    0    0    0    0    0    0    0