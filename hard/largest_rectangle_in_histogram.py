# 84. Largest Rectangle in Histogram Hard
# Neetcode 150 (Important)

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

# Brute force solution:
# time complexity: O(N^3) due to 2 for loops and min calculation, spece complexity: O(N)

from typing import List

class Solution:

    def largestRectArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        for i in range(n): # O(N)
            for j in range(i+1, n+1): # O(N)
                min_height = min(heights[i:j]) # O(N)
                area = min_height*(j-i)
                max_area = max(max_area, area)
        return max_area

sol = Solution()
ans = sol.largestRectArea(heights = [2,1,5,6,2,3])

print(ans)


# Time complexity: O(n), where n is the number of elements in the heights list, since we have to traverse the list once. 
# and in stack we push and pop each element at most once.
# Space complexity: O(n), for the stack that stores indices of the heights.

from typing import List

class Solution:

    def largestRectArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        stack = []
        for i in range(n):
            # Pop from stack while the current height is less than the height at the top of the stack
            while stack and heights[i]<heights[stack[-1]]:
                # Pop the bar we're finalizing.
                height = heights[stack.pop()]
                # # After popping, stack[-1] (if it exists) is the nearest bar to the LEFT that is shorter than `height`
                width = i - stack[-1] - 1 if stack else i # explanation below (number of positions strictly between the two boundaries)
                max_area = max(max_area, height*width)
            stack.append(i)
        
        # Flush pass: whatever's left in the stack has no shorter bar to its right
        for i in range(len(stack)):
            height = heights[stack.pop()]
            # Same width logic as above, but R = n instead of i, since we've run off the end
            width = n - stack[-1] - 1 if stack else n
            max_area = max(max_area, height*width)
        return max_area

sol = Solution()
ans = sol.largestRectArea(heights = [2,1,5,6,2,3])

print(ans)

# Understanding width formula:
# Say you have index positions: 0, 1, 2, 3, 4, 5

# If L = 1 and R = 4 are your two boundary markers, how many positions are strictly between them (not including L or R themselves)?

# 0   1   2   3   4   5
#     L   ?   ?   R

# Positions between: 2 and 3 → that's 2 positions.

# Formula: R - L - 1 = 4 - 1 - 1 = 2

# Same complexities

# If we want to avoid the flush loop:
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        heights = heights + [0]   # append sentinel
        # original: [2,1,5,6,2,3] → becomes [2,1,5,6,2,3,0]

        for i in range(len(heights)):   # now loops one extra time, i=6
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1 if stack else i
                maxArea = max(maxArea, height * width)
            stack.append(i)

        return maxArea   # no flush loop needed — everything already got popped
            

# Neetcode solution with same complexities, here the stack structure is complex to understand and in the previous solutions the width forumla is complex to understand
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