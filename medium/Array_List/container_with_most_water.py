# 11. Container With Most Water (Neetcode 150) Important
# Topics: Array, Two Pointers, Greedy

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# Example 1:

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1

# Constraints:

# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104


# Brute force solution
# Time Complexity: O(n^2)
# Space Complexity: O(1)
class Solution:
    def maxVol(self, nums: List[int]) -> int:
        max_vol = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                length = j-i
                height = min(nums[i], nums[j])
                max_vol = max(max_vol, length*height)
        return max_vol

sol = Solution()
ans = sol.maxVol([1,8,6,2,5,4,8,3,7])
print(ans)



# Time Complexity: O(n)
# Space Complexity: O(1)
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_vol = 0
        l = 0
        r = len(height)-1
        while l<r:
            vol = (r-l)*min(height[l],height[r]) # width * height
            # we take the minimum height because the water cannot overflow
            max_vol = max(vol, max_vol)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_vol


# how do you know you're not skipping over a better answer?" Here's the reasoning you should be able to state:

# At any step, the width can only shrink as l and r move inward — it never grows again. 
# So the only way a future position could beat the current volume is if the height increases enough to outweigh the smaller width. 
# Now, the container's height is always limited by the shorter of the two lines. 
# If I move the pointer at the taller line instead, the width still shrinks, but the height is still capped by the same short line 
# (or gets even worse if the new line is shorter) — so that move can never produce a better result. 
# Moving the shorter line's pointer is the only move that has any chance of increasing the height enough to compensate for the 
# reduced width. That's why it's always safe (and necessary) to move the shorter pointer.