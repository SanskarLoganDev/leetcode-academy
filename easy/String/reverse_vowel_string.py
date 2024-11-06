# 345 REVERSE VOWELS OF A STRING

# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "IceCreAm"

# Output: "AceCreIm"

# Explanation:

# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:

# Input: s = "leetcode"

# Output: "leotcede"

# My solution

def reverseVowels(s):
    vowel = ['a','e','i','o','u']
    left = 0
    right = len(s)-1
    s= [x for x in s] # for a long string, this takes a lot of time
    print(s)
    while left<right:
        if s[left].lower() in vowel and s[right].lower() in vowel:
            temp = s[left]
            s[left]=s[right]
            s[right]=temp
            left+=1
            right-=1
            continue

        elif s[left].lower() in vowel and s[right].lower() not in vowel:
            right-=1
            continue
        elif s[left].lower() not in vowel and s[right].lower() in vowel:
            left+=1
            continue
        left+=1
        right-=1
    str1 = ""
    for i in s: # for a long string, this takes a lot of time
        str1+=i
    
    return str1

print(reverseVowels("leetcode"))


# Optimised solution

def reverseVowels2(s):
    s=list(s)
        # Convert string into array of individual string characters - easier to work with. 
    n=len(s)
    left=0
    right=n-1
    vowels=set('AEIOUaeiou')
    # Use of 2 pointers. 
    while left<right:
        while left<right and s[left] not in vowels:
            left+=1
        while left<right and s[right] not in vowels:
            right-=1
        s[left],s[right]=s[right],s[left] # quick swapping
        left+=1
        right-=1
    s=''.join(s)
    return s
print(reverseVowels2("leetcode"))