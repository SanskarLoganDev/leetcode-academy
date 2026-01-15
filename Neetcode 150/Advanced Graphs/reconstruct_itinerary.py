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

            neighbors = adj.get(from_airport, []) # get the list of possible next airports. We do this instead of iterating directly over adj[from_airport] to avoid issues if the key does not exist
            for i in range(len(neighbors)):
                v = neighbors.pop(i) # choose the next airport to visit. we remove it from the list to avoid using the same ticket again
                if dfs(v):
                    return True # found a valid itinerary
                neighbors.insert(i, v) # backtrack, put the airport back for other paths
            path.pop() # backtrack, what we found was not the correct path
            return False

        dfs("JFK")

        return path
    
# Dry run for the input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]:
   
# DFS + Backtracking trace (step-by-step)

# I will show:
# current from_airport
# what gets appended to path
# which neighbor is popped (ticket “used”)
# how adj changes (because you mutate the lists)

# Call A: dfs("JFK")
# path = ["JFK"]
# adj["JFK"] = ["ATL", "SFO"]
# loop over neighbors indices i = 0..1
# A.i=0
# pop adj["JFK"].pop(0) → "ATL"
# now adj["JFK"] becomes ["SFO"] (ticket JFK→ATL is “used”)
# Recurse into "ATL".

# Call B: dfs("ATL")
# path = ["JFK", "ATL"]
# adj["ATL"] = ["JFK", "SFO"]
# loop i = 0..1
# B.i=0
# pop adj["ATL"].pop(0) → "JFK"
# now adj["ATL"] becomes ["SFO"] (ticket ATL→JFK is “used”)
# Recurse into "JFK".

# Call C: dfs("JFK") (second time)
# Important: adj["JFK"] is currently ["SFO"] because we already popped "ATL" earlier and we have not backtracked.
# path = ["JFK", "ATL", "JFK"]
# adj["JFK"] = ["SFO"]
# loop i = 0..0
# C.i=0
# pop adj["JFK"].pop(0) → "SFO"
# now adj["JFK"] becomes [] (ticket JFK→SFO is “used”)
# Recurse into "SFO".

# Call D: dfs("SFO")
# path = ["JFK", "ATL", "JFK", "SFO"]
# adj["SFO"] = ["ATL"]
# loop i = 0..0
# D.i=0
# pop adj["SFO"].pop(0) → "ATL"
# now adj["SFO"] becomes [] (ticket SFO→ATL is “used”)
# Recurse into "ATL".

# Call E: dfs("ATL") (second time)
# Important: adj["ATL"] is currently ["SFO"] because earlier we popped "JFK" and haven’t restored it.
# path = ["JFK", "ATL", "JFK", "SFO", "ATL"]
# adj["ATL"] = ["SFO"]
# loop i = 0..0
# E.i=0
# pop adj["ATL"].pop(0) → "SFO"
# now adj["ATL"] becomes [] (ticket ATL→SFO is “used”)
# Recurse into "SFO".

# Call F: dfs("SFO") (second time)
# path = ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
# Check: len(path) == no_tickets + 1 → 6 == 6 ✅
# return True

# Now this True bubbles up through all previous calls, and because you return immediately on success, no further backtracking restorations are done (which is fine because we are done).

# Method to reduce time complexity: Hierholzer’s algorithm + lexicographic choice
# Core idea (why it avoids backtracking)

# Instead of guessing the next edge and undoing if it fails, you do this:

# Always take a valid outgoing edge from the current airport (to satisfy lex order, take the smallest).

# Remove that edge permanently (use that ticket).

# Continue until you get stuck (no outgoing edges).

# When you get stuck, add that airport to the itinerary (this is the key) and backtrack to the previous airport.

# The itinerary is built in reverse; reverse it at the end.

# Why “append when stuck” works:

# In an Eulerian traversal, if you reach a node with no remaining outgoing edges, that node must be the end of the remaining trail segment, so it belongs next in the final route.

# This systematically stitches cycles/trails together without exponential trial-and-error.

from typing import List

# time complexity: O(E log E) where E is the number of edges (tickets)
# space complexity: O(E) for the adjacency list and route
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {}

        # 1) Build adjacency list: from -> list of to's
        for u, v in tickets:
            if u not in adj:
                adj[u] = []
            adj[u].append(v)

        # 2) Sort destinations in reverse lexical order
        # so we can pop() the smallest destination in O(1)
        for u in adj:
            adj[u].sort(reverse=True)

        route = []

        def dfs(u: str) -> None:
            # 3) Use all outgoing edges from u
            while u in adj and adj[u]: # we also check u in adj to avoid key error
                v = adj[u].pop()     # pop smallest (because list is reverse-sorted)
                dfs(v)

            # 4) Postorder append: add airport when it has no more outgoing edges
            route.append(u)

        dfs("JFK")
        return route[::-1]

