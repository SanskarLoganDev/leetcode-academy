# 215. Kth Largest Element in an Array

# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

 

# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

from typing import List

# Using sort O(NlogK)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k-1]


# Time complexity — O(n log k)

# Up to k times we do heappush on a heap of size ≤ k ⇒ each O(log k) ⇒ O(k log k).
# For the remaining n − k elements:
# Compare with heap[0] ⇒ O(1).
# If larger, heapreplace (pop then push) ⇒ O(log k).
# Worst case, this happens for each of the n − k elements ⇒ O((n − k) log k).

# Total worst-case: O(k log k + (n − k) log k) = O(n log k).
# Space complexity — O(k)

# The heap stores at most k elements. No other auxiliary structures grow with n.

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in range(len(nums)):
            if len(heap)<k:
                heapq.heappush(heap, nums[i])
            elif nums[i]>heap[0]:
                heapq.heapreplace(heap, nums[i])
        return heap[0]

# time complexity: O(N + Klog(N))    
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-x for x in nums] # O(N) to create a max heap
        heapq.heapify(max_heap)
        while k>1:
            heapq.heappop(max_heap) # O(log N) operation to pop the smallest element, done k times
            k-=1
        return -max_heap[0]
        