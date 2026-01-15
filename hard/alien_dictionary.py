# 269. Alien Dictionary
# Neetcode 150 (Important)

# There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.

# You are given a list of strings words from the alien language's dictionary. Now it is claimed that the strings in words are sorted lexicographically by the rules of this new language.

# If this claim is incorrect, and the given arrangement of string in words cannot correspond to any order of letters, return "".

# Otherwise, return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there are multiple solutions, return any of them.

# Example 1:

# Input: words = ["wrt","wrf","er","ett","rftt"]
# Output: "wertf"

# Example 2:

# Input: words = ["z","x"]
# Output: "zx"

# Example 3:

# Input: words = ["z","x","z"]
# Output: ""
# Explanation: The order is invalid, so return "".
 

# Constraints:

# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of only lowercase English letters.

# DFS Approach
# Time complexity

# Let:

# N = len(words)

# L = max length of a word

# U = number of unique characters (≤ 26 here, but analyze generally)

# E = number of edges in the character graph

# Building the graph

# You compare each adjacent pair of words and scan until first mismatch:

# Worst-case compare up to L chars per pair

# There are N-1 pairs

# Time: O(N · L)

# DFS topo sort

# Each node visited once, each edge explored once:

# Time: O(U + E)

# Total time:

# O(N · L + U + E)
# Given letters are lowercase English, U ≤ 26, E ≤ 26², so DFS part is effectively constant; the dominant term is O(N · L).

# 5) Space complexity

# adj: stores U nodes and E edges → O(U + E)

# visited: up to U entries → O(U)

# recursion stack depth up to U → O(U)

# res: stores U chars → O(U)

# Total:

# O(U + E) (dominant), plus recursion stack O(U).

from typing import List
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {ch:set() for word in words for ch in word}
        
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            m = min(len(w1), len(w2))
            if len(w1)>len(w2) and w1[:m] == w2[:m]:
                return ""
            for j in range(m):
                if w1[j]!=w2[j]:
                    adj[w1[j]].add(w2[j])
                    break                
        # Example adjacency list {w: {e}, e: {r}, r: {t}, t: {f}, f: {}}
        visited = {}
        # Use visited[c] = True to mean: currently in recursion stack (i.e., on the current DFS path).
        # Use visited[c] = False to mean: fully processed (done exploring all neighbors).
        # If during DFS you reach a node that is already True, you found a cycle → invalid ordering.
        
        res = []
        def dfs(c):
            if c in visited:
                return visited[c] # if True, cycle found  
            visited[c] = True # mark as being visited (in recursion stack)

            for v in adj[c]: # visit all neighbors
                if dfs(v): # cycle found
                    return True # propagate True up the call stack

            visited[c] = False # mark as fully processed
            res.append(c) # add to result

        for c in adj:
            if dfs(c):
                return "" # cycle found

        res.reverse() # reverse to get correct order

        return "".join(res)

# 2) Dry run of DFS on ["wrt","wrf","er","ett","rftt"]
# Step A: Build adj

# Unique letters: {w, r, t, f, e} (from all words)

# Initialize:

# adj[w]=∅, adj[r]=∅, adj[t]=∅, adj[f]=∅, adj[e]=∅

# Now compare adjacent words:

# wrt vs wrf

# w==w, r==r, t!=f (first mismatch)

# add edge t -> f

# wrf vs er

# w!=e (first mismatch at index 0)

# add edge w -> e

# er vs ett

# e==e, r!=t

# add edge r -> t

# ett vs rftt

# e!=r

# add edge e -> r

# Final edges:

# w -> e

# e -> r

# r -> t

# t -> f

# So adjacency:

# w: {e}

# e: {r}

# r: {t}

# t: {f}

# f: {}

# This is basically a chain: w → e → r → t → f

# Step B: DFS topo sort with cycle detection

# State variables:

# visited = {} (dict)

# res = []

# Loop: for c in adj:
# (Exact iteration order depends on insertion order of dict; in practice, with this comprehension, it’s the order characters are first encountered in words. For explanation, assume we encounter: w, r, t, f, e or similar. The final valid output can still be wertf.)

# Let’s walk the meaningful path starting with w (because w leads through the whole chain):

# dfs('w')

# visited['w'] = True (on recursion stack)

# neighbors: e → call dfs('e')

# dfs('e')

# visited['e'] = True

# neighbors: r → call dfs('r')

# dfs('r')

# visited['r'] = True

# neighbors: t → call dfs('t')

# dfs('t')

# visited['t'] = True

# neighbors: f → call dfs('f')

# dfs('f')

# visited['f'] = True

# neighbors: none

# mark done: visited['f'] = False

# append to res: res = ['f']

# return (no cycle)

# Back to dfs('t'):

# finished neighbors

# visited['t'] = False

# append: res = ['f','t']

# Back to dfs('r'):

# visited['r'] = False

# append: res = ['f','t','r']

# Back to dfs('e'):

# visited['e'] = False

# append: res = ['f','t','r','e']

# Back to dfs('w'):

# visited['w'] = False

# append: res = ['f','t','r','e','w']

# Now the outer loop continues for other letters, but they’re already in visited with value False, so:

# calling dfs(c) returns visited[c] which is False → no cycle and no extra appends.

# Finally:

# res.reverse() → ['w','e','r','t','f']

# join → "wertf"

# That matches the expected.

# 3) Why cycle detection works in your code

# If you ever revisit a node currently on the path, visited[node] is True, and you immediately return True (cycle found).

# Example cycle case: ["z","x","z"] yields z -> x and x -> z. DFS from z goes to x, from x goes to z which is True → cycle → return "".