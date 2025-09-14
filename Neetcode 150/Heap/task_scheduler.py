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
        print(max_heap)
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

# Explanation with example:
    
# Start

# Heap: {A6, B2, C1, D1}
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