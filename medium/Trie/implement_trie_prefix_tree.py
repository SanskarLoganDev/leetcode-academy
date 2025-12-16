# 208. Implement Trie (Prefix Tree)
# Neetcode 150 (Important)

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

# Using proper Trie structure
# time complexity:
# insert: O(L) where L is length of word
# search: O(L)
# startsWith: O(L)
# space complexity: O(N) where N is number of nodes in Trie

class TrieNode:
    def __init__(self):
        self.children = {} # children["a"] = TrieNode()
        self.endOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode() 

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        if cur.endOfWord:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# Detailed explanation:

# ## 1. Visualizing `insert("apple")` step by step

# We’ll track:

# * `cur` (which node we’re at)
# * `children` maps

# Initially:

# * `root` is a TrieNode
# * `root.children = {}`
# * `root.endOfWord = False`

# ### Call: `insert("apple")`

# ```python
# cur = self.root
# for c in "apple":
#     ...
# cur.endOfWord = True
# ```

# #### Iteration 1: `c = 'a'`

# * Current node: `cur = root`
# * `root.children` **before**: `{}`

# Check:

# ```python
# if 'a' not in root.children:
#     root.children['a'] = TrieNode()
# cur = root.children['a']
# ```

# Now:

# * `root.children = { 'a': NodeA }`
# * NodeA is a new TrieNode:

#   * `NodeA.children = {}`
#   * `NodeA.endOfWord = False`
# * `cur = NodeA`

# You can picture it as:

# * root

#   * `'a'` → NodeA

# #### Iteration 2: `c = 'p'` (first `p`)

# * `cur = NodeA`
# * `NodeA.children` before: `{}`

# Check:

# ```python
# if 'p' not in NodeA.children:
#     NodeA.children['p'] = TrieNode()
# cur = NodeA.children['p']
# ```

# Now:

# * `NodeA.children = { 'p': NodeAP }`
# * NodeAP is new:

#   * `NodeAP.children = {}`
#   * `NodeAP.endOfWord = False`
# * `cur = NodeAP`

# Structure:

# * root

#   * `'a'` → NodeA

#     * `'p'` → NodeAP

# #### Iteration 3: `c = 'p'` (second `p`)

# * `cur = NodeAP` (this represents `"ap"`)
# * `NodeAP.children` before: `{}`

# ```python
# if 'p' not in NodeAP.children:
#     NodeAP.children['p'] = TrieNode()
# cur = NodeAP.children['p']
# ```

# Now:

# * `NodeAP.children = { 'p': NodeAPP }`
# * NodeAPP: `children = {}`, `endOfWord = False`
# * `cur = NodeAPP` (represents `"app"`)

# Structure:

# * root

#   * `'a'` → NodeA

#     * `'p'` → NodeAP

#       * `'p'` → NodeAPP

# #### Iteration 4: `c = 'l'`

# * `cur = NodeAPP`
# * `NodeAPP.children` before: `{}`

# ```python
# if 'l' not in NodeAPP.children:
#     NodeAPP.children['l'] = TrieNode()
# cur = NodeAPP.children['l']
# ```

# Now:

# * `NodeAPP.children = { 'l': NodeAPPL }`
# * `cur = NodeAPPL` (represents `"appl"`)

# #### Iteration 5: `c = 'e'`

# * `cur = NodeAPPL`
# * `NodeAPPL.children` before: `{}`

# ```python
# if 'e' not in NodeAPPL.children:
#     NodeAPPL.children['e'] = TrieNode()
# cur = NodeAPPL.children['e']
# ```

# Now:

# * `NodeAPPL.children = { 'e': NodeAPPLE }`
# * `cur = NodeAPPLE` (represents `"apple"`)

# After the loop:

# ```python
# cur.endOfWord = True
# ```

# So:

# * NodeAPPLE: `endOfWord = True`

# Final structure (each node’s `children` map):

# * `root.children = { 'a': NodeA }`
# * `NodeA.children = { 'p': NodeAP }`
# * `NodeAP.children = { 'p': NodeAPP }`
# * `NodeAPP.children = { 'l': NodeAPPL }`
# * `NodeAPPL.children = { 'e': NodeAPPLE }`
# * `NodeAPPLE.children = {}`, `NodeAPPLE.endOfWord = True`

# Each path from root down through chars spells out the prefix.

