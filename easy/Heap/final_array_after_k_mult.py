# 3264. Final Array State After K Multiplication Operations I

# You are given an integer array nums, an integer k, and an integer multiplier.

# You need to perform k operations on nums. In each operation:

# Find the minimum value x in nums. If there are multiple occurrences of the minimum value, select the one that appears first.
# Replace the selected minimum value x with x * multiplier.
# Return an integer array denoting the final state of nums after performing all k operations.


# Example 1:

# Input: nums = [2,1,3,5,6], k = 5, multiplier = 2

# Output: [8,4,6,5,6]

# Explanation:

# Operation	        Result
# After operation 1	[2, 2, 3, 5, 6]
# After operation 2	[4, 2, 3, 5, 6]
# After operation 3	[4, 4, 3, 5, 6]
# After operation 4	[4, 4, 6, 5, 6]
# After operation 5	[8, 4, 6, 5, 6]
# Example 2:

# Input: nums = [1,2], k = 3, multiplier = 4

# Output: [16,8]

# Explanation:

# Operation	        Result
# After operation 1	[4, 2]
# After operation 2	[4, 8]
# After operation 3	[16, 8]

from typing import List
# Solution using list O(k * n)

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        iter = 0
        while iter<k:
            min_num = min(nums)
            min_index = nums.index(min_num)
            nums[min_index]*=multiplier
            iter+=1
        return nums

# Solution using heap O(n + k log n)

import heapq
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        # Build a heap of tuples (value, index) from nums.
        # The tuple ensures that if two values are equal, the one with the smaller index (i.e. the one that appears first)
        # is chosen because tuples are compared elementwise.
        h = [(nums[i], i) for i in range(len(nums))]
        heapq.heapify(h)  # O(n) time to build the heap
        
        # Perform k operations.
        for _ in range(k):
            # Pop the smallest tuple (value, index) from the heap.
            val, idx = heapq.heappop(h)
            
            # Multiply the popped value by multiplier.
            new_val = val * multiplier
            
            # Update the original array with the new value at the corresponding index.
            nums[idx] = new_val
            
            # Push the updated (value, index) pair back into the heap.
            heapq.heappush(h, (new_val, idx))
            
        return nums

# Python's heapq module doesn't need explicit instructions about which element of the tuple to use for ordering; it uses Python’s built-in comparison operators on tuples. When comparing two tuples, Python compares them lexicographically, which means:
# 1.	It first compares the first elements of both tuples.
# 2.	If the first elements are equal, it compares the second elements.
# 3.	This process continues if there are more elements.
# In our solution, each element we put into the heap is a tuple of the form (value, index). When you call heapq.heapify(h), the heap is built using the < operator on these tuples. Here's how it works:
# •	When comparing (a, i) and (b, j), Python first compares a to b.
# •	If a < b, then (a, i) is considered smaller, regardless of i and j.
# •	If a == b, then Python compares i and j. This tie-breaker ensures that if two elements have the same value, the one with the smaller (earlier) index will be considered smaller.
