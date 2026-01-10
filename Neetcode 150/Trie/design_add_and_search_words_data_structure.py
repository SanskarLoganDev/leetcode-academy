# 211. Design Add and Search Words Data Structure
# Neetcode 150 (Important)

# Design a data structure that supports adding new words and finding if a string matches any previously added string.

# Implement the WordDictionary class:

# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

# Example:

# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]

# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
 

# Constraints:

# 1 <= word.length <= 25
# word in addWord consists of lowercase English letters.
# word in search consist of '.' or lowercase English letters.
# There will be at most 2 dots in word for search queries.
# At most 104 calls will be made to addWord and search.

# Uses the concept of DFS and Backtracking on a Trie data structure
# time complexity: O(M∗26^N) where M is length of the word being searched, N is number of wildcards in the word
# space complexity: O(N) where N is number of nodes in the trie

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(j, root): # here j is the index of the character in the word we are processing
            cur = root # here we do not start from self.root because we may be in the middle of the trie already
            for i in range(j, len(word)):
                c = word[i] # current character to process
                
                if c==".": # wildcard character
                    for child in cur.children.values(): # explore all possible paths
                        if dfs(i+1, child): # we do i+1 because we move to the next character in the word
                            return True # if any path returns True, we return True
                    return False # if no paths returned True, we return False
                    
                if c not in cur.children: # character not found in current path
                    return False
            
                cur = cur.children[c] # move to the next node in the trie
            return cur.endOfWord # after processing all characters, check if we are at the end of a valid word

        return dfs(0, self.root) # start DFS from index 0 of the word and root of the trie


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# Unoptimized search using list:
# time complexity: O(N*M) where N is number of words added and M is length of the word being searched
# space complexity: O(N*M)
class WordDictionary:

    def __init__(self):
        self.res = []

    def addWord(self, word: str) -> None:
        self.res.append(word)

    def search(self, word: str) -> bool:
        if word in self.res: # direct match found
            return True
        
        if not self.res: # empty list, no words added
            return False
        
        for i in range(len(self.res)):
            if len(self.res[i])!=len(word):
                continue # length mismatch, continue checking next word
            flag = True
            for j in range(len(word)):
                if word[j]==".": # wildcard character, skip comparison
                    continue
                if word[j]!=self.res[i][j]: # character mismatch
                    flag = False # set flag to False and break inner loop
                    break
            if flag: # all characters matched
                return True
        return False # no matching word found

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# Dry run with the given example
# Setup

# Operations:

# addWord("bad")
# addWord("dad")
# addWord("mad")


# Trie after additions (conceptually):

# (root)
#  ├── b
#  │    └── a
#  │         └── d  (endOfWord=True)
#  ├── d
#  │    └── a
#  │         └── d  (endOfWord=True)
#  └── m
#       └── a
#            └── d  (endOfWord=True)

# A) search("pad") → expected False

# Call: dfs(0, root)

# j=0, cur=root

# Loop i=0, c='p'

# 'p' not in root.children → return False

# So search("pad") = False.

# B) search("bad") → expected True

# Call: dfs(0, root)

# i=0, c='b' exists → cur = node('b')

# i=1, c='a' exists → cur = node('a')

# i=2, c='d' exists → cur = node('d')

# loop ends → return cur.endOfWord = True

# So search("bad") = True.

# C) search(".ad") → expected True

# Call: dfs(0, root)

# i=0, c='.' wildcard

# We must try all children of root: b, d, m

# So we run:

# Try child = b:

# Call dfs(i+1=1, node('b'))

# Inside this call:

# j=1, cur = node('b')

# i=1, c='a' exists → cur=node('a')

# i=2, c='d' exists → cur=node('d')

# end → return cur.endOfWord = True

# Because this returned True, the original call immediately returns True (short-circuit).

# So search(".ad") = True.

# (If b had failed, it would then try d, then m.)

# Call tree for search(".ad")

# Pattern = . a d (indices 0,1,2)

# Start:

# dfs(0, root)   pattern: [. a d]
#   i=0 sees '.' → branch over children of root: {b, d, m}


# Branches:

# dfs(0, root)
# ├─ try child 'b' → dfs(1, node('b'))   pattern: . [a d]
# │    i=1 'a' exists → move to node('a')
# │    i=2 'd' exists → move to node('d')
# │    end of pattern → return endOfWord(True)
# │  → True
# │
# ├─ try child 'd' → dfs(1, node('d'))   pattern: . [a d]
# │    (this branch would also return True, but never executed because we already got True)
# │
# └─ try child 'm' → dfs(1, node('m'))   pattern: . [a d]
#      (same; not executed due to short-circuit)

# Key observation

# As soon as the 'b' branch returns True, your code immediately returns True and does not explore 'd' or 'm'.


# D) search("b..") → expected True

# Call: dfs(0, root)

# i=0, c='b' exists → cur=node('b')

# i=1, c='.' wildcard

# Explore all children of node('b')
# Node('b') has only child 'a'

# Try child = a:

# Call dfs(i+1=2, node('a'))

# Inside:

# j=2, cur=node('a')

# i=2, c='.' wildcard again

# Explore all children of node('a')
# Node('a') has only child 'd'

# Try child = d:

# Call dfs(i+1=3, node('d'))

# Inside:

# j=3, and len(word)=3, so the for-loop does not run

# return cur.endOfWord

# node('d').endOfWord = True → returns True

# This True bubbles up:

# dfs(3, d) True → dfs(2, a) True → dfs(0, root) True

# So search("b..") = True.

# Call tree for search("b..")

# Pattern = b . . (indices 0,1,2)

# Start:

# dfs(0, root)   pattern: [b . .]
#   i=0 sees 'b' → follow 'b' edge (no branching)
#   i=1 sees '.' → branch over children of node('b')


# Tree:

# dfs(0, root)
#   i=0 'b' exists → cur = node('b')
#   i=1 '.' → branch over children of node('b') = {'a'}
#   └─ try child 'a' → dfs(2, node('a'))   pattern: b . [.]
#        i=2 '.' → branch over children of node('a') = {'d'}
#        └─ try child 'd' → dfs(3, node('d'))   pattern: b . . [end]
#             (loop doesn't run; j == len(word))
#             return endOfWord(True)
#           → True
#      → True
# → True