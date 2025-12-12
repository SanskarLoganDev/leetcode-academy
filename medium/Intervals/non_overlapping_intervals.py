# 435. Non-overlapping Intervals
# Neetcode 150 (Important)

# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

# Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.

 

# Example 1:

# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

# Example 2:

# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

# Example 3:

# Input: intervals = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

# Constraints:

# 1 <= intervals.length <= 105
# intervals[i].length == 2
# -5 * 104 <= starti < endi <= 5 * 104

# time complexity: O(n log n) due to sorting the intervals based on start time
# space complexity: O(1)
from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        count = 0
        i = 0
        j = 1
        while j<len(intervals):
            cs, ce = intervals[i] # here cs and ce are the start and end of the current interval
            ns, ne = intervals[j] # ns and ne are the start and end of the next interval
            if ns>=ce: # no overlapping
                i = j
                j+=1
            # overlapping
            elif ce<=ne: # current interval ends before next interval
                j+=1
                count+=1
            elif ne<ce: # next interval ends before current interval
                i = j
                j+=1
                count+=1
        return count
        
# Another way but same complexity

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0]) # we could simply use .sort() as well, here lambda can be used to specify sorting by start time
        count = 0
        i = 1
        prev_end = intervals[0][1]
        while i<len(intervals):
            start, end = intervals[i] # start and end of current interval
            if start<prev_end: # overlapping
                count+=1
                i+=1
                prev_end = min(end, prev_end) # keep the interval which ends first to minimize overlapping with future intervals

            else: # no overlapping
                prev_end = end
                i+=1
        return count
        