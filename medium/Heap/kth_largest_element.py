# 215. Kth Largest Element in an Array
# Neetcode 150 (Important)

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
                heapq.heappush(heap, nums[i]) # heappush takes O(log k) time
            elif nums[i]>heap[0]:
                heapq.heapreplace(heap, nums[i]) # heapreplace takes O(log k) time
        return heap[0]

# time complexity: O(N + Klog(N)), sapce complexity: O(N)    
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-x for x in nums] # O(N) to create a max heap
        heapq.heapify(max_heap) # heapify takes O(N) time
        while k>1:
            heapq.heappop(max_heap) # O(log N) operation to pop the smallest element, done k times
            k-=1
        return -max_heap[0]
    
# Best optimised solution using quickselect without using heap

# Worst time complexity is O(N^2) when we select a bad pivot and have to choose each element as pivot
# Average time complexity is O(N)

# space complexity: O(1)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Quickselect algo (in-place)
        n = len(nums)
        l = 0
        r = n-1
        pivot_idx = 0 # will be reset by partition algo

        def partition_algo(left, right): # left and right
            p = nums[left]
            i = left+1 # start with one after pivot and swap it at the end, this also handles single element array like [1]
            j = right
            # pivot number and not index here
            while i<=j:
                # left should be larger than pivot and right should be smaller than pivot
                # when that does not happen we swap
                if nums[i] < p < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i+=1
                    j-=1

                # happy case 1: left is larger
                if nums[i] >= p:
                    i+=1

                # happy case 2: right is smaller
                if nums[j] <= p:
                    j-=1

            # at the end swap j and pivot
            nums[j], nums[left] = nums[left], nums[j]
            return j # pivot element is at j

        # kth largest pivot element - nums[k-1] (partition in descending order)
        while True:
            pivot_idx = partition_algo(l, r)

            if pivot_idx == k-1:
                break

            # since the pivot_idx is larger we move towards left
            # for example: we were looking for 2nd largest element and we found 4th largest
            # now we move towards left since it is in descending order, so 2nd largest would towards left of 4th largest
            elif pivot_idx > k-1:
                r = pivot_idx-1 
            else:
                l = pivot_idx+1
        return nums[pivot_idx]

# For randomizing the pivot:

# Your pivot is always nums[left] — the leftmost element of the current range, with no randomization. This means on already-sorted or reverse-sorted input, every partition split is maximally unbalanced (one side ends up empty), degrading to the true O(n²) worst case rather than just a rare, unlikely one. The random-pivot version I showed earlier avoids this by making the "adversarial input" scenario essentially impossible to construct on purpose.

# If you want to keep your iterative style but harden it against this, you'd just add one line before reading p:

# import random
# def partition_algo(left, right):
#     rand_idx = random.randint(left, right)
#     nums[left], nums[rand_idx] = nums[rand_idx], nums[left]  # move random pick to the front
#     p = nums[left]
#     ...