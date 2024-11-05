# 290. WORD PATTERN

# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.

# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"

# Output: true

# Explanation:

# The bijection can be established as:

# 'a' maps to "dog".
# 'b' maps to "cat".
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"

# Output: false

# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"

# Output: false

def wordPattern(pattern, s):
    word_map = {}
    s = s.split()
    if len(s)!=len(pattern):
        return False
            
    for i in range(len(pattern)):
        if pattern[i] not in word_map and s[i] not in word_map.values():
            word_map[pattern[i]]=s[i]
        elif pattern[i] not in word_map and s[i] in word_map.values():
            return False
        elif word_map[pattern[i]]!=s[i]:
            return False
    return True

print(wordPattern(pattern = "abba", s = "dog dog dog dog"))
            