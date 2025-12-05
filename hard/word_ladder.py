# 127. Word Ladder
# Neetcode 150 (Important) Hard

# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

# Example 1:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

# Example 2:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

# Constraints:

# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.

from typing import List
from collections import deque

# This is not a regular Graph problem that we usually see. Here we have to generate the graph on the fly by changing one letter at a time and checking if the new word is in the wordList or not.
# We can use BFS to find the shortest path from beginWord to endWord.

# time complexity:O(L · N² · 26) where N is the number of words in wordList, L is the length of each word, and 26 is for each letter in the alphabet.
# space complexity: O(N) for the queue and set

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: # if endWord is not in wordList then return 0
            return 0
        wordList.append(beginWord) # add beginWord to wordList to consider it in the transformations
        q = deque()
        q.append((beginWord, 1)) # word and level
        set1 = set()
        set1.add(beginWord) # to keep track of visited words

        while q:
            word, level = q.popleft() # current word and level
            for i in range(len(word)): # loop through each character in the word
                for j in range(ord('a'), ord('z')+1): # change each character to every possible character from a to z
                    new_word = word[:i]+chr(j)+word[i+1:] # generate new word by changing one character
                    if new_word == endWord:
                        return level+1
                    if new_word not in set1 and new_word in wordList: # if new word is not visited and is in wordList
                        set1.add(new_word) # mark new word as visited
                        q.append((new_word, level+1)) # add new word to queue with level+1
        return 0 # if we reach here then there is no transformation sequence from beginWord to endWord
            
# Time complexity explanation:
# For each word you pull from the queue:

# You generate at most 26 * L new_words (each position, each letter).

# For each new_word you do:

# new_word not in set1 → average O(1) (set lookup)

# new_word in wordList → O(N) (because wordList is still a list)

# So each new_word check costs O(N) because of the wordList membership test.

# Per popped word:

# 26 * L (neighbors) × O(N) (membership in wordList) = O(26 * L * N) = O(L * N)


# In the worst case, BFS will eventually pop all reachable words, i.e. up to N words.

# So total BFS cost:

# O(N) words popped × O(L * N) work per word = O(L * N^2)


# Add the initial O(N) check for endWord in wordList, and the total is still:

# Time Complexity: O(L · N²)
