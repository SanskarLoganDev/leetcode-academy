# 253. Meeting Rooms II
# Neetcode 150 (Important)

# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

# Example 1:

# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2
# Explanation: We need two meeting rooms because the first meeting overlaps with both the second and third meetings.

# Example 2:

# Input: intervals = [[7,10],[2,4]]
# Output: 1
 # Explanation: We only need one meeting room because the meetings do not overlap.

# Constraints:

# 1 <= intervals.length <= 104
# 0 <= starti < endi <= 106

from typing import List

# time complexity: O(n log n) due to sorting the start and end times
# space complexity: O(n) for storing the start and end times

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = [] # list to store start times
        end = [] # list to store end times
        for interval in intervals: # populate the start and end lists
            end.append(interval[1])
            start.append(interval[0])
        start.sort() # sort the start times
        end.sort() # sort the end times
        s, e = 0, 0 # pointers for start and end lists
        res, count = 0, 0 # res to store the result and count to store the current number of rooms needed
        while s<len(start) and e<len(end): # iterate through both lists
            if start[s]<end[e]: # a meeting is starting before the earliest ending meeting ends
                count+=1 # need a new room
                s+=1
            else: # a meeting has ended before the next meeting starts. This also covers the edge case when start[s] == end[e], 
    # here we choose end first as according to the problem statement, meetings that end at time t and meetings that start at time t do not overlap.
                count-=1 # a room is freed up
                e+=1
            res = max(res, count)
        return res