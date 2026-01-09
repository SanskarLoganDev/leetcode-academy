# 79. Word Search
# Neetcode 150 (Important)

# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example 1:
# https://assets.leetcode.com/uploads/2020/11/04/word2.jpg
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true

# Example 2:
# https://assets.leetcode.com/uploads/2020/11/04/word-1.jpg
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true

# Example 3:
# https://assets.leetcode.com/uploads/2020/10/15/word3.jpg
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
 

# Constraints:

# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.

# Follow up: Could you use search pruning to make your solution faster with a larger board?

# time complexity O(M * N * 3^L) where M,N are dimensions of board and L is length of word: O(mn⋅4^L)
# For each starting cell (m⋅n), the DFS can branch up to 4 directions per step for up to L steps
# Tighter common bound

# After the first move, you typically cannot go back to the immediately previous cell because it’s marked visited ("#"), so the branching factor is at most 3 for subsequent levels:

# First character match: up to 4 choices

# Next characters: up to 3 choices each

# So a tighter bound is:O(mn⋅4⋅3^(L−1))=O(mn⋅3^L)

# space complexity O(L) where L is length of word (recursion stack)
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        def backtracking(i, j, level):
            if level==len(word): # all letters matched
                return True
            if i<0 or i>=m or j<0 or j>=n: # out of bounds
                return False # backtrack
            if board[i][j]=="#": # already visited
                return False # backtrack
            if board[i][j]!=word[level]: # current letter does not match
                return False # backtrack
            temp = board[i][j] # store the current letter
            board[i][j] = "#" # mark as visited
            for d in directions:
                ni = i+d[0]
                nj = j+d[1]

                if backtracking(ni, nj, level+1): # if any path returns true, propagate true upwards
                    return True
            board[i][j] = temp # unmark for backtracking
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0] and backtracking(i, j, 0): # start only if first letter matches
                    return True
        return False
                
                
# Explanation and relation with dfs/bfs
# You are right to notice that this *looks like DFS*, so why do people call it “backtracking”? The most precise answer is:

# * This problem is a **path-existence search** on a grid graph, **but** it is a *stateful* DFS where the state (“which cells are used in the current path”) must be **undone** as you return.
# * That “do a choice → recurse → undo the choice” structure is exactly what “backtracking” means.

# So: it is **DFS + backtracking** (not a vanilla BFS/DFS graph traversal).

# ---

# ## 1) How it differs from a traditional DFS/BFS graph problem

# ### Traditional graph traversal (DFS/BFS)

# Typical DFS/BFS for “visit all nodes” uses a visited set that is **global** for the whole run:

# * Once you visit a node, you mark it visited and you *never unvisit it*.
# * Goal: explore connected component, shortest path (BFS), reachability, etc.

# Example: “Is there any path from A to B in an unweighted graph?”
# You mark visited nodes globally because revisiting them never helps.

# ### This Word Search problem is different

# Here, the constraint is:

# * You may **not reuse a cell in the same path**, but
# * You **may reuse that same cell in a different path** (starting elsewhere, or trying a different branch).

# So “visited” is not a global property of the node. It is **path-dependent**.

# That means:

# * A cell can be “visited” in one recursive branch and must be “unvisited” when exploring other branches.

# This is the main conceptual difference.

# ---

# ## 2) Why BFS is awkward here (and why DFS fits naturally)

# BFS explores many partial paths at once. For this problem, each partial path has its own “visited set”.

# To do BFS correctly, you’d need each queue entry to carry:

# * `(r, c, index_in_word, visited_state_for_that_path)`

# That visited_state explodes in size (exponential number of states), so BFS becomes heavy.

# DFS naturally maintains “current path” via the recursion stack, so path-specific visited tracking is much simpler.

# ---

# ## 3) Why this is a backtracking problem

# Backtracking is not defined by “must output all combinations.”
# Backtracking is defined by:

# > Try a choice, recurse, and if it fails, undo the choice and try another.

# Your code does exactly that:

# 1. **Choose** the cell: match `word[level]` at `(i, j)`
# 2. **Mark it used**: `board[i][j] = "#"`
# 3. **Explore** neighbors recursively
# 4. If no neighbor works, **undo**: `board[i][j] = temp`

# That undo step is the “backtracking” step.

# So even though you are not collecting all solutions, you are still **searching a combinatorial space of possibilities** (possible paths) and backing out when a partial path fails.

# ---

# ## 4) “Traditional backtracking problems are all combinations” — not always

# Many backtracking problems *do* generate all solutions (subsets, permutations, N-Queens).
# But there’s another common category:

# * **Decision backtracking**: “Does there exist at least one solution?”

#   * Word Search is in this category.
#   * Sudoku solver can be either “find one valid fill” (decision) or “find all fills” (enumeration).

# In decision backtracking, you return `True/False` to stop early when you find a valid solution.

# ---

# ## 5) Why does DFS here return True/False, but in “normal DFS” we just return?

# Because the goal is different.

# ### Normal DFS traversal

# Goal: visit nodes / compute something globally (component size, topological order, etc.).
# Return value is often unused; you just recurse and finish.

# ### Here (existence of a specific word path)

# Goal: find **one** valid path.
# Returning `True` means: “Stop searching, solution found.”
# Returning `False` means: “This branch/path attempt failed; try another neighbor.”

# So the return value is used for **pruning and early exit**.

# ---

# ## 6) Visual intuition: this is “path building,” not “node exploring”

# At each step `level`, you need the next character `word[level]`.

# You are not exploring the grid “freely.” You are exploring only moves that keep matching the word prefix.

# That makes the recursion tree look like:

# * level 0: choose a start cell matching word[0]
# * level 1: choose a neighbor matching word[1]
# * level 2: choose a neighbor matching word[2]
# * …
# * level L: success

# Each level is a “decision point.” That is classic backtracking structure.

# ---

# ## 7) Why the “unmark” step is essential

# This line:

# ```python
# board[i][j] = temp
# ```

# is what makes it backtracking.

# If you didn’t restore it:

# * One failed path attempt would permanently block cells for other attempts, causing wrong answers.

# This is why a global visited set does not work here (unless you make it per path).

# ---

# ### Summary in one sentence

# Word Search is a graph path-existence problem with **path-specific constraints**, so it is solved via **DFS with backtracking** (mark/unmark) and uses boolean returns to **stop early** when a valid path is found.

