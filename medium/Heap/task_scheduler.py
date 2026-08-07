# 621. Task Scheduler
# Neetcode 150 (Important)

# You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

# Return the minimum number of CPU intervals required to complete all tasks.

# Example 1:

# Input: tasks = ["A","A","A","B","B","B"], n = 2

# Output: 8

# Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

# After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

# Example 2:

# Input: tasks = ["A","C","A","B","D","B"], n = 1

# Output: 6

# Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

# With a cooling interval of 1, you can repeat a task after just one other task.

# Example 3:

# Input: tasks = ["A","A","A", "B","B","B"], n = 3

# Output: 10

# Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

# There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.

# Constraints:

# 1 <= tasks.length <= 104
# tasks[i] is an uppercase English letter.
# 0 <= n <= 100

# time complexity: O(N) where N is the len(tasks)
# Space complexity: O(1), nowhere we store more than a  max of 26 characters
from typing import List

import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mp = [0]*26 # instead of this, we can also use a dictionary to hold frequencies
        for task in tasks:
            mp[ord(task)-65]+=1
        time = 0

        max_heap = []
        for i in mp:
            if i>0:
                max_heap.append(i)
        max_heap = [-num for num in max_heap] # converting to max heap by negating the values
        heapq.heapify(max_heap)

        while max_heap:  
            temp = []
            i = 1
            while i<=n+1 and max_heap:
                freq = -heapq.heappop(max_heap) # negating again to get the original frequency
                freq-=1
                temp.append(freq)
                i+=1
            # here we do -freq because we negated the frequencies while pushing to the max heap
            [heapq.heappush(max_heap, -freq) for freq in temp if freq>0] # pushing back the remaining frequencies to the max heap

            if max_heap: # if max_heap is not empty, it means we had to idle for some time
                time+=n+1
            else:
                time+=len(temp) # if max_heap is empty, we only add the number of tasks we executed in this cycle

        return time

# Explanation of last logic here:
# So len(temp) = "how many genuinely busy intervals happened in this round" — a 0 in there doesn't mean "nothing happened," it means "a task ran and that was its last instance."

# Now the two branches, side by side

# if max_heap: (heap still has work left after this round)
# This means there's more scheduling to do later. Whatever tasks got run this round (even the ones now at 0) had
# other, different tasks running alongside them in this round's slots — and even if this round didn't fill all n+1
# slots with real tasks, the CPU still must occupy a full n+1-wide block before the next round can safely begin
# (that's the cooldown constraint). So we charge time += n+1 regardless of how many of those slots were genuinely
# busy vs. idle — the round costs n+1 no matter what, because more work is still queued after it.

# else: (heap is now empty — this was the final round)
# Since nothing is left to schedule afterward, there's no need to protect any future cooldown — you don't need to
# pad this round out to a full n+1 width with idle time nobody needs. 
# The round's true cost is exactly however many real task-executions happened, which is precisely len(temp). 
# If 3 tasks ran in this final round, that's 3 busy intervals and 0 wasted idle time tacked onto the end.


# Explanation with example:
    
# Start

# Heap: {A: 6, B: 2, C: 1, D: 1}, n=1
# time = 0

# Cycle 1 (up to 2 slots)

# pop A6 → run A → A5

# pop B2 → run B → B1
# push back: A5, B1
# heap after: {A5, B1, C1, D1}
# heap not empty → time += 2 → time = 2
# timeline: A, B

# Cycle 2

# pop A5 → run A → A4

# pop B1 → run B → B0 (don’t push back)
# push back: A4
# heap after: {A4, C1, D1}
# heap not empty → time += 2 → time = 4
# timeline: A, B

# Cycle 3

# pop A4 → run A → A3

# pop C1 → run C → C0
# push back: A3
# heap after: {A3, D1}
# heap not empty → time += 2 → time = 6
# timeline: A, C

# Cycle 4

# pop A3 → run A → A2

# pop D1 → run D → D0
# push back: A2
# heap after: {A2}
# heap not empty → time += 2 → time = 8
# timeline: A, D

# Cycle 5

