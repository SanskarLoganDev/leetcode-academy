# 1768. Merge Strings Alternately

# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

 

# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# Example 2:

# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s
# Example 3:

# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d

def mergeAlternatively(word1, word2):
    l = min(len(word1), len(word2))
    res = ""
    for i in range(l):
        res+=word1[i]+word2[i]
    if len(word1)>len(word2):
        res+=word1[len(word2):len(word1)]
    if len(word2)>len(word1):
        res+=word2[len(word1):len(word2)]
    return res

print(mergeAlternatively(word1 = "abcd", word2 = "pq"))

def mergeAlternatively2(word1, word2):
    result=[]
    i=0
    while i < len(word1) or i < len(word2):
        if i < len(word1):
            result.append(word1[i])
        if i < len(word2):
            result.append(word2[i])
        i+=1
    return ''.join(result)

print(mergeAlternatively2(word1 = "abcd", word2 = "pq"))