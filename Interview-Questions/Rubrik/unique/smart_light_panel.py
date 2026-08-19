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
        self.arr = [[0,0] for _ in range(n)] # [[0,0]], [(value, timestamp/version)]
        self.globalVersion = 0
        self.globalStatus = 0
        self.countOn = 0
        self.countOff = n
        self.flip = False # only needed to apply toggleAll in O(1), we do not actually need to flip all the values just keep track of it
         
    def get_i(self, idx: int) -> int:
        val = self.arr[idx]
        if val[1] < self.globalVersion:
            res = self.globalStatus
        else:
            res = val[0]
        # now due to toggle all we need to check if the state is flipped before returning the value
        if self.flip:
            return 1 - res # if its 0, we return 1, if its 1 we return 0
        else:
            return res
        
    def set_i(self, idx, b): # O(1)
        current = self.get_i(idx) # do not use this: if b==0 and self.arr[idx][0]==1:, as this could have been offset by set_all or toggle all
        if b==0 and current == 1: 
            self.countOn-=1
            self.countOff+=1
        elif b==1 and current==0:
            self.countOff-=1
            self.countOn+=1
            
        # now due to toggle all we need to check if the state is flipped
        # if the state is flipped, the get_i call above handled it and so we need to add the opposite value
        if self.flip:
            res = 1 - b
        else:
            res = b
        self.arr[idx] = [res, self.globalVersion] # if this index's version was offset/left behind by setAll previously, it will now be updated to current global version
        # self.globalVersion+=1
        
    # def toggle(self, idx: int): # O(1) # this toggle works well when we do not have toggleAll and the flip variable
    #     current = self.get_i(idx)
    #     # to avoid the logic below, we could simply use: self.set_i(idx, 1 - current)
    #     if current==0:
    #         self.arr[idx][0] = 1
    #         self.countOn+=1
    #         self.countOff-=1
    #     else:
    #         self.arr[idx][0] = 0
    #         self.countOff+=1
    #         self.countOn-=1
    #     # self.globalVersion+=1
    #     self.arr[idx][1] = self.globalVersion # if this index's version was offset/left behind by setAll previously, it will now be updated to current global version
        
        
    # this is the lengthy version of toggle, when we have flip and toggleAll in place with O(1) toggle    
    # def toggle(self, idx: int):  # O(1)
    #     current = self.get_i(idx)

    #     if current == 0:
    #         # logically we want this light to become 1
    #         if self.flip:
    #             self.arr[idx][0] = 0
    #         else:
    #             self.arr[idx][0] = 1

    #         self.countOn += 1
    #         self.countOff -= 1

    #     else:
    #         # logically we want this light to become 0
    #         if self.flip:
    #             self.arr[idx][0] = 1
    #         else:
    #             self.arr[idx][0] = 0

    #         self.countOff += 1
    #         self.countOn -= 1

    #     self.arr[idx][1] = self.globalVersion
    
    # Best way to handle O(1) toggle when toggleAll and flip are in place
    def toggle(self, idx: int):
        current = self.get_i(idx)
        self.set_i(idx, 1 - current) # toggle value by 1 - current
        
    def setAll(self, b: int): # O(1)
        self.globalVersion+=1
        self.globalStatus = b
        # this resets everything and the flipped state too
        self.flip = False
        if b==0:
            self.countOff = self.n
            self.countOn = 0
        else:
            self.countOff = 0
            self.countOn = self.n
        
    def count_ON(self): # O(1)
        return self.countOn
    
    def count_OFF(self): # O(1)
        return self.countOff
    
    def toggleAll(self): # O(1)
        self.flip = not self.flip
        self.countOff, self.countOn = self.countOn, self.countOff
    
p = Solution2(5)

print(f"Expected answer: 0, Actual Answer {p.count_ON()}")       # 0

p.set_i(1, 1)
p.set_i(3, 1)
print(f"Expected answer: 1, Actual Answer {p.get_i(1)}")          # 1
print(f"Expected answer: 2, Actual Answer {p.count_ON()}")       # 2

p.toggle(1)
p.toggle(2)
print(f"Expected answer: 2, Actual Answer {p.count_ON()}")       # 2

p.setAll(1)
print(f"Expected answer: 1, Actual Answer {p.get_i(0)}")          # 1
print(f"Expected answer: 1, Actual Answer {p.get_i(2)}")          # 1
print(f"Expected answer: 5, Actual Answer {p.count_ON()}")       # 5

p.set_i(2, 0)
p.set_i(4, 0)
p.toggle(0)
print(f"Expected answer: 2, Actual Answer {p.count_ON()}")       # 2

p.toggleAll()
print(f"Expected answer: 1, Actual Answer {p.get_i(0)}")          # 1
print(f"Expected answer: 0, Actual Answer {p.get_i(1)}")          # 0
print(f"Expected answer: 1, Actual Answer {p.get_i(2)}")          # 1
print(f"Expected answer: 3, Actual Answer {p.count_ON()}")       # 3

p.set_i(1, 1)
p.set_i(2, 0)
p.toggle(3)
print(f"Expected answer: 4, Actual Answer {p.count_ON()}")       # 4

p.setAll(0)
print(f"Expected answer: 0, Actual Answer {p.count_ON()}")       # 0
print(f"Expected answer: 5, Actual Answer {p.count_OFF()}")      # 5

p.toggleAll()
print(f"Expected answer: 5, Actual Answer {p.count_ON()}")       # 5

p.toggleAll()
print(f"Expected answer: 0, Actual Answer {p.count_ON()}")       # 0

p.set_i(4, 1)
p.set_i(4, 1)
print(f"Expected answer: 1, Actual Answer {p.count_ON()}")       # 1

# This is dangerous:

# self.arr = [[0,0]] * n

# All entries initially reference the same inner list.

# For example:

# arr = [[0,0]] * 3
# arr[0][0] = 1


# print(arr)

# produces:

# [[1,0], [1,0], [1,0]]

# because all three entries point to the same [0,0].


# Dry run:
# Start: arr=[[0,0],[0,0],[0,0]], globalVersion=0, globalStatus=0, flip=False, countOn=0

# set_i(1,1):
# get_i(1)=0 -> change 0->1 -> arr[1]=[1,0], countOn=1
# Logical lights: [0,1,0]

# setAll(1):
# globalVersion=1, globalStatus=1, flip=False, countOn=3
# arr is NOT changed, but old versions are stale
# get_i(0): arr[0]=[0,0], 0<1 -> use globalStatus=1
# Logical lights: [1,1,1]

# set_i(1,0):
# get_i(1)=1 because its old version is stale -> change 1->0
# arr[1]=[0,1], countOn=2
# Logical lights: [1,0,1]

# toggleAll():
# flip=True, swap countOn/countOff
# arr is NOT changed
# Logical lights become: [0,1,0]

# get_i(1):
# arr[1]=[0,1] -> version is current, so res=0
# flip=True -> return 1-res = 1

# set_i(0,1) while flip=True:
# get_i(0)=0 logically
# We want logical value 1, but because flip=True we store 0
# arr[0]=[0,1]
# Later get_i(0): stored 0 -> flipped -> returns 1

# toggle(idx):
# current=get_i(idx), then set_i(idx, 1-current)
# This automatically handles both setAll and toggleAll states