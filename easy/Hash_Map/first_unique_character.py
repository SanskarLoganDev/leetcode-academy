# 387. First Unique Character in a String

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

# Example 1:

# Input: s = "leetcode"

# Output: 0

# Explanation:

# The character 'l' at index 0 is the first character that does not occur at any other index.

# Example 2:

# Input: s = "loveleetcode"

# Output: 2

# Example 3:

# Input: s = "aabb"

# Output: -1

def firstUniqChar(s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        count = Counter(s)
        for char in s:
            if count[char]==1:
                return s.index(char)
        return -1
    
print(firstUniqChar("aabb"))

def firstUniqChar2(s):
        """
        :type s: str
        :rtype: int
        """
        for char in s:
            if s.count(char)==1:
                return s.index(char)
        return -1
    
print(firstUniqChar("loveleetcode"))