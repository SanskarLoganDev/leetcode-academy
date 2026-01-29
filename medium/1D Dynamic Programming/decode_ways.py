# 91. Decode Ways
# Neetcode 150 (Important)

# You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following mapping:

# "1" -> 'A'

# "2" -> 'B'

# ...

# "25" -> 'Y'

# "26" -> 'Z'

# However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes ("2" and "5" vs "25").

# For example, "11106" can be decoded into:

# "AAJF" with the grouping (1, 1, 10, 6)
# "KJF" with the grouping (11, 10, 6)
# The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).
# Note: there may be strings that are impossible to decode.

# Given a string s containing only digits, return the number of ways to decode it. If the entire string cannot be decoded in any valid way, return 0.

# The test cases are generated so that the answer fits in a 32-bit integer.

# Example 1:
# Input: s = "12"
# Output: 2
# Explanation:
# "12" could be decoded as "AB" (1 2) or "L" (12).

# Example 2:
# Input: s = "226"
# Output: 3
# Explanation:
# "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

# Example 3:
# Input: s = "06"
# Output: 0
# Explanation:
# "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06"). In this case, the string is not a valid encoding, so return 0.

# Constraints:

# 1 <= s.length <= 100
# s contains only digits and may contain leading zero(s).

# Using recursion
# time complexity O(2^N) as at each step we have 2 choices and space complexity O(N) for recursion stack
class Solution:
    def numDecodings(self, s: str) -> int:
        def solve(i):
            if i>=len(s):
                return 1
            if s[i] == '0':
                return 0
            ways = solve(i+1)
            if i+1<len(s) and 10<=int(s[i:i+2])<=26:
                ways = ways + solve(i+2)
            return ways

        return solve(0)

            
# Using memoization to optimize the above solution
# time complexity O(N) and space complexity O(N) for recursion stack + O(N)       
class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def solve(i):
            if i>=len(s): # Reached the end successfully
                return 1
            if s[i] == '0': # Leading zero can't be decoded
                return 0
            if i in memo: # Check if already computed
                return memo[i]
            # Take 1 digit
            ways = solve(i+1)
            # Take 2 digits if valid (10..26)
            if i+1<len(s) and 10<=int(s[i:i+2])<=26:
                ways = ways + solve(i+2) # add ways from taking 2 digits
            memo[i] = ways
            return memo[i]

        return solve(0)

# Dry run
# Call trace + memo filling
# Call solve(0) (suffix = "11106")

# s[0] = '1' (not '0')

# Compute:

# 1-digit: solve(1)

# 2-digit: check "11" → 11 is valid → solve(2)

# So we need solve(1) and solve(2).

# Call solve(1) (suffix = "1106")

# s[1] = '1'

# Compute:

# 1-digit: solve(2)

# 2-digit: check "11" → valid → solve(3)

# So we need solve(2) and solve(3).

# Call solve(2) (suffix = "106")

# s[2] = '1'

# Compute:

# 1-digit: solve(3)

# 2-digit: check "10" → 10 is valid → solve(4)

# So we need solve(3) and solve(4).

# Call solve(3) (suffix = "06")

# s[3] = '0' → return 0 immediately

# Because no encoding maps to '0' by itself, and any decoding cannot start with '0'.

# So: solve(3) = 0

# Call solve(4) (suffix = "6")

# s[4] = '6'

# Compute:

# 1-digit: solve(5)

# 2-digit: not possible (no 2 chars left)

# Call solve(5) (suffix = "")

# i == n → return 1

# So:

# solve(4) = solve(5) = 1

# memo[4] = 1

# Memo so far: {4: 1}

# Return to solve(2)

# We now have:

# 1-digit path: solve(3) = 0

# 2-digit "10" path: solve(4) = 1

# So:

# solve(2) = 0 + 1 = 1

# memo[2] = 1

# Memo so far: {4: 1, 2: 1}

# Return to solve(1)

# Compute:

# 1-digit path: solve(2) → memo hit = 1

# 2-digit "11" path: solve(3) = 0 (leading zero case)

# So:

# solve(1) = 1 + 0 = 1

# memo[1] = 1

# Memo so far: {4: 1, 2: 1, 1: 1}

# Return to solve(0)

# Compute:

# 1-digit path: solve(1) → memo hit = 1

# 2-digit "11" path: solve(2) → memo hit = 1

# So:

# solve(0) = 1 + 1 = 2

# memo[0] = 2

# Final memo: {4: 1, 2: 1, 1: 1, 0: 2}
# Answer: 2

# What are the 2 valid decodings?

# "11106" can be split as:

# 1 | 1 | 10 | 6 → A A J F

# 11 | 10 | 6 → K J F

# Invalid splits get blocked by the '0' rule, e.g.:

# 1 | 11 | 06 ❌ because "06" starts with '0' (not a valid code)

        