# ---

# ## 2. `search("apple")`

# Call:

# ```python
# cur = root
# for c in "apple":
#     if c not in cur.children: return False
#     cur = cur.children[c]
# return cur.endOfWord
# ```

# We walk down the tree using the same maps we built.

# * `c = 'a'`:

#   * `'a' in root.children`? Yes.
#   * `cur = root.children['a']` → NodeA
# * `c = 'p'`:

#   * `'p' in NodeA.children`? Yes.
#   * `cur = NodeA.children['p']` → NodeAP
# * `c = 'p'`:

#   * `'p' in NodeAP.children`? Yes.
#   * `cur = NodeAP.children['p']` → NodeAPP
# * `c = 'l'`:

#   * `'l' in NodeAPP.children`? Yes.
#   * `cur = NodeAPP.children['l']` → NodeAPPL
# * `c = 'e'`:

#   * `'e' in NodeAPPL.children`? Yes.
#   * `cur = NodeAPPL.children['e']` → NodeAPPLE

# Loop ends. Now:

# ```python
# return cur.endOfWord   # NodeAPPLE.endOfWord == True
# ```

# So `search("apple")` returns `True`.

# ---

# ## 3. `search("app")` before inserting `"app"`

# Same logic, but shorter:

# * `cur = root`
# * `c = 'a'` → go to NodeA
# * `c = 'p'` → NodeAP
# * `c = 'p'` → NodeAPP

# End of loop → now `cur = NodeAPP`.

# Check:

# ```python
# return cur.endOfWord
# ```

# NodeAPP `.endOfWord` is currently `False` (we only marked `"apple"`).
# So `search("app")` returns `False`.

# **Important idea:**

# * Being *reachable* as a path from root encodes the **prefix**.
# * `endOfWord = True` encodes that this prefix is a **complete word** that was inserted.

# ---

# ## 4. `startsWith("app")`

# ```python
# cur = root
# for c in "app":
#     if c not in cur.children: return False
#     cur = cur.children[c]
# return True
# ```

# Walk:

# * `'a'` → root.children['a'] = NodeA
# * `'p'` → NodeA.children['p'] = NodeAP
# * `'p'` → NodeAP.children['p'] = NodeAPP

# Loop ends; we don’t check `endOfWord` at all. We just return `True`.

# So `startsWith("app")` is True because that prefix exists as a path in the tree.

# ---

# ## 5. Insert `"app"` and then search `"app"`

# ### `insert("app")`

# Now we insert `"app"`:

# * `cur = root`
# * `'a'`: already in `root.children` → `cur = NodeA`
# * `'p'`: already in NodeA.children → `cur = NodeAP`
# * `'p'`: already in NodeAP.children → `cur = NodeAPP`

# After loop:

# ```python
# cur.endOfWord = True
# ```

# So:

# * NodeAPP.endOfWord becomes **True**.

# Trie structure is the same nodes, but now:

# * NodeAPP.endOfWord = True
# * NodeAPPLE.endOfWord = True

# Now `search("app")`:

# * Walk: root → 'a' → 'p' → 'p' → NodeAPP
# * `return cur.endOfWord` → True

# So now `"app"` and `"apple"` are both recognized as words.

# ---

# ## 6. Why no array of 26 children?

# In many “textbook” trie implementations, each node has:

# ```python
# children = [None] * 26
# ```

# and you index as:

# ```python
# index = ord(c) - ord('a')
# node = node.children[index]
# ```

# You are doing instead:

# ```python
# children = {}   # Python dict
# children[c] = TrieNode()
# ```

# Conceptually they are the same:

# * Both represent a mapping: **character → child node**.
# * The fixed array uses integer indices 0..25.
# * Your dict uses character keys `'a'..'z'` directly.

# Why is dict okay here?

# * Alphabet is small and fixed (26 lowercase letters).
# * Python dict average lookup/insert is O(1).
# * So `c not in cur.children` / `cur.children[c]` behaves like array access in big-O terms.
# * You don’t need to pre-allocate 26 slots in every node; you only store keys actually used.

# TrieNode with dict:

# * Uses **less space** when branching is sparse (not all letters are used at every node).
# * Keeps code more readable in Python.

# Both designs give you:

# * **Insert**: O(L)
# * **Search**: O(L)
# * **StartsWith**: O(L)

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