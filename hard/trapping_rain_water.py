# 42. Trapping Rain Water

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

# Two Pointers Approach
# Time Complexity: O(n) - We traverse the height array once to calculate the trapped water.
# Space Complexity: O(1) - We use two pointers to keep track of the left and right walls, so we don't need any additional space.