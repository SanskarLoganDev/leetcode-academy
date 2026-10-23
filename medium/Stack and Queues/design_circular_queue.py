# 622. Design Circular Queue

# Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle, and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

# One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

# Implement the MyCircularQueue class:

# MyCircularQueue(k) Initializes the object with the size of the queue to be k.
# int Front() Gets the front item from the queue. If the queue is empty, return -1.
# int Rear() Gets the last item from the queue. If the queue is empty, return -1.
# boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
# boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
# boolean isEmpty() Checks whether the circular queue is empty or not.
# boolean isFull() Checks whether the circular queue is full or not.
# You must solve the problem without using the built-in queue data structure in your programming language. 

 

# Example 1:

# Input
# ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
# [[3], [1], [2], [3], [4], [], [], [], [4], []]
# Output
# [null, true, true, true, false, 3, true, true, true, 4]

# Explanation
# MyCircularQueue myCircularQueue = new MyCircularQueue(3);
# myCircularQueue.enQueue(1); // return True
# myCircularQueue.enQueue(2); // return True
# myCircularQueue.enQueue(3); // return True
# myCircularQueue.enQueue(4); // return False
# myCircularQueue.Rear();     // return 3
# myCircularQueue.isFull();   // return True
# myCircularQueue.deQueue();  // return True
# myCircularQueue.enQueue(4); // return True
# myCircularQueue.Rear();     // return 4
 

# Constraints:

# 1 <= k <= 1000
# 0 <= value <= 1000
# At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull.

# Solution using Array

class MyCircularQueue:

    def __init__(self, k: int): # time: O(k), space: O(k), initializing a list of size k requires writing k values
        self.cap = k
        self.size = 0
        self.front = 0  # we deque (remove) from the front
        self.q = [-1]*k # we enque (add/append) from the rear

    def enQueue(self, value: int) -> bool: # time: O(1), space: O(1)
        if self.isFull():
            return False
        else:
            self.q[(self.front + self.size) % self.cap] = value
            self.size+=1
            return True

    def deQueue(self) -> bool: # time: O(1), space: O(1)
        if self.isEmpty():
            return False
        else:
            self.front = (self.front + 1)%self.cap
            self.size-=1
            return True

    def Front(self) -> int: # time: O(1), space: O(1)
        if self.size == 0:
            return -1
        return self.q[self.front]

    def Rear(self) -> int: # time: O(1), space: O(1)
        if self.size==0:
            return -1
        return self.q[(self.front + self.size - 1) % self.cap]

    def isEmpty(self) -> bool: # time: O(1), space: O(1)
        return self.size == 0

    def isFull(self) -> bool: # time: O(1), space: O(1)
        return self.size == self.cap


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()


# Dry run

# Let's trace this with cap = 3 (q = [0,0,0], head=0, ct=0) through a sequence of operations, watching exactly how head, ct, and the modulo arithmetic interact.

# enQueue(1)

# isFull()? ct(0) == cap(3)? No.
# Write position: (head + ct) % cap = (0 + 0) % 3 = 0. So q[0] = 1 → q = [1, 0, 0].
# ct += 1 → ct = 1.
# Queue conceptually holds: [1], front is at index 0.

# enQueue(2)

# isFull()? ct(1) == cap(3)? No.
# Write position: (0 + 1) % 3 = 1. q[1] = 2 → q = [1, 2, 0].
# ct = 2.
# Queue holds: [1, 2].

# enQueue(3)

# Write position: (0 + 2) % 3 = 2. q[2] = 3 → q = [1, 2, 3].
# ct = 3.
# Queue holds: [1, 2, 3] — now full (ct == cap).

# enQueue(4) — should fail, queue is full

# isFull()? ct(3) == cap(3)? Yes → return False immediately. Nothing changes.

# deQueue() — remove the front element (which is 1)

# isEmpty()? ct(3) == 0? No.
# head = (head + 1) % cap = (0 + 1) % 3 = 1.
# ct -= 1 → ct = 2.
# Notice: q itself is untouched — still [1, 2, 3]. The 1 at index 0 is now considered "stale leftover data," but it's harmless, 
# because head has moved past it — nothing will ever read index 0 again until it gets overwritten by a future enQueue. 
# Queue conceptually holds [2, 3] (front is now whatever q[head] points to, which is q[1] = 2).

# Continuing right where we left off — state was q=[4,2,3], head=1, ct=3 (full), conceptual queue [2,3,4].

# Front()

# not ct → ct=3 is truthy, so this is False, we proceed.
# Returns q[head] = q[1] = 2.
# Correct — the front of [2,3,4] is 2.

# Rear()

# not ct → False, proceed.
# Returns q[(head + ct - 1) % cap] = q[(1 + 3 - 1) % 3] = q[3 % 3] = q[0] = 4.
# Correct — the rear of [2,3,4] is 4. Notice it correctly reaches back to index 0, even though head is at 1 — this is the wraparound working in the "read" direction too, not just for writes.

# isFull()

# ct(3) == cap(3) → True.

# isEmpty()

# ct(3) == 0 → False.

# deQueue() — remove the front (2)

# isEmpty()? No.
# head = (head + 1) % cap = (1 + 1) % 3 = 2.
# ct -= 1 → ct = 2.
# q array unchanged: still [4, 2, 3] (the 2 at index 1 is now stale, ignored). Conceptual queue: front is q[head]=q[2]=3, next is q[(head+1)%cap]=q[0]=4 → [3, 4].

# Front()

# q[head] = q[2] = 3. Correct.

# Rear()

# q[(head+ct-1)%cap] = q[(2+2-1)%3] = q[3%3] = q[0] = 4. Correct.

# enQueue(5)

# isFull()? ct(2) == cap(3)? No.
# Write position: (head+ct)%cap = (2+2)%3 = 4%3 = 1. So q[1] = 5 → q = [4, 5, 3].
# ct += 1 → ct = 3.
# Conceptual queue: front q[2]=3, then q[(2+1)%3]=q[0]=4, then q[(2+2)%3]=q[1]=5 → [3, 4, 5].