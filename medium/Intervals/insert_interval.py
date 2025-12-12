# 57. Insert Interval
# Neetcode 150 (Important)

# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.

# Note that you don't need to modify intervals in-place. You can make a new array and return it.

# Example 1:

# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

# Example 2:

# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 
# Constraints:

# 0 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 105
# intervals is sorted by starti in ascending order.
# newInterval.length == 2
# 0 <= start <= end <= 105

# Approach: Linear scan + Merging intervals
# Time complexity: O(n^2)
# Space complexity: O(1)

from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        while i<len(intervals):
            if intervals[i][1]<newInterval[0]:
                i+=1
                continue
            if intervals[i][0]>newInterval[1]:
                intervals.insert(i, newInterval) # insert at the correct position, O(N)
                return intervals
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
                intervals.pop(i) # O(N) # we dont increment i here as we have removed the current interval
        intervals.append(newInterval)
        return intervals
    
# Optimal Approach

# time complexity: O(n)
# space complexity: O(n)

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        res = []
        while i<len(intervals):
            if intervals[i][1]<newInterval[0]:
                res.append(intervals[i])
                i+=1
                continue
            if intervals[i][0]>newInterval[1]:
                break  # we can break here as the remaining intervals will also be after newInterval. We cant append in res here we would also need to append all remaining intervals in the original list
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
                i+=1
        res.append(newInterval)
        if i<len(intervals): # better to have this check outside of the loop as we need to optimize.
            res.extend(intervals[i:]) # append the remaining intervals. A simple for loop can also be used here.
        return res


