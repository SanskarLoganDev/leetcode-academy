# 703. Kth Largest Element in a Stream
# Neetcode 150 (Important)

# You are part of a university admissions office and need to keep track of the kth highest test score from applicants in real-time. This helps to determine cut-off marks for interviews and admissions dynamically as new applicants submit their scores.

# You are tasked to implement a class which, for a given integer k, maintains a stream of test scores and continuously returns the kth highest test score after a new score has been submitted. More specifically, we are looking for the kth highest score in the sorted list of all scores.

# Implement the KthLargest class:

# KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of test scores nums.
# int add(int val) Adds a new test score val to the stream and returns the element representing the kth largest element in the pool of test scores so far.
 

# Example 1:

# Input:
# ["KthLargest", "add", "add", "add", "add", "add"]
# [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

# Output: [null, 4, 5, 5, 8, 8]

# Explanation:

# KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
# kthLargest.add(3); // return 4
# kthLargest.add(5); // return 5
# kthLargest.add(10); // return 5
# kthLargest.add(9); // return 8
# kthLargest.add(4); // return 8

# Example 2:

# Input:
# ["KthLargest", "add", "add", "add", "add"]
# [[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]]

# Output: [null, 7, 7, 7, 8]

# Explanation:

# KthLargest kthLargest = new KthLargest(4, [7, 7, 7, 7, 8, 3]);
# kthLargest.add(2); // return 7
# kthLargest.add(10); // return 7
# kthLargest.add(9); // return 7
# kthLargest.add(9); // return 8

from typing import List

# Time omplexity: O(NlogN) since we are using sorting
# Space complexity: O(N) for storing the elements in the list
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums # extra space to store the elements
        self.k = k

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort(reverse=True)
        return self.nums[self.k-1]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# Implementation using heap: With a min‐heap of fixed size k, each add call takes O(log k) time
# time complexity: O(log k) for each add operation
# space complexity: O(k) for the heap

import heapq
from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        # This heap will store the k largest elements seen so far.
        self.heap = []
        # Process each number in the initial list by calling add. (for k=3, the heap will not have more than 3 elements)
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # If the heap has fewer than k elements, add the new value.
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        # Otherwise, if the new value is larger than the smallest element in the heap,
        # it deserves a spot among the k largest elements.
        elif val > self.heap[0]:
            # heapreplace removes the smallest element and adds the new one.
            heapq.heapreplace(self.heap, val)
        # After the operation, the smallest element in the heap (heap[0] is the kth largest element overall.
        # time complexity of heapreplace is O(log k)
        return self.heap[0]

# Example usage:
kthLargest = KthLargest(3, [4, 5, 8, 2])
print(kthLargest.add(3))   # Expected output: 4
print(kthLargest.add(5))   # Expected output: 5
print(kthLargest.add(10))  # Expected output: 5
print(kthLargest.add(9))   # Expected output: 8
print(kthLargest.add(4))   # Expected output: 8
