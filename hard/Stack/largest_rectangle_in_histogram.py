# 84. Largest Rectangle in Histogram
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
# time complexity: O(N^2) due to 2 for loops, space complexity: O(N)

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            minh = heights[i]
            for j in range(i, len(heights)):
                minh = min(heights[j], minh)
                width = j-i+1
                max_area = max(max_area, minh*width)
        return max_area

sol = Solution()
ans = sol.largestRectArea(heights = [2,1,5,6,2,3])

print(ans)


# Time complexity: O(n), where n is the number of elements in the heights list, since we have to traverse the list once. 
# and in stack we push and pop each element at most once.
# Space complexity: O(n), for the stack that stores indices of the heights.

# Best solution
# Video link: https://www.youtube.com/watch?v=OQJjh6AT00g
# If we want to avoid the flush loop:
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # will hold the index and not the height
        heights = heights + [0]   # append sentinel becuase we start the loop if we see a lower height on the right, 
        # a 0 to the right will calculate areas considering the remaining values in the stack
        # original: [2,1,5,6,2,3] → becomes [2,1,5,6,2,3,0]

        for i in range(len(heights)):   # now loops one extra time, i=6
            while stack and heights[i] < heights[stack[-1]]: # we only check the right less value
                height = heights[stack.pop()] # The popped bar is treated as the height of the rectangle.
                width = i - stack[-1] - 1 if stack else i # Explanation below
                maxArea = max(maxArea, height * width)
            stack.append(i)

        return maxArea   # no flush loop needed — everything already got popped

# Understanding: width = i - stack[-1] - 1 if stack else i
# After popping:
# - i is the first smaller bar on the RIGHT
# - stack[-1] is the first smaller bar on the LEFT
#
# Therefore the rectangle can extend from:
# stack[-1] + 1  to  i - 1
#
# Width = (i - 1) - (stack[-1] + 1) + 1
#       = i - stack[-1] - 1
#
# If the stack is empty, there is no smaller bar on the left,
# so the rectangle extends all the way back to index 0.

# Understanding width formula with example:
# Say you have index positions: 0, 1, 2, 3, 4, 5

# If L = 1 and R = 4 are your two boundary markers, how many positions are strictly between them (not including L or R themselves)?

# 0   1   2   3   4   5
#     L   ?   ?   R

# Positions between: 2 and 3 → that's 2 positions.

# Formula: R - L - 1 = 4 - 1 - 1 = 2

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