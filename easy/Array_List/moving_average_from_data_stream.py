# 346. Moving Average from Data Stream

# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

# Implement the MovingAverage class:

# MovingAverage(int size) Initializes the object with the size of the window size.
# double next(int val) Returns the moving average of the last size values of the stream.
 

# Example 1:

# Input
# ["MovingAverage", "next", "next", "next", "next"]
# [[3], [1], [10], [3], [5]]
# Output
# [null, 1.0, 5.5, 4.66667, 6.0]

# Explanation
# MovingAverage movingAverage = new MovingAverage(3);
# movingAverage.next(1); // return 1.0 = 1 / 1
# movingAverage.next(10); // return 5.5 = (1 + 10) / 2
# movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
# movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3
 

# Constraints:

# 1 <= size <= 1000
# -105 <= val <= 105
# At most 104 calls will be made to next.

# Time complexity: O(1) can also be implemented using deque/queue but same time complexity (implemented below)
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.avg_list = []
        

    def next(self, val: int) -> float:
        self.avg_list.append(val)
        if len(self.avg_list)<self.size:
            return sum(self.avg_list)/len(self.avg_list)
        return sum(self.avg_list[-self.size:])/self.size


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

# Using queue
from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.size = size 
        self.queue = deque()
        self.sum = 0
        self.max = size 
        self.length = 0 

    def next(self, val: int) -> float:
        if self.length < self.max:
            self.length += 1
            self.queue.append(val)
            self.sum += val
        else:
            self.sum -= self.queue.popleft()
            self.queue.append(val)
            self.sum += val
        return self.sum / self.length