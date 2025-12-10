# 332. Reconstruct Itinerary
# Neetcode 150 (Important)

# You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

# All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

# For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

# Example 1:
# https://assets.leetcode.com/uploads/2021/03/14/itinerary1-graph.jpg

# Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# Output: ["JFK","MUC","LHR","SFO","SJC"]

# Example 2:
# https://assets.leetcode.com/uploads/2021/03/14/itinerary2-graph.jpg

# Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
 

# Constraints:

# 1 <= tickets.length <= 300
# tickets[i].length == 2
# fromi.length == 3
# toi.length == 3
# fromi and toi consist of uppercase English letters.
# fromi != toi



# Approach: Backtracking + DFS
# Time complexity: Preprocessing: O(n log n)

# DFS/backtracking (dominant):

# States: Θ(n!)
# Work per state: O(n^2) (due to pop(i) / insert(i, v) on lists of size up to n)

# → Worst-case time: 𝑂(𝑛^2⋅𝑛!)

# Space:

# adj + path + recursion stack: O(n)
# space: O(E) for the adjacency list and path

from typing import List
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        no_tickets = len(tickets)

        adj = {}
        for u, v in tickets: # build the adjacency list but using a dictionary this time as the nodes are strings not integers
            if u in adj:
                adj[u].append(v)
            else:
                adj[u] = [v]

        for key in adj:
            adj[key].sort()
        path = [] # to store the final itinerary

         # backtracking + DFS
        
        def dfs(from_airport):
            path.append(from_airport)
            if len(path) == no_tickets+1:
                return True # found a valid itinerary

            neighbors = adj[from_airport]
            for i in range(len(neighbors)):
                v = neighbors.pop(i) # choose the next airport to visit. we remove it from the list to avoid using the same ticket again
                if dfs(v):
                    return True # found a valid itinerary
                neighbors.insert(i, v) # backtrack, put the airport back for other paths
            path.pop() # backtrack, what we found was not the correct path
            return False

        dfs("JFK")

        return path