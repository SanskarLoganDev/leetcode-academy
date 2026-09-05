# 42. Trapping Rain Water
# Neetcode 150

# Topics: # Array, Two Pointers, Stack, # Dynamic Programming, Monotonic Stack

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Example 1:

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9
 

# Constraints:

# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105

from typing import List

# (My Solution)
# Time Complexity: O(n^2) - We traverse the height array once to calculate the trapped water and slicing operations take O(n) time for each element.
# The overall time complexity is O(n^2) because we are calculating the maximum height
# Space Complexity: O(n) - We use two additional arrays to store the maximum heights
class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0]
        max_right = []
        total = 0
        for i in range(1,len(height)):
            max_left.append(max(height[0:i])) # each slice is length ≈ n–1–i and max over it is O(n–1–i). Summing (n–1) + (n–2) + … + 1 = O(n^2).
        for i in range(len(height)-1):
            max_right.append(max(height[i+1:len(height)]))
        max_right.append(0)
        for i in range(len(height)):
            vol = min(max_left[i], max_right[i]) - height[i]
            if vol > 0:
                total+=vol
        return total
    
# Same code but optimized by comparing adjacent heights. 

# Approach when not including the current index in left max and right max calculations
# Time complexity: O(N), Space complexity: O(N)
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0]*n
        right_max = [0]*n
        total = 0
        # in the below loop we do not include 0 index as water will fall off of it anyways
        for i in range(1, n): # maximum value to the left of the current index
            left_max[i] = max(left_max[i-1], height[i-1])

        # in the below loop we do not include n-1 index as water will fall off of it anyways
        for i in range(n-2, -1, -1): # maximum value to the right of the current index
            right_max[i] = max(right_max[i+1], height[i+1])

        for i in range(1, n-1): # water will fall off of the end indexes
            vol = min(left_max[i], right_max[i]) - height[i]
            if vol>0:
                total+=vol
        
        return total
                

sol = Solution()
ans = sol.trapRain([0,1,0,2,1,0,1,3,2,1,2,1]) # [4,2,0,3,2,5]
print(ans)

# Approach including the current index in left max and right max calculations
# Time complexity: O(N), Space complexity: O(N)
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left = [0]*n 
        max_right = [0]*n
        max_left[0] = height[0]
        max_right[-1] = height[n-1]
        total = 0
        for i in range(1, n):
            max_left[i] = max(max_left[i-1], height[i])

        for i in range(n-2, -1, -1):
            max_right[i] = max(max_right[i+1], height[i])

        for i in range(n):
            vol = min(max_left[i], max_right[i]) - height[i]
            if vol>0:
                total+=vol
        return total

# Two Pointers Approach (Optimised approach)
# Time Complexity: O(n) - We traverse the height array once to calculate the trapped water.
# Space Complexity: O(1) - We use two pointers to keep track of the left and right walls, so we don't need any additional space.

# Explanation:# We use two pointers, one starting from the left and one from the right.
# We keep track of the maximum height seen so far from both sides.

# Approach including the current index in left max and right max calculations
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l,r = 0, n-1
        left_max, right_max = height[l], height[r] # on the initial and last indexes there would be no trapped water therefore it does not matter
        total = 0
        while l<r: # l<r because we already do l+=1 or r-=1 in the if and else statements before processing
            if left_max<right_max: 
                l+=1
                # current height is included in the max_left
                left_max = max(left_max, height[l])
                vol = min(left_max, right_max) - height[l]
                if vol>0:
                    total+=vol
            else:
                r-=1
                # current height is included in the max_right
                right_max = max(right_max, height[r])
                vol = min(left_max, right_max) - height[r]
                if vol>0:
                    total+= vol
        return total
    
# Approach when not including the current height in left max and right max calculations
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
        l = 1
        r = n-2
        max_left = height[0]
        max_right = height[n-1]
        total = 0
        while l<=r: # l<=r because we do l+=1 or r-=1 at the end and we do not want a central value to be skipped
            if max_left < max_right:
                # current height not included in max_left
                vol = min(max_left, max_right) - height[l]
                if vol>0:
                    total+=vol
                max_left = max(max_left, height[l]) # now current height is used
                l+=1
      
            else:
                # current height not included in max_right
                vol = min(max_left, max_right) - height[r]
                if vol>0:
                    total+=vol
                max_right = max(max_right, height[r]) # now current height is used
                r-=1

        return total

# in the 2 pointers approach or the left_max & right_max array approach, you can either include or exclude the current index in the left_max and right_max calculation
# as it wont affect the result in any way
# Example where current bar IS the maximum

# Take:

# height = [1, 5, 2]

# At i = 1, current height is 5.

# Version 1:

# left max excluding current = 1
# right max excluding current = 2

# min(1,2) - 5 = -4
# => no water

# Version 2:

# max_left[1] = 5
# max_right[1] = 5

# min(5,5) - 5 = 0

# Still no water.

# So including the current bar changes the intermediate maximums, but not the final trapped water.

# Why mathematically both are valid

# Water at index i cannot be negative:

# water = max(0, min(left boundary, right boundary) - height[i])

# If height[i] is taller than one of the true surrounding boundaries, then version 1 gives a negative result, which you ignore.

# Version 2 instead lets height[i] become the maximum itself, which makes:

# min(...) - height[i] = 0

# So both end up adding 0.


# Dynamic Programming Approach
# Time Complexity: O(n) - We traverse the height array once to calculate the trapped water.
# Space Complexity: O(n) - We use two additional arrays to store the maximum heights
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left = [0]*n
        max_right = [0]*n
        l_wall, r_wall = 0,0
        total = 0
        for i in range(n):
            j = -i-1 # j is the index from the right side, so it starts from -1 and goes to -n
            max_left[i] = l_wall
            max_right[j] = r_wall
            l_wall = max(l_wall, height[i]) # max_left[i] will store the maximum height to the left of index i
            r_wall = max(r_wall, height[j]) # max_right[j] will store the maximum height to the right of index j
        # Now we can calculate the trapped water
        for i in range(n):
            vol = min(max_left[i],max_right[i])-height[i]
            if vol>0:
                total+=vol
        return total
