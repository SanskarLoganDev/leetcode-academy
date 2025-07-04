# 84. Largest Rectangle in Histogram Hard

# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram. 

# Example 1:


# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.
# Example 2:


# Input: heights = [2,4]
# Output: 4
 

# Constraints:

# 1 <= heights.length <= 105
# 0 <= heights[i] <= 104

from typing import List

# Time complexity: O(n), where n is the number of elements in the heights list, since we have to traverse the list once. and in stack we push and pop each element at most once.
# Space complexity: O(n), for the stack that stores indices of the heights.

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # (index, height) # to store the index and height of the histogram bars
        for i in range(len(heights)):
            start = i
            # Pop from stack while the current height is less than the height at the top of the stack
            while stack and heights[i]<stack[-1][1]: 
                index, height = stack.pop()
                maxArea = max(maxArea, height*(i-index)) # calculate area with the popped height, here i is the current index and index is the index of the popped height
                start = index
            stack.append((start, heights[i]))
            
        # Now pop all remaining elements in the stack
        for i in range(len(stack)):
            index, height = stack.pop()
            maxArea = max(maxArea, height*(len(heights)-index)) # here len(heights) is the width of the histogram, since we are at the end of the histogram and index is the index of the height in the stack

        return maxArea