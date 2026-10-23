# 641. Design Circular Deque

# Design your implementation of the circular double-ended queue (deque).

# Implement the MyCircularDeque class:

# MyCircularDeque(int k) Initializes the deque with a maximum size of k.
# boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise.
# boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
# boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
# boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
# int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
# int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
# boolean isEmpty() Returns true if the deque is empty, or false otherwise.
# boolean isFull() Returns true if the deque is full, or false otherwise.
 

# Example 1:

# Input
# ["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
# [[3], [1], [2], [3], [4], [], [], [], [4], []]
# Output
# [null, true, true, true, false, 2, true, true, true, 4]

# Explanation
# MyCircularDeque myCircularDeque = new MyCircularDeque(3);
# myCircularDeque.insertLast(1);  // return True
# myCircularDeque.insertLast(2);  // return True
# myCircularDeque.insertFront(3); // return True
# myCircularDeque.insertFront(4); // return False, the queue is full.
# myCircularDeque.getRear();      // return 2
# myCircularDeque.isFull();       // return True
# myCircularDeque.deleteLast();   // return True
# myCircularDeque.insertFront(4); // return True
# myCircularDeque.getFront();     // return 4

# Constraints:

# 1 <= k <= 1000
# 0 <= value <= 1000
# At most 2000 calls will be made to insertFront, insertLast, deleteFront, deleteLast, getFront, getRear, isEmpty, isFull.

# time complexity: O(1) for every function

# Main logic:
# +1 in array index -> (idx + 1) % size
# -1 in array index -> (idx -1 + size) % size 

class MyCircularDeque:

    def __init__(self, k: int): # Space : O(k)
        self.k = k
        self.arr = [-1]*k
        self.size = 0
        self.front = 0
        self.rear = k-1

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = (self.front - 1 + self.k)%self.k # make sure the front index is moved before inserting the value and points at the newly inserted value
        self.arr[self.front] = value       
        self.size+=1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1)%self.k # make sure the rear index is moved before inserting the value and points at the newly inserted value
        self.arr[self.rear] = value
        self.size+=1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.arr[self.front] = -1 # in case of delete, just assign the current index as -1 and then move the index
        self.front = (self.front + 1)%self.k
        self.size-=1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.arr[self.rear] = -1
        self.rear = (self.rear - 1 + self.k)%self.k
        self.size-=1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.arr[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.arr[self.rear]

    def isEmpty(self) -> bool:
        return self.size==0

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()