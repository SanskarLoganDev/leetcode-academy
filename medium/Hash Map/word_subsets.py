# 916. Word Subsets  Important

# You are given two string arrays words1 and words2.

# A string b is a subset of string a if every letter in b occurs in a including multiplicity.

# For example, "wrr" is a subset of "warrior" but is not a subset of "world".
# A string a from words1 is universal if for every string b in words2, b is a subset of a.

# Return an array of all the universal strings in words1. You may return the answer in any order.

# Example 1:

# Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]

# Output: ["facebook","google","leetcode"]

# Example 2:

# Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["lc","eo"]

# Output: ["leetcode"]

# Example 3:

# Input: words1 = ["acaac","cccbb","aacbb","caacc","bcbbb"], words2 = ["c","cc","b"]

# Output: ["cccbb"]

# Base unoptimised solution
from typing import List

class Solution1:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        res = []
        for i in range(len(words1)):
            flag = True
            for word in words2:
                for k in word:
                    if word.count(k)> words1[i].count(k):
                        flag = False

            if flag:
                res.append(words1[i])

        return res
    
from typing import List

class Solution2:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        res = []
        group = {}
        
        # Build the aggregated frequency requirement from words2:
        # For each letter, store the maximum count it appears in any word from words2.
        for word in words2:
            for char in set(word):  # iterate over unique characters to avoid redundant counts
                group[char] = max(group.get(char, 0), word.count(char))
        
        # Check each word in words1 against the aggregated requirements.
        for word in words1:
            flag = True
            for char in group:
                # If word does not have enough occurrences of char, it's not universal.
                if word.count(char) < group[char]:
                    flag = False
                    break
            if flag:
                res.append(word)
        
        return res

# Example usage:
sol = Solution2()
print(sol.wordSubsets(["amazon","apple","facebook","google","leetcode"], ["e","o"]))   # Expected: ["facebook","google","leetcode"]
print(sol.wordSubsets(["amazon","apple","facebook","google","leetcode"], ["lc","eo"]))   # Expected: ["leetcode"]
print(sol.wordSubsets(["acaac","cccbb","aacbb","caacc","bcbbb"], ["c","cc","b"]))         # Expected: ["cccbb"]

    
