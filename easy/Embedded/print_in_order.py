# 1114. Print in Order

# Suppose we have a class:

# public class Foo {
#   public void first() { print("first"); }
#   public void second() { print("second"); }
#   public void third() { print("third"); }
# }
# The same instance of Foo will be passed to three different threads. Thread A will call first(), thread B will call second(), and thread C will call third(). Design a mechanism and modify the program to ensure that second() is executed after first(), and third() is executed after second().

# Note:

# We do not know how the threads will be scheduled in the operating system, even though the numbers in the input seem to imply the ordering. The input format you see is mainly to ensure our tests' comprehensiveness.

# Example 1:

# Input: nums = [1,2,3]
# Output: "firstsecondthird"
# Explanation: There are three threads being fired asynchronously. The input [1,2,3] means thread A calls first(), thread B calls second(), and thread C calls third(). "firstsecondthird" is the correct output.

# Example 2:

# Input: nums = [1,3,2]
# Output: "firstsecondthird"
# Explanation: The input [1,3,2] means thread A calls first(), thread B calls third(), and thread C calls second(). "firstsecondthird" is the correct output.
 

# Constraints:

# nums is a permutation of [1, 2, 3].

# Brute force solution

class Foo:
    def __init__(self):
        self.stage = 0


    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.stage = 1


    def second(self, printSecond: 'Callable[[], None]') -> None:
        while self.stage < 1: # start after stage has reached 1
            pass
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.stage = 2 # reach stage 2


    def third(self, printThird: 'Callable[[], None]') -> None:
        while self.stage < 2: # start after stage has reached 2
            pass
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        self.stage = 3 # reach stage 3
        
# Why Is Busy Waiting Bad?

# Look at this code:

# while self.stage < 1:
#     pass

# Imagine first() takes five seconds to execute.

# For those five seconds, Thread B keeps checking:

# Is stage >= 1? No.

# Is stage >= 1? No.

# Is stage >= 1? No.

# Is stage >= 1? No.

# Is stage >= 1? No.

# ...

# Potentially millions of checks!

# This is called busy waiting or spin waiting.

# The thread continuously executes instructions while waiting for a condition to become true.

from threading import Event

class Foo:
    def __init__(self):
        self.first_done = Event()
        self.second_done = Event()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_done.set()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.first_done.wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.second_done.set()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.second_done.wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()


# Optimized Approach: threading.Event

# Python provides a synchronization primitive called Event.

# from threading import Event

# An Event is essentially a signal that one thread can use to notify another thread that something has happened.

# Think of it as a traffic light.

# An event has two possible states:

# State	Meaning
# Not set	Threads calling wait() must wait
# Set	Threads calling wait() can proceed

# We primarily use three operations.

# 1. Event()

# Creates a new event.

# event = Event()

# Initially, the event is not set.

# 2. event.wait()

# Waits until the event becomes set.

# event.wait()

# If the event is not set:

# Thread ---> wait()
#               |
#               v
#            BLOCKED

# If another thread sets the event, the waiting thread becomes eligible to continue.

# If the event is already set, wait() returns immediately.

# 3. event.set()

# Sets the event and wakes threads waiting on it.

# event.set()

# Example:

# Thread A                     Thread B
# --------                     --------

#                              event.wait()
#                                   |
#                                   v
#                                BLOCKED

# Perform some work
#        |
#        v
# event.set()
#        |
#        |--------------------------|
#                                   v
#                              Continue

# Important distinction: Unlike busy waiting, Event.wait() does not continuously execute Python instructions to check the condition. 
# It uses blocking synchronization provided by the underlying threading implementation.