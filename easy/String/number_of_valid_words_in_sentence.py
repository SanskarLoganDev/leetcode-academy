# 2047. Number of Valid Words in a Sentence

# A sentence consists of lowercase letters ('a' to 'z'), digits ('0' to '9'), hyphens ('-'), punctuation marks ('!', '.', and ','), and spaces (' ') only. Each sentence can be broken down into one or more tokens separated by one or more spaces ' '.

# A token is a valid word if all three of the following are true:

# It only contains lowercase letters, hyphens, and/or punctuation (no digits).
# There is at most one hyphen '-'. If present, it must be surrounded by lowercase characters ("a-b" is valid, but "-ab" and "ab-" are not valid).
# There is at most one punctuation mark. If present, it must be at the end of the token ("ab,", "cd!", and "." are valid, but "a!b" and "c.," are not valid).
# Examples of valid words include "a-b.", "afad", "ba-c", "a!", and "!".

# Given a string sentence, return the number of valid words in sentence.

# Example 1:

# Input: sentence = "cat and  dog"
# Output: 3
# Explanation: The valid words in the sentence are "cat", "and", and "dog".

# Example 2:

# Input: sentence = "!this  1-s b8d!"
# Output: 0
# Explanation: There are no valid words in the sentence.
# "!this" is invalid because it starts with a punctuation mark.
# "1-s" and "b8d" are invalid because they contain digits.

# Example 3:

# Input: sentence = "alice and  bob are playing stone-game10"
# Output: 5
# Explanation: The valid words in the sentence are "alice", "and", "bob", "are", and "playing".
# "stone-game10" is invalid because it contains digits.
 

# Constraints:

# 1 <= sentence.length <= 1000
# sentence only contains lowercase English letters, digits, ' ', '-', '!', '.', and ','.
# There will be at least 1 token.

# Time: O(N)
# Space: O(N)
class Solution:
    def countValidWords(self, sentence: str) -> int:
        words = sentence.split(' ')
        valid = 0
        for word in words:
            if len(word)==0:
                continue
            flag = True
            count_hyphen = 0
            for i in range(len(word)):
                if count_hyphen > 1:
                    flag = False
                    break
                elif word[i].isdigit():
                    flag = False
                elif (i==0 or i==len(word)-1) and word[i]=='-':
                    flag = False
                    break
                elif word[i]=='-' and (not word[i-1].isalpha() or not word[i+1].isalpha()):
                    flag = False
                    break
                if word[i]=='-':
                    count_hyphen +=1
                elif i<len(word)-1 and (word[i] == '!' or word[i] == '.' or word[i] == ','):
                    flag = False
                    break
            if flag:
                valid+=1
        return valid
    
import re
# Cleaner solution using regex but same time and space
class Solution:
    def countValidWords(self, sentence: str) -> int:
        pattern = r'([a-z]+(-[a-z]+)?[!.,]?|[!.,])'

        valid = 0

        for word in sentence.split():
            if re.fullmatch(pattern, word):
                valid += 1

        return valid
    
# Breaking down the regex

# Take:

# [a-z]+(-[a-z]+)?[!.,]?
# [a-z]+

# Means:

# one or more lowercase letters

# Examples:

# "a"
# "cat"
# "hello"

# The + means at least one.

# So:

# [a-z]+

# matches:

# cat
# hello
# abc

# but not:

# 123
# -
# !
# (-[a-z]+)?

# This is the optional hyphen portion.

# Inside:

# -

# means literally a hyphen.

# Then:

# [a-z]+

# requires one or more lowercase letters after the hyphen.

# So:

# -[a-z]+

# matches:

# -b
# -game
# -world

# Because this whole part comes after:

# [a-z]+

# we automatically guarantee that the hyphen has a letter before it too.

# For example:

# stone-game

# gets interpreted as:

# stone + -game

# So:

# stone-game ✅

# But:

# -game ❌

# because there are no letters before -.

# And:

# game- ❌

# because there are no letters after -.

# The ? here:

# (-[a-z]+)?

# means:

# this whole hyphen section can appear zero or one time.

# Therefore:

# hello       ✅
# hello-world ✅
# a-b         ✅

# but:

# a-b-c       ❌

# because only one hyphen group is allowed.

# [!.,]?

# This means:

# optionally one punctuation character at the end.

# The brackets:

# [!.,]

# mean:

# match exactly one of !, ., or ,

# And ? means zero or one occurrence.

# So:

# hello   ✅
# hello!  ✅
# hello.  ✅
# hello,  ✅

# but:

# hello!! ❌
# hello,. ❌

# Also, because this appears at the end of the regex, punctuation cannot occur in the middle.

# For example:

# hel!lo

# cannot match:

# [a-z]+(-[a-z]+)?[!.,]?

# because after the !, there are still more characters.