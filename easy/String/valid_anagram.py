# 242. Valid Anagram

# Given two strings s and t, return true if t is an 
# anagram
#  of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

def validAnagram(s,t):
    if len(s)!=len(t):
            return False
    s=''.join(sorted(s)) # sorted has the time complexity of O(NlogN)
    t=''.join(sorted(t))
    return s==t

print(validAnagram("anagram", "nagaram"))

# Alternate Way (Optimised) O(N+M) where N is the length of s and M is the length of t:

def isAnagram(s, t):
    return all(s.count(x) == t.count(x) for x in 'abcdefghijklmnopqrstuvwxyz')