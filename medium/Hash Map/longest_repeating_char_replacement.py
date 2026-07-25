# 424. Longest Repeating Character Replacement 
# (Neetcode 150) Important

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


# Brute force solution
# time complexity: O(N^2), space complexity: O(1) since the counter hashmap will at most have 26 keys

class Solution:
    def longestRepeat(self, s: str, k: int) -> int:
        if len(s)==0:
            return 0
        max_len = 0
        for i in range(len(s)):
            counter = {}
            max_f = 0
            for j in range(i, len(s)):
                counter[s[j]] = counter.get(s[j], 0)+1
                max_f = max(max_f, counter[s[j]]) # the char that is being added can only affect the max freq character so only this character's frequency is tested
                len_substr = j-i+1
                convertable_characters = len_substr - max_f # the other chars that need to be converted
                if convertable_characters<=k:
                    max_len = max(max_len, len_substr)
                else:
                    break
        return max_len

sol = Solution()
ans = sol.longestRepeat("AABABBA", 2)
print(ans)


# time complexity: O(N), space complexity: O(1) since we are using a fixed size dictionary for the characters A-Z    

class Solution:
    def longestRepeat(self, s: str, k: int) -> int:
        if len(s)==0:
            return 0
        max_len = 0
        counter = {}
        l = 0
        max_f = 0
        for i in range(len(s)):
            counter[s[i]] = counter.get(s[i], 0)+1 # increment the count of the character at index i
            max_f = max(max_f, counter[s[i]])
            len_substr = i-l+1
            convertable_chars = len_substr - max_f
            if convertable_chars<=k:
                max_len = max(max_len, len_substr)
            else: # move the left pointer when convertable chars are more than k
                counter[s[l]]-=1 # decrement the count of the character at index l (leftmost in the window)
                l+=1
                max_f = max(counter.values()) # this check can be removed for further optimization
                # as the reduction would decrease the max_f, but we are looking for longer valid substr which would increase
                # the length of substr and thus increase the convertable chars and lead to more invalid cases anyway.

        return max_len


sol = Solution()
ans = sol.longestRepeat("AABABBAB", 2)
print(ans)