# 2747. Count Zero Request Servers

# You are given an integer n denoting the total number of servers and a 2D 0-indexed integer array logs, where logs[i] = [server_id, time] denotes that the server with id server_id received a request at time time.

# You are also given an integer x and a 0-indexed integer array queries.

# Return a 0-indexed integer array arr of length queries.length where arr[i] represents the number of servers that did not receive any requests during the time interval [queries[i] - x, queries[i]].

# Note that the time intervals are inclusive.

# Example 1:

# Input: n = 3, logs = [[1,3],[2,6],[1,5]], x = 5, queries = [10,11]
# Output: [1,2]
# Explanation: 
# For queries[0]: The servers with ids 1 and 2 get requests in the duration of [5, 10]. Hence, only server 3 gets zero requests.
# For queries[1]: Only the server with id 2 gets a request in duration of [6,11]. Hence, the servers with ids 1 and 3 are the only servers that do not receive any requests during that time period.

# Example 2:

# Input: n = 3, logs = [[2,4],[2,1],[1,2],[3,1]], x = 2, queries = [3,4]
# Output: [0,1]
# Explanation: 
# For queries[0]: All servers get at least one request in the duration of [1, 3].
# For queries[1]: Only server with id 3 gets no request in the duration [2,4].


# Constraints:

# 1 <= n <= 105
# 1 <= logs.length <= 105
# 1 <= queries.length <= 105
# logs[i].length == 2
# 1 <= logs[i][0] <= n
# 1 <= logs[i][1] <= 106
# 1 <= x <= 105
# x < queries[i] <= 106


# Brute force solution
from typing import List

# Time complexity: O(l*q) where l = len(logs), q = len(queries)
# Space complexity: O(q+n) where n = total servers
# For each query, you create:
# server_set = set()
# This set can contain at most one entry for each server, so its maximum size is: O(N)
# But the set is discarded after that query and recreated for the next query. You do not store Q sets at the same time.
# You also store:
# res
# which contains one answer per query: O(Q)
# Therefore:
# Including the returned result: O(N+Q)

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        res = []
        for i in range(len(queries)):
            server_set = set()
            count = 0
            for log in logs:
                if log[1] < queries[i]-x or log[1] > queries[i]: # if the time is out of range, ignore
                    continue
                if log[0] not in server_set and queries[i]-x<=log[1]<=queries[i]: # if the server has not been counted eariler and the time is within range
                    count+=1
                server_set.add(log[0]) 
            res.append(n-count)
        return res
    
# Optimised approach using sliding window + sorting
# Putting it together
# Time Complexity=O(llogl) + O(plogq) + O(q) + O(l)

# The O(q) and O(l) terms are dominated by their respective log counterparts, so:
# Time Complexity=O(llogl+qlogq)

# Same as the previous solution — this version is just a more verbose way of constructing sorted_queries, with no change to the algorithm's actual complexity.

# Space Complexity: O(l + q + n)
# logs.sort() → Timsort auxiliary space, O(l) worst case
# sorted_queries → explicitly built list of q tuples → O(q)
# ans → O(q)
# hit_count → O(n+1) = O(n)

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key = lambda x: x[1]) # O(lLogl)
        sorted_queries = []
        for i in range(len(queries)): # O(q)
            sorted_queries.append((i, queries[i]))

        sorted_queries.sort(key = lambda x: x[1]) # O(qlogq)
        ans = [0]*len(queries) # needed the because queries are not sorted but answer needs to be returned in the inital query order
        hit_count = [0]*(n+1) # maintains the count of server requests for each server in a range
        servers = 0 # maintains total server count
        i = 0 # pointers for sliding window
        j = 0
        for idx, q in sorted_queries: # O(l)
            # expand: bring in logs with time <= q
            while j<len(logs) and logs[j][1]<=q:
                hit_count[logs[j][0]]+=1
                if hit_count[logs[j][0]]==1: # only increase server count when hit_count==1 to avoid duplicates being counted
                    servers+=1
                j+=1
            # shrink: evict logs now older than q - x
            while i<len(logs) and logs[i][1] < q-x:
                hit_count[logs[i][0]]-=1
                if hit_count[logs[i][0]] == 0:
                    servers-=1
                i+=1
            ans[idx] = n - servers
        return ans
    
# Dry run
# Using n=3, logs=[[1,3],[2,6],[1,5]], x=5, queries=[10,11]. Let's walk through it exactly as it ran.

# Setup

# logs.sort(key=lambda log: log[1]) sorts by time: [[1,3], [1,5], [2,6]] (was [[1,3],[2,6],[1,5]], now time-ordered).

# sorted_queries = sorted(enumerate(queries), key=lambda q: q[1]) gives [(0,10), (1,11)] — already in order here since queries itself happened to be sorted, but the index is preserved either way.

# ans=[0,0], count=[0,0,0,0] (size n+1=4, index 0 unused), servers=0, i=0, j=0.

# Query idx=0, q=10 (window is [10-5, 10] = [5, 10])

# Expand — pull in every log with time <= 10:

# j=0: log=[1,3], time 3 <= 10 → count[1] += 1 → count[1]=1. Since it just went from 0 to 1, server 1 just became active → servers=1. j=1.
# j=1: log=[1,5], time 5 <= 10 → count[1] += 1 → count[1]=2. It was already >=1, so server 1 was already counted as active — servers stays 1. j=2.
# j=2: log=[2,6], time 6 <= 10 → count[2] += 1 → count[2]=1. New active server → servers=2. j=3.
# j=3 now equals len(logs)=3 → expand loop stops.

# Shrink — evict logs older than q-x=5:

# i=0: log=[1,3], time 3 < 5 → yes, too old → count[1] -= 1 → count[1]=1. Since count[1] is still >=1 (server 1 has another log at time 5 still inside the window), servers stays 2. i=1.
# i=1: log=[1,5], time 5 < 5? No (not strictly less) → shrink stops here.

# ans[0] = n - servers = 3 - 2 = 1 ✅ matches expected.

# Query idx=1, q=11 (window is [11-5, 11] = [6, 11])

# Expand: j is already at 3 (== len(logs)), so the while condition fails immediately — nothing new to bring in. This is the entire point of not resetting j between queries: everything with time <= 10 was already absorbed on the previous query, and since 11 > 10, nothing needs to be re-checked.

# Shrink: i=1: log=[1,5], time 5 < 6? Yes → count[1] -= 1 → count[1]=0. Since it just dropped to 0, server 1 is no longer active anywhere in the window → servers -= 1 → servers=1. i=2.
# i=2: log=[2,6], time 6 < 6? No → shrink stops.

# ans[1] = n - servers = 3 - 1 = 2 ✅ matches expected.

# Final: [1, 2] — correct