# pop A2 → run A → A1
# (no second task available this cycle)
# push back: A1
# heap after: {A1}
# heap not empty → time += 2 → time = 10
# timeline: A, idle ← (the “+2” accounts for the required idle)

# Cycle 6 (final)

# pop A1 → run A → A0
# push back: none
# heap after: {}
# heap empty → time += len(temp) = 1 → time = 11
# timeline: A

# Result

# Minimal intervals = 11

# One valid schedule (by cycles):
# (A,B) → (A,B) → (A,C) → (A,D) → (A, idle) → (A)

# This matches the well-known formula:
# Let f_max = 6 (count of most frequent task A) and m = 1 (number of tasks with that max count).
# Answer = max(len(tasks), (f_max-1)*(n+1) + m) = max(10, (6-1)*2 + 1) = max(10, 11) = 11.

# Same time and space complexity, just using greedy without heap
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = [0]*26
        for task in tasks:
            counts[ord(task) - ord('A')]+=1
        counts.sort()
        # for tasks = ["A","A","A","B","B","B"], n = 2
        max_freq = counts[-1]
        no_pits = max_freq - 1  # 3-1 = 2
        idlespots = n*no_pits   # A _ _ A _ _ A, here idlespots = 4 = 2*2
        # starting with the 2nd largest element therefore index 24
        for i in range(24, -1, -1):
            idlespots = idlespots - min(counts[i], no_pits)
        
        if idlespots>0:
            return len(tasks) + idlespots
        return len(tasks)

# Code walkthrough
# example (tasks = ["A","A","A","A","B","B","B","B","C","C","C","D","D","E"], n=2) 
# has exactly the edge cases we want: a tie for max frequency (A and B both at 4), 
# a filler that overflows the available pits

# Step 1 — Build counts

# Walk through all 14 tasks, incrementing counts[ord(task)-ord('A')]. 
# Before sorting, the relevant (non-zero) entries are:

# counts[0] (A) = 4, counts[1] (B) = 4, counts[2] (C) = 3, counts[3] (D) = 2, counts[4] (E) = 1

# All other 21 letters stay 0.

# Step 2 — Sort counts

# counts.sort() arranges all 26 values ascending. 
# The 21 zeros settle at the front (indices 0–20), then the real frequencies fill in ascending order at the back:

# counts[21] = 1 (E)
# counts[22] = 2 (D)
# counts[23] = 3 (C)
# counts[24] = 4 (either A or B — whichever Python's sort happens to place there; doesn't matter, value is what counts)
# counts[25] = 4 (the other of A/B)

# Step 3 — Compute the frame

# max_freq = counts[-1] = 4
# no_pits = max_freq - 1 = 3 — this is how many gaps exist between four instances of the busiest task: X _ _ _ X _ _ _ X _ _ _ X
# idlespots = n * no_pits = 2 * 3 = 6 — total idle slots in that frame (3 gaps, each n=2 wide)

# Step 4 — Loop from i=24 down to i=0, subtracting fillers

# This walks every other entry (everything except the single largest at index 25), from second-largest down to the smallest, using each to soak up idle slots — capped at no_pits per task, since a task can occupy at most one slot per gap.

# i=24: counts[24] = 4 — this is the tied max-frequency task (say B). Even though B is just as frequent as A, it can still only fill min(4, no_pits=3) = 3 idle slots (one per gap; its 4th instance can't fit in the frame and must trail afterward). idlespots = 6 - 3 = 3

# i=23: counts[23] = 3 (C). min(3, 3) = 3. C fills all 3 remaining idle slots exactly. idlespots = 3 - 3 = 0

# i=22: counts[22] = 2 (D). min(2, 3) = 2, but idlespots is already 0 — subtracting still works arithmetically: idlespots = 0 - 2 = -2. Note: this pushes idlespots negative, since there was nothing left to fill.

# i=21: counts[21] = 1 (E). min(1, 3) = 1. idlespots = -2 - 1 = -3

# i=20 down to i=0: all zeros. min(0, 3) = 0 each time — no change. idlespots stays -3.

# Step 5 — Final check

# idlespots = -3, which is not > 0, so the code takes the return len(tasks) branch → returns 14.