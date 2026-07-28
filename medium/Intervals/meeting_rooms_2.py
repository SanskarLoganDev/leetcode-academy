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
# we must keep track of rooms that open up for another meeting when one meeting ends (reusability of rooms)
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
    

# Dry run

# intervals = [[0,30],[5,10],[15,20],[40,50],[45,55]]

# Step 1: split into separate start and end arrays
# start = [0, 5, 15, 40, 45]
# end   = [30, 10, 20, 50, 55]

# Step 2: sort both independently (they no longer need to stay paired,
# since we only care about "when does *a* room open up", not which specific interval)
# start (sorted) = [0, 5, 15, 40, 45]
# end   (sorted) = [10, 20, 30, 50, 55]

# Step 3: two-pointer sweep, s = index into start[], e = index into end[]
# s=0, e=0, count=0, res=0

# --- Compare start[0]=0 vs end[0]=10 ---
# 0 < 10 → a meeting starts before any meeting ends → need a new room
# count = 1, s = 1
# res = max(0, 1) = 1

# --- Compare start[1]=5 vs end[0]=10 ---
# 5 < 10 → another meeting starts before the first one ends → need another room
# count = 2, s = 2
# res = max(1, 2) = 2

# --- Compare start[2]=15 vs end[0]=10 ---
# 15 < 10 is False → a meeting ends before the next one starts → free up a room
# count = 1, e = 1
# res stays 2 (count went down, not up)

# --- Compare start[2]=15 vs end[1]=20 ---
# 15 < 20 → next meeting starts before this end time → need a room again
# count = 2, s = 3
# res = max(2, 2) = 2

# --- Compare start[3]=40 vs end[1]=20 ---
# 40 < 20 is False → a meeting ends → free up a room
# count = 1, e = 2

# --- Compare start[3]=40 vs end[2]=30 ---
# 40 < 30 is False → another meeting ends → free up another room
# count = 0, e = 3
# (makes sense: by time 40, both [0,30] and [15,20] have long since ended)

# --- Compare start[3]=40 vs end[3]=50 ---
# 40 < 50 → new meeting starts before this end time → need a room
# count = 1, s = 4
# res stays 2 (1 < 2, no new peak)

# --- Compare start[4]=45 vs end[3]=50 ---
# 45 < 50 → another meeting starts before that same end time → need another room
# count = 2, s = 5
# res = max(2, 2) = 2

# s is now 5, which equals len(start) → loop condition s < len(start) fails → loop ends

# Final answer: res = 2
# Correct! At no point in time are more than 2 meetings happening simultaneously —
# [0,30] overlaps briefly with [5,10] and separately with [15,20] (peak of 2),
# and later [40,50] overlaps with [45,55] (peak of 2 again) — but these two
# clusters never overlap each other, so the overall peak stays at 2.
    
    
    

# Why a simpler code (first thought) fails here

# class Solution(object):
#     def minMeetingRooms(self, intervals: List[List[int]]) -> int:
#         count = 1
#         intervals.sort()
#         for i in range(len(intervals)-1):
#             if intervals[i][1]>intervals[i+1][0]:
#                 count+=1
#         return count
    
# Case 1: Your exact example fails
# intervals = [[0,30],[5,10],[15,20],[40,50],[45,55]], answer from code above = 3

# Correct answer: Let's figure out the true minimum rooms needed by tracking what's actually happening over time:

# [0,30] is happening the whole time from 0 to 30
# [5,10] and [15,20] both fall inside [0,30]'s span, but [5,10] and [15,20] don't overlap each other — so at most 2 rooms are ever needed simultaneously (never 3)
# [40,50] and [45,55] overlap each other → needs 2 rooms at that time
# These two clusters (0-30 range vs 40-55 range) don't overlap each other at all

# True answer: 2 (you never need more than 2 rooms at any single point in time)