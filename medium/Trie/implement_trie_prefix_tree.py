# 208. Implement Trie (Prefix Tree)

# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

# Implement the Trie class:

# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

# Example 1:

# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]

# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True
 

# Constraints:

# 1 <= word.length, prefix.length <= 2000
# word and prefix consist only of lowercase English letters.
# At most 3 * 104 calls in total will be made to insert, search, and startsWith.


# Poor mans Trie using list

class Trie:

    def __init__(self):
        self.tries = []

    def insert(self, word: str) -> None: # O(1)
        self.tries.append(word)

    def search(self, word: str) -> bool: # O(n.L) where n is number of words and L is average length of word
        for w in self.tries:
            if word==w:
                return True
        return False

    def startsWith(self, prefix: str) -> bool: # O(n.P) where n is number of words and P is average length of prefix
        flag = True
        if not self.tries:
            return False
        for w in self.tries:
            if len(prefix)>len(w):
                flag = False
                continue
            for i in range(len(prefix)):
                if w[i]!=prefix[i]:
                    flag = False
                    break
                flag = True
            if flag:
                return flag
        return flag


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)