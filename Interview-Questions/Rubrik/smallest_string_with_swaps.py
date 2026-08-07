# 1202. Smallest String With Swaps

# You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

# You can swap the characters at any pair of indices in the given pairs any number of times.

# Return the lexicographically smallest string that s can be changed to after using the swaps.

# Example 1:

# Input: s = "dcab", pairs = [[0,3],[1,2]]
# Output: "bacd"
# Explaination: 
# Swap s[0] and s[3], s = "bcad"
# Swap s[1] and s[2], s = "bacd"
# Example 2:

# Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
# Output: "abcd"
# Explaination: 
# Swap s[0] and s[3], s = "bcad"
# Swap s[0] and s[2], s = "acbd"
# Swap s[1] and s[2], s = "abcd"
# Example 3:

# Input: s = "cba", pairs = [[0,1],[1,2]]
# Output: "abc"
# Explaination: 
# Swap s[0] and s[1], s = "bca"
# Swap s[1] and s[2], s = "bac"
# Swap s[0] and s[1], s = "abc"
 

# Constraints:

# 1 <= s.length <= 10^5
# 0 <= pairs.length <= 10^5
# 0 <= pairs[i][0], pairs[i][1] < s.length
# s only contains lower case English letters.

from typing import List
from collections import deque


# Time complexity: O(n! · P · n)

# Breaking this down from the code itself:

# V = number of distinct strings ever added to visited (and thus processed from queue). 
# In the worst case — all n characters distinct, all indices connected via pairs — this is n!, as just confirmed.

# For each dequeued string, the inner loop runs once per pair: for a, b in pairs, so P = len(pairs) iterations.

# Each iteration does list(current) (O(n)), a swap (O(1)), ''.join(chars) (O(n)), a set membership check new_s not in visited (O(n) to hash a string of length n), 
# and possibly visited.add(new_s) (also O(n) to hash). So each pair-swap attempt costs O(n).

# Space complexity
# visited (a set) and queue (a deque) can each hold up to V = n! distinct strings in the worst case, 
# and each string itself takes O(n) space to store — giving O(n! · n) total.

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        q = deque()
        q.append(s)
        visited = set()
        visited.add(s)
        smallest = s
        while q:
            curr = q.popleft()
            if curr<smallest: # compares lexicographically
                smallest = curr
            for i, j in pairs:
                curr_list = list(curr)
                curr_list[i], curr_list[j] = curr_list[j], curr_list[i]
                curr_str = "".join(curr_list)
                if curr_str not in visited:
                    q.append(curr_str)
                    visited.add(curr_str)
        return smallest
    

