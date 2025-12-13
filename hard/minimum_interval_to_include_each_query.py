# 1851. Minimum Interval to Include Each Query
# Neetcode 150 (Important)

# You are given a 2D integer array intervals, where intervals[i] = [lefti, righti] describes the ith interval starting at lefti and ending at righti (inclusive). The size of an interval is defined as the number of integers it contains, or more formally righti - lefti + 1.

# You are also given an integer array queries. The answer to the jth query is the size of the smallest interval i such that lefti <= queries[j] <= righti. If no such interval exists, the answer is -1.

# Return an array containing the answers to the queries.

# Example 1:

# Input: intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
# Output: [3,3,1,4]
# Explanation: The queries are processed as follows:
# - Query = 2: The interval [2,4] is the smallest interval containing 2. The answer is 4 - 2 + 1 = 3.
# - Query = 3: The interval [2,4] is the smallest interval containing 3. The answer is 4 - 2 + 1 = 3.
# - Query = 4: The interval [4,4] is the smallest interval containing 4. The answer is 4 - 4 + 1 = 1.
# - Query = 5: The interval [3,6] is the smallest interval containing 5. The answer is 6 - 3 + 1 = 4.

# Example 2:

# Input: intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]
# Output: [2,-1,4,6]
# Explanation: The queries are processed as follows:
# - Query = 2: The interval [2,3] is the smallest interval containing 2. The answer is 3 - 2 + 1 = 2.
# - Query = 19: None of the intervals contain 19. The answer is -1.
# - Query = 5: The interval [2,5] is the smallest interval containing 5. The answer is 5 - 2 + 1 = 4.
# - Query = 22: The interval [20,25] is the smallest interval containing 22. The answer is 25 - 20 + 1 = 6.
 

# Constraints:

# 1 <= intervals.length <= 105
# 1 <= queries.length <= 105
# intervals[i].length == 2
# 1 <= lefti <= righti <= 107
# 1 <= queries[j] <= 107

# time complexity: O(m * n) where m is the number of queries and n is the number of intervals
# space complexity: O(m)
from typing import List
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = []
        for j in range(len(queries)):
            s = float("inf")
            for interval in intervals:
                left = interval[0]
                right = interval[1]
                if left<=queries[j]<=right:
                    s = min(s, right-left+1)
            if s==float("inf"):
                res.append(-1)
            else:
                res.append(s)
        return res
                
import heapq


# time complexity: O(n log n + q log q) where n is the number of intervals and m is the number of queries
# space complexity: O(n + q) for heap and result array
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = [0 for _ in range(len(queries))] # to store the result for each query, here we could not use map as map wont inlcude duplicate queries
        intervals.sort() # sort intervals based on start time, we sort both intervals and queries so they can be processed in order. O(n log n)
        q_with_idx = [] # to store queries along with their original indices
        for i in range(len(queries)): # populate the q_with_idx list
            q_with_idx.append((queries[i], i))
        q_with_idx.sort() # sort queries based on their values O(q log q)
        min_heap = [] # min heap to store the intervals based on their size. Format: (right-left+1, right)
        i = 0
        for q, idx in q_with_idx: # O
            while i<len(intervals) and intervals[i][0]<=q: # add all intervals that start before or at the query time
                left, right = intervals[i]
                heapq.heappush(min_heap, (right-left+1, right)) # push the size and end time of the interval into the min heap, O(log n)
                i+=1
            # min_heap[0] is the smallest interval that includes the query 
            # min_heap[0][1] is the end time of that interval
            while min_heap and min_heap[0][1]<q: # remove all intervals that end before the query time
                heapq.heappop(min_heap)

            if min_heap:
                res[idx] = min_heap[0][0] # the smallest interval that includes the query
            else:
                res[idx] = -1
        return res            
    
# Time complexity explanation
# Your mental model right now is:

# Outer for over m queries → O(m)

# Inner while over n intervals → O(n)

# heappush → O(log n)

# So total = O(m · n · log n)

# That would be correct if the inner while loop could run over all n intervals for each query.

# But in your code, that’s not what happens, because of the way the pointer i is used.

# Let’s look carefully.

# Over all queries combined, the body of this while runs at most n times.

# It does not restart from i = 0 for each query.

# So you do at most n heappush calls total, not m * n.