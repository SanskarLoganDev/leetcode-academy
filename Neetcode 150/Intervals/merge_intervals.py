# 56. Merge Intervals
# Neetcode 150 (Important)

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

# Constraints:

# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104

from typing import List 

# time complexity O(nlogn) due to sorting
# space complexity O(n) for the output array
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for i in range(1,len(intervals)):
            if intervals[i][0]<=res[-1][1]: # comparing start of current interval with end of last merged interval
                start, end = res.pop() # popping last merged interval
                res.append([start, max(intervals[i][1], end)]) # merging intervals
                continue
            res.append(intervals[i])
        return res