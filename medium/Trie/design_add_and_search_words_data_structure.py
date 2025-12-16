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
        def dfs(j, root):
            cur = root # here we do not start from self.root because we may be in the middle of the trie already
            for i in range(j, len(word)):
                c = word[i] # current character to process
                
                if c==".": # wildcard character
                    for child in cur.children.values(): # explore all possible paths
                        if dfs(i+1, child):
                            return True # if any path returns True, we return True
                    return False # if no paths returned True, we return False
                    
                if c not in cur.children: # character not found in current path
                    return False
            
                cur = cur.children[c] # move to the next node in the trie
            return cur.endOfWord # after processing all characters, check if we are at the end of a valid word

        return dfs(0, self.root) # start DFS from index 0 and root of the trie


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