# Key design decisions explained
# 1) Why do we “append after exhausting edges” (postorder)?

# Notice this line is after the while loop:

# route.append(u)


# Meaning: “only add u to the final route when there are no outgoing tickets left from u.”

# This is the crucial Hierholzer idea:

# If you are at airport u and there are no remaining unused tickets leaving u, then u must be the end of the remaining partial itinerary you are constructing.

# So you commit u into the route at that moment.

# This builds the itinerary in reverse order (end to start), so we reverse at the end.

# 2) Why sort in reverse?

# We need the lexicographically smallest itinerary.

# That means: whenever there are multiple choices from an airport, we should choose the smallest destination first.

# In Python lists:

# pop() from the end is O(1).

# pop(0) from the front is O(n) (shifts all elements).

# If we sort destinations in ascending order, the smallest is at index 0, but getting it via pop(0) is slow.

# So we sort in reverse order and do:

# v = adj[u].pop()


# Because in a reverse-sorted list:

# smallest element ends up at the end

# pop() returns that smallest element in O(1)

# Example:

# Destinations: ["ATL", "SFO"]

# Reverse sort → ["SFO", "ATL"]

# pop() → "ATL" (smallest)

# This is a performance decision that matters for avoiding TLE.

# 3) Why while instead of for?

# We are mutating the list (pop() removes edges). A while loop that continues until the list is empty is the cleanest and safest structure:

# while adj[u]:
#     v = adj[u].pop()
#     dfs(v)


# Also, it directly matches the algorithm: “keep using outgoing edges until none remain.”

# Dry run on your example

# Input:

# tickets = [
#   ["JFK","SFO"],
#   ["JFK","ATL"],
#   ["SFO","ATL"],
#   ["ATL","JFK"],
#   ["ATL","SFO"]
# ]

# Step 1: Build adj

# After inserting all tickets:

# adj["JFK"] = ["SFO", "ATL"]

# adj["SFO"] = ["ATL"]

# adj["ATL"] = ["JFK", "SFO"]

# So:

# adj = {
#   "JFK": ["SFO", "ATL"],
#   "SFO": ["ATL"],
#   "ATL": ["JFK", "SFO"]
# }

# Step 2: Reverse sort each adjacency list

# adj["JFK"]: ["SFO", "ATL"] reverse-sorted becomes ["SFO", "ATL"]

# adj["ATL"]: ["JFK", "SFO"] reverse-sorted becomes ["SFO", "JFK"]

# adj["SFO"]: ["ATL"] stays ["ATL"]

# So:

# adj = {
#   "JFK": ["SFO", "ATL"],
#   "ATL": ["SFO", "JFK"],
#   "SFO": ["ATL"]
# }


# (Remember: pop() takes from the end, so this makes us pop the smallest next airport.)

# DFS execution trace

# We start: dfs("JFK"), route = []

# dfs("JFK")

# adj["JFK"] = ["SFO", "ATL"]

# pop() → "ATL" (smallest)
# call dfs("ATL")

# dfs("ATL")

# adj["ATL"] = ["SFO", "JFK"]

# pop() → "JFK" (smallest)
# call dfs("JFK")

# dfs("JFK") (second time)

# adj["JFK"] = ["SFO"] (because "ATL" was popped earlier)

# pop() → "SFO"
# call dfs("SFO")

# dfs("SFO")

# adj["SFO"] = ["ATL"]

# pop() → "ATL"
# call dfs("ATL")

# dfs("ATL") (second time)

# adj["ATL"] = ["SFO"] (because "JFK" was popped earlier)

# pop() → "SFO"
# call dfs("SFO")

# dfs("SFO") (second time)

# adj["SFO"] is now []

# no outgoing edges → route.append("SFO")
# route = ["SFO"]
# return to dfs("ATL") (second time)

# back to dfs("ATL") (second time)

# adj["ATL"] is now []

# append "ATL"
# route = ["SFO", "ATL"]
# return to dfs("SFO") (first time)

# back to dfs("SFO") (first time)

# adj["SFO"] is []

# append "SFO"
# route = ["SFO", "ATL", "SFO"]
# return to dfs("JFK") (second time)

# back to dfs("JFK") (second time)

# adj["JFK"] is []

# append "JFK"
# route = ["SFO", "ATL", "SFO", "JFK"]
# return to dfs("ATL") (first time)

# back to dfs("ATL") (first time)

# adj["ATL"] is [] (we used both edges)

# append "ATL"
# route = ["SFO", "ATL", "SFO", "JFK", "ATL"]
# return to dfs("JFK") (first time)

# back to dfs("JFK") (first time)

# adj["JFK"] is [] (we used both edges)

# append "JFK"
# route = ["SFO", "ATL", "SFO", "JFK", "ATL", "JFK"]
# done

# Now reverse:

# route[::-1] = ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]