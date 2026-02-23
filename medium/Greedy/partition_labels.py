# 763. Partition Labels
# Neetcode 150 (Important)

# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string "ababcc" can be partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.

# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

# Return a list of integers representing the size of these parts.

# Example 1:

# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

# Example 2:

# Input: s = "eccbbbbdec"
# Output: [10]
 
# Constraints:

# 1 <= s.length <= 500
# s consists of lowercase English letters.

from typing import List

# Brute force approach:

# time complexity O(N^2) in worst case where all characters in the string are the same, we are iterating through the string and for each character we are iterating through the string again to find the last occurrence of that character
# space complexity O(N) for the dictionary to store the frequency of each character in the string
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mp = {}
        for c in s:
            if c in mp:
                mp[c]+=1
            else:
                mp[c]=1
        print(mp)
        res = []
        i=0
        j=0
        chars_in_use = set()
        while j<len(s):
            chars_in_use.add(s[j])
            mp[s[j]]-=1
            flag = True
            for char in chars_in_use:
                if mp[char]!=0:
                    flag = False
            if flag:
                res.append(j-i+1)
                chars_in_use = set()
                j+=1
                i = j
            else:
                j+=1
        return res
    

# Optimised approach
# time complexity O(N) where N is the length of the string
# space complexity O(N) for the dictionary to store the last occurrence of each character in the string
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        i = 0
        j = 0
        mp = {}
        for idx in range(len(s)):
            mp[s[idx]] = idx # store the last occurrence of each character in the string
        end = mp[s[j]]
        res = []
        while j<len(s):
            end = max(end, mp[s[j]]) # update the end index to the maximum of the current end index and the last occurrence of the current character
            if j==end:
                res.append(j-i+1) # if the current index is equal to the end index, we have found a partition, so we append the size of the partition to the result list
                i=j+1
            j+=1
        return res

