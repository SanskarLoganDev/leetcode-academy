# 49. Group Anagrams (Neetcode)

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:

# Input: strs = [""]

# Output: [[""]]

# Example 3:

# Input: strs = ["a"]

# Output: [["a"]]

# time complexity O(NKlogK) where N is the length of strs and K is the maximum length of a string in strs, since we sort each string.
# space complexity O(NK) for storing the result.

from typing import List
class Solution:
    def groupAnagrams(self, strs):
        anagrams = {}
        for i in range(len(strs)):
            s = "".join(sorted(strs[i]))
            if s not in anagrams:
                anagrams[s] = [strs[i]]
            else:
                anagrams[s].append(strs[i])
        return [x for x in anagrams.values()]

# time complexity O(NK) where N is the length of strs and K is the maximum length of a string in strs, since we count the frequency of each character.
# space complexity O(NK) for storing the result.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)==0:
          return []  
        anagrams = {}
        for string in strs:
            alpha = [0]*26
            for s in string:
                alpha[ord(s)-ord('a')]+=1
            cat = "".join(str(alpha))
            if cat in anagrams:
                anagrams[cat].append(string)
            else:
                anagrams[cat] = [string]
        return [x for x in anagrams.values()]
    
# Conclusion:

# Sorting approach: O(n k log k) time, O(n k) auxiliary space (for the sorted keys).

# Counting‐array approach (current): O(n k) time, O(n) auxiliary space.

# Because the counting‐array version avoids the k log k sort for each string, it is the more efficient solution for grouping anagrams when k is nontrivial.