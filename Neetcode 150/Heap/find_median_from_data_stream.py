# 295. Find Median from Data Stream

# Neetcode 150 (Important)

# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:

# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 
# Example 1:

# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]

# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0
 
# Constraints:

# -105 <= num <= 105
# There will be at least one element in the data structure before calling findMedian.
# At most 5 * 104 calls will be made to addNum and findMedian.
 
# Follow up:

# If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
# If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?

# Brute Force
# Tmie complexity: O(NlogN)

class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        self.nums.sort()
        if len(self.nums)%2!=0:
            return self.nums[len(self.nums)//2]
        mid1 = self.nums[len(self.nums)//2]
        mid2 = self.nums[(len(self.nums)//2)-1]
        return (mid1+mid2)/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# 4 important conditions to be followed
# 1. if num> max_left_heap[0] -> push to min_right_heap
# 2. if len(min_right_heap)> len(max_left_heap) -> pop from min_right_heap and push to max_left_heap
# 3. if len(max_left_heap)> len(min_right_heap)+1 -> pop from max_left_heap and push to min_right_heap
# 4. if len(max_left_heap)> len(min_right_heap) -> return max_left_heap[0] else return (max_left_heap[0]+min_right_heap[0])/2

import heapq
class MedianFinder:
    
    def __init__(self):
        self.max_left_heap = []
        self.min_right_heap = []

    def addNum(self, num: int) -> None:
        if not self.max_left_heap:
            self.max_left_heap.append(-num)
            return
        if num>-self.max_left_heap[0]:
            heapq.heappush(self.min_right_heap, num)
            if len(self.min_right_heap)> len(self.max_left_heap):
                popped = heapq.heappop(self.min_right_heap)
                heapq.heappush(self.max_left_heap, -popped)
        else:
            heapq.heappush(self.max_left_heap, -num)
            if len(self.max_left_heap)>len(self.min_right_heap)+1:
                popped = -heapq.heappop(self.max_left_heap)
                heapq.heappush(self.min_right_heap, popped) 

    def findMedian(self) -> float:
        if len(self.max_left_heap)>len(self.min_right_heap):
            return -self.max_left_heap[0]
        else:
            return (-self.max_left_heap[0]+self.min_right_heap[0])/2
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()