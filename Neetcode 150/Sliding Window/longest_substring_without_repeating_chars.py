# 3. Longest Substring Without Repeating Characters (Neetcode 150) Important

# Given a string s, find the length of the longest substring without duplicate characters.
# topics: Hash Table, Two Pointers, String

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {} # dictionary {"element": "its index in s"}
        max_len = 0
        start = 0  # Left boundary of the current window
        
        for i in range(len(s)):
            # If the character is already seen and is within the current window:
            if s[i] in char_index and char_index[s[i]] >= start: # here we have char_index[s[i]] >= start, to check if the character is within the current window otherwise the value of start will go backwards
                # Move the start to one position after the last occurrence of ch.
                start = char_index[s[i]] + 1
            # Update the last seen index for ch.
            char_index[s[i]] = i
            # Update max_len if the current window is larger.
            max_len = max(max_len, i - start + 1)
        
        return max_len
        