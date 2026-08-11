# Problem: The Smart Light Panel

# You're building the controller for a panel of n lights, numbered 0 ... n-1.

# Each light is on (1) or off (0). At power-up, all lights are off.

# Design a data structure supporting:

# Method	   What it does
# get(i)	   Return whether light i is on or off
# set(i, b)	   Turn light i on (b=1) or off (b=0)
# toggle(i)	   Flip light i
# setAll(b)	   Turn every light on or off at once, like a master switch
# countOn()	   Return how many lights are currently on
# countOff()   Return how many lights are currently off

# Part 2
# Add:

# Method	    What it does
# toggleAll()	Flip every light at once

# Hard requirement

# Every operation must run in O(1) time, including:

# setAll, countOn, and toggleAll.

# O(n) space is allowed.

# Brute force
# time complexity: O(N)
# space complexity: O(N)


class Solution:
    def __init__(self, n: int) -> None: # O(N), here O(N) is fine
        self.arr = [0]*n
        self.n = n
        self.countOn = 0
        self.countOff = n
        
    def get_i(self, idx: int): # O(1)
        return self.arr[idx]
    
    def set_i(self, idx: int, b: int):  # O(1)
        if b==0 and self.arr[idx]==1:
            self.countOn-=1
            self.countOff+=1
        elif b==1 and self.arr[idx]==0:
            self.countOff-=1
            self.countOn+=1
                
        self.arr[idx] = b
        
        
    def toggle(self, idx: int): # O(1)
        if self.arr[idx]==0:
            self.arr[idx] = 1
            self.countOn+=1
            self.countOff-=1
        else:
            self.arr[idx] = 0
            self.countOff+=1
            self.countOn-=1
            
    def setAll(self, b: int): # O(N)
        if b==0:
            for i in range(self.n):
                self.arr[i] = 0
            self.countOff = self.n
            self.countOn = 0
        else:
            for i in range(self.n):
                self.arr[i] = 1
            self.countOff = 0
            self.countOn = self.n
        
    def count_ON(self): # O(1)
        return self.countOn
    
    def count_OFF(self): # O(1)
        return self.countOff
    
    def toggleAll(self): # O(N)
        for i in range(self.n):
            if self.arr[i]==0:
                self.arr[i]=1
                self.countOn+=1
                self.countOff-=1
            else:
                self.arr[i]=0
                self.countOff+=1
                self.countOn-=1
                
# Optimised solution with O(1) time for all
            
class Solution2:
    def __init__ (self, n: int):
        self.n = n
        self.arr = [0]*n # [(0,0)]
        self.globalVersion = 0
        
p = Solution(5)

print(p.count_ON())       # 0

p.set_i(1, 1)
p.set_i(3, 1)
print(p.get_i(1))          # 1
print(p.count_ON())       # 2

p.toggle(1)
p.toggle(2)
print(p.count_ON())       # 2

p.setAll(1)
print(p.get_i(0))          # 1
print(p.get_i(2))          # 1
print(p.count_ON())       # 5

p.set_i(2, 0)
p.set_i(4, 0)
p.toggle(0)
print(p.count_ON())       # 2

p.toggleAll()
print(p.get_i(0))          # 1
print(p.get_i(1))          # 0
print(p.get_i(2))          # 1
print(p.count_ON())       # 3

p.set_i(1, 1)
p.set_i(2, 0)
p.toggle(3)
print(p.count_ON())       # 4

p.setAll(0)
print(p.count_ON())       # 0
print(p.count_OFF())      # 5

p.toggleAll()
print(p.count_ON())       # 5

p.toggleAll()
print(p.count_ON())       # 0

p.set_i(4, 1)
p.set_i(4, 1)
print(p.count_ON())       # 1