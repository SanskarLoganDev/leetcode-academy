# 567. Permutation in String (Neetcode 150) Important

# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false

# Constraints:

# 1 <= s1.length, s2.length <= 104
# s1 and s2 consist of lowercase English letters.


# My inital solution with time complexity O(N+M) where N is the length of s1 and M is the length of s2. 
# The 2nd solution is more optimized.
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        count1 = [0]*26
        count2 = [0]*26
        for s in s1:
            count1[ord(s)-ord('a')]+=1
        l = 0
        r = len(s1)-1
        for i in range(l,r+1):
                count2[ord(s2[i])-ord('a')]+=1
        while r<len(s2):
            if count1==count2:
                return True
            count2[ord(s2[l])-ord('a')]-=1
            l+=1
            r+=1
            if r<len(s2):
                count2[ord(s2[r])-ord('a')]+=1
        return False

# Time complexity: O(N), where N is the length of s2. We traverse s2 once and maintain a sliding window of size len(s1).
# Space complexity: O(1), since we are using a fixed size array of size 26 for the characters a-z.
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        count1 = [0]*26
        count2 = [0]*26
        for i in range(len(s1)):
            count1[ord(s1[i])-ord('a')]+=1
            count2[ord(s2[i])-ord('a')]+=1 # initialize the first window of size len(s1) in s2
        
        if count1==count2:
            return True

        for i in range(len(s1), len(s2)):
            count2[ord(s2[i])-ord('a')]+=1
            count2[ord(s2[i-len(s1)])-ord('a')]-=1 # remove the character that is sliding out of the window, here i-len(s1) is the index of the character that is sliding out of the window
            if count1==count2:
                return True
        return False

# Same solution as above but using a dictionary instead of a list for character counts.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False

        # 1) Build hashmaps for s1 and the first window of s2
        count1 = {}
        count2 = {}
        for i in range(m):
            count1[s1[i]] = count1.get(s1[i], 0) + 1
            count2[s2[i]] = count2.get(s2[i], 0) + 1

        # 2) If they match, we're done
        if count1 == count2:
            return True

        # 3) Slide the window over s2
        for i in range(m, n):
            # add new right char
            count2[s2[i]] = count2.get(s2[i], 0) + 1

            # remove old left char
            ch_out = s2[i - m]
            count2[ch_out] -= 1
            if count2[ch_out] == 0:
                del count2[ch_out]

            # 4) compare maps after each shift
            if count1 == count2:
                return True

        return False
