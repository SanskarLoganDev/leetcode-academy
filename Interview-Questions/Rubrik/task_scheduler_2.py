# 2365. Task Scheduler II

# You are given a 0-indexed array of positive integers tasks, representing tasks that need to be completed in order, where tasks[i] represents the type of the ith task.

# You are also given a positive integer space, which represents the minimum number of days that must pass after the completion of a task before another task of the same type can be performed.

# Each day, until all tasks have been completed, you must either:

# Complete the next task from tasks, or
# Take a break.
# Return the minimum number of days needed to complete all tasks.

# Example 1:

# Input: tasks = [1,2,1,2,3,1], space = 3
# Output: 9
# Explanation:
# One way to complete all tasks in 9 days is as follows:
# Day 1: Complete the 0th task.
# Day 2: Complete the 1st task.
# Day 3: Take a break.
# Day 4: Take a break.
# Day 5: Complete the 2nd task.
# Day 6: Complete the 3rd task.
# Day 7: Take a break.
# Day 8: Complete the 4th task.
# Day 9: Complete the 5th task.
# It can be shown that the tasks cannot be completed in less than 9 days.

# Example 2:

# Input: tasks = [5,8,8,5], space = 2
# Output: 6
# Explanation:
# One way to complete all tasks in 6 days is as follows:
# Day 1: Complete the 0th task.
# Day 2: Complete the 1st task.
# Day 3: Take a break.
# Day 4: Take a break.
# Day 5: Complete the 2nd task.
# Day 6: Complete the 3rd task.
# It can be shown that the tasks cannot be completed in less than 6 days.
 

# Constraints:

# 1 <= tasks.length <= 105
# 1 <= tasks[i] <= 109
# 1 <= space <= tasks.length

# Brute force solution
# Time complexity: O(N*space)
# Space Complexity: O(n): next_available dict stores at most one entry per unique task value, 
# so in the worst case (all distinct tasks), this is O(n).

from typing import List
class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        next_available = {}
        idx = 0
        day = 0
        while idx < len(tasks):
            curr_task = tasks[idx]
            if curr_task in next_available and day < next_available[curr_task]:
                day+=1
            else:
                next_available[curr_task] = day + space + 1
                idx+=1
                day+=1

        return day
    
# Optimised solution by skipping idle days:
# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        next_available = {}
        day = 0
        for task in tasks:
            if task in next_available and day < next_available[task]: # the task was already finished and has to start again, so compare it when it becomes available. 
                # Example: [1,2,1,2,3,1] the 2nd time 1 appears
                day = next_available[task] # only jump when task already in dict and we have to wait for space to complete this repeating task again, so we simply jump to that day
            next_available[task] = day + space + 1
            day+=1

        return day
    
# Dry run 1: tasks=[1,2,1,2,3,1], space=3

# current_day=0, next_available={}

# task=1: not seen → next_available[1]=0+3+1=4, current_day=1
# task=2: not seen → next_available[2]=1+3+1=5, current_day=2
# task=1: seen, next_available[1]=4, current_day(2) < 4 → jump to current_day=4. Then next_available[1]=4+3+1=8, current_day=5
# task=2: seen, next_available[2]=5, current_day(5) < 5 is False → no jump. next_available[2]=5+3+1=9, current_day=6
# task=3: not seen → next_available[3]=6+3+1=10, current_day=7
# task=1: seen, next_available[1]=8, current_day(7) < 8 → jump to current_day=8. next_available[1]=8+3+1=12, current_day=9

# Final current_day = 9 — matches the expected output exactly, and if you check, every jump lines up precisely with the "Day X" breaks described in the problem's own explanation.    

# Dry run 2: tasks=[1,2,3,4,5], space=3

# Processing tasks[0] = 1
# Before: current_day=0, next_available={}
# Check: is 1 a key in next_available? No — the dict is empty, we haven't seen anything yet. So the if condition is False immediately (short-circuits on the first part, task in next_available), and no jump happens.
# After: next_available[1] = current_day + space + 1 = 0 + 3 + 1 = 4. Then current_day += 1 → 1.
# next_available = {1: 4}

# Processing tasks[1] = 2
# Before: current_day=1, next_available={1: 4}
# Check: is 2 in next_available? No — only 1 has been recorded so far, and 2 is a completely different key. No jump.
# After: next_available[2] = 1 + 3 + 1 = 5. current_day → 2.
# next_available = {1: 4, 2: 5}

# Processing tasks[2] = 3
# Before: current_day=2, next_available={1: 4, 2: 5}
# Check: is 3 in next_available? No. No jump.
# After: next_available[3] = 2 + 3 + 1 = 6. current_day → 3.
# next_available = {1: 4, 2: 5, 3: 6}

# Processing tasks[3] = 4
# Before: current_day=3, next_available={1: 4, 2: 5, 3: 6}
# Check: is 4 in next_available? No. No jump.
# After: next_available[4] = 3 + 3 + 1 = 7. current_day → 4.
# next_available = {1: 4, 2: 5, 3: 6, 4: 7}

# Processing tasks[4] = 5
# Before: current_day=4, next_available={1: 4, 2: 5, 3: 6, 4: 7}
# Check: is 5 in next_available? No. No jump.
# After: next_available[5] = 4 + 3 + 1 = 8. current_day → 5.
# next_available = {1: 4, 2: 5, 3: 6, 4: 7, 5: 8}

# Loop ends. Final answer: current_day = 5.