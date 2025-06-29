# 424. Longest Repeating Character Replacement (Neetcode 150) Important

# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
 
# Constraints:

# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length

# time complexity: O(N), space complexity: O(1) since we are using a fixed size dictionary for the characters A-Z
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        res = 0
        l = 0
        for r in range(len(s)):
            counter[s[r]] = counter.get(s[r],0)+1 # increment the count of the character at index r
            # Check if the current window size minus the count of the most frequent character is greater than k
            if (r-l+1 - max(counter.values()))>k:
                counter[s[l]]-=1 # decrement the count of the character at index l
                l+=1
                
            res = max(res, r-l+1)
        return res