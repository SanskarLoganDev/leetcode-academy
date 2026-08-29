# 212. Word Search II
# Neetcode 150 (Important)

# Given an m x n board of characters and a list of strings words, return all words on the board.

# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

# Example 1:
# https://assets.leetcode.com/uploads/2020/11/07/search1.jpg
# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]

# Example 2:
# https://assets.leetcode.com/uploads/2020/11/07/search2.jpg
# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []
 
# Constraints:

# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] is a lowercase English letter.
# 1 <= words.length <= 3 * 104
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# All the strings of words are unique.

# Solution uses Backtracking but does not use trie
# Time complexity O(M * N * 3^L * W) where M,N are dimensions of board, L is length of longest word, W is number of words
# From a cell you can try up to 4 neighbors, but once you move, the previous cell is marked '#', so you cannot immediately go back.
# That makes the branching roughly 4 choices for the first step, then at most 3 choices thereafter

# Space complexity O(L) where L is length of longest word (recursion stack)
# res set stores up to W words -> O(W) (output-dependent).
from typing import List
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])
        directions = [(0,1), (0,-1), (1,0), (-1, 0)]
        def backtrack(i, j, level, word): # here word is the current word we are searching for
            if level==len(word): # all letters matched
                return True
            if i<0 or j<0 or i>=m or j>=n: # out of bounds
                return False
            
            if board[i][j]=="#": # already visited
                return False

            if board[i][j]!=word[level]: # current letter does not match
                return False

            temp = board[i][j] # store the current letter
            board[i][j] = '#' # mark as visited
            for d in directions:
                ni = i+d[0]
                nj = j+d[1]
                if backtrack(ni, nj, level+1, word): # move to next letter
                    board[i][j] = temp # restore the letter before returning
                    return True
            board[i][j] = temp # restore the letter before backtracking
            return False
        res = set() # use set to avoid duplicates
        for word in words: # for each word in words list
            for i in range(m): # for each row
                for j in range(n): # for each column
                    if word[0]==board[i][j]: # if first letter matches
                        if backtrack(i, j, 0, word): # start backtracking
                            res.add(word)

        return list(res) # convert set to list
    
# Optimised solution using Trie and Backtracking
# Time complexity O(M * N * 3^L) where M,N are dimensions of board, L is length of longest word
# Space complexity O(L) where L is length of longest word (recursion stack) + O(T) where T is total number of letters in trie

# Why this is a real improvement (not just notation)

# One board traversal instead of W traversals
# The old method repeats essentially the same DFS work separately for each word.
# The trie method explores the board once and “checks all words simultaneously” by following trie prefixes.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def addWord(self, word: str) -> None:
        cur = self # here we have self and not self.root because we are calling this method on the TrieNode itself
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])
        root = TrieNode()
        for word in words:
            root.addWord(word)
        directions = [(0,1), (0,-1), (1,0), (-1, 0)]
        res = set() # use set to avoid duplicates
        visited = set() # to track visited cells during DFS

        def dfs(i, j, curr_node, word): # here word is the word created so far
            if i<0 or j<0 or i>=m or j>=n: # out of bounds
                return
            if (i, j) in visited:
                return
            if board[i][j] not in curr_node.children: # current letter not in trie path
                return

            visited.add((i, j)) # mark as visited
            curr_node = curr_node.children[board[i][j]] # move to the next node in trie
            word+=board[i][j] # append current letter to word
            if curr_node.endOfWord: # found a valid word
                res.add(word) # add to result set

            for d in directions:
                ni = i+d[0]
                nj = j+d[1]

                dfs(ni, nj, curr_node, word) 
            visited.remove((i, j)) # backtrack

        # traverse the grid just once and find all the words in trie if present
        for i in range(m):
            for j in range(n):
                if root.children: # if trie is not empty
                    dfs(i, j, root, "") # start DFS from each cell

        return list(res)