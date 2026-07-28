# 153. Find Minimum in Rotated Sorted Array (Neecode 150) Important

# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
# Example 2:

# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
# Example 3:

# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 

# Constraints:

# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# All the integers of nums are unique.
# nums is sorted and rotated between 1 and n times.

# Both the solutions below have time complexity of O(log n) and space complexity of O(1).

# Neetcode solution:
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        res = nums[l]
        while l<=r:
            if nums[r]>nums[l]: # remaining array is sorted
                res = min(res, nums[l])
                break
            mid = (l+r)//2
            res = min(res, nums[mid])
            if nums[mid]>=nums[l]: # means we are in the left sorted portion
                l = mid+1
            else: # in right sorted portion
                r = mid-1
        return res

# CodeStoryWithMIK solution:

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l<r: # here we use < instead of <= to avoid infinite loop as we are doing r = mid in the else condition
            mid = (l+r)//2
            if nums[mid]>nums[r]: # break in ascending order found, therefore move right
                l=mid+1
            else:
                r = mid # here we do not do mid-1 because we want to include mid in the next iteration as mid could be the minimum element
        return nums[r]
    
    
# The core idea

# A rotated sorted array has exactly one "breakpoint" — the spot where a smaller number suddenly follows a bigger one. That breakpoint is where the minimum lives. 
# Everything is otherwise sorted in two ascending chunks.

# The trick: at any mid, compare nums[mid] to nums[r] (the right edge, not the left edge — this matters).

# If nums[mid] > nums[r]: the minimum can't be at or before mid, because if it were, the array from mid to r would have to be sorted ascending (no rotation point in that range) — but it's not, since nums[mid] > nums[r] proves a rotation point exists somewhere between mid and r. So the min is strictly to the right of mid → l = mid + 1.
# If nums[mid] <= nums[r]: the segment from mid to r is sorted ascending (no breakpoint in this range) — so the minimum is either mid itself or somewhere to its left. Since mid could still be the answer, we don't exclude it → r = mid (not mid - 1).

# The loop ends when l == r — that's the minimum.

# Dry run: nums = [4,5,6,7,0,1,2]

# Indices: 0:4, 1:5, 2:6, 3:7, 4:0, 5:1, 6:2

# Start: l=0, r=6

# Iteration 1:

# mid = (0+6)//2 = 3 → nums[3] = 7
# Compare nums[mid]=7 vs nums[r]=2: 7 > 2 → minimum is to the right of mid
# l = mid+1 = 4

# State: l=4, r=6

# Iteration 2:

# mid = (4+6)//2 = 5 → nums[5] = 1
# Compare nums[mid]=1 vs nums[r]=2: 1 <= 2 → segment mid..r is sorted, min is at mid or to its left
# r = mid = 5

# State: l=4, r=5

# Iteration 3:

# mid = (4+5)//2 = 4 → nums[4] = 0
# Compare nums[mid]=0 vs nums[r]=1: 0 <= 1 → min is at mid or to its left
# r = mid = 4

# State: l=4, r=4 → loop ends (l == r)

# Return nums[4] = 0 ✅ correct.

# Why r = mid and not r = mid - 1

# This is the detail that trips people up. Compare to standard binary search where you'd do r = mid - 1 when you've ruled out mid. 
# Here, we haven't ruled out mid — it's still a live candidate for being the minimum itself (since the condition nums[mid] <= nums[r] doesn't tell us mid isn't the min, just that the true min is somewhere in [l, mid]). 
# So we keep mid in the search range by setting r = mid instead of excluding it.

# Meanwhile, in the other branch, nums[mid] > nums[r] does definitively rule out mid as the minimum (since something smaller — nums[r] — exists to its right), so it's safe to fully exclude it with l = mid + 1.

# Why compare against nums[r] and not nums[l]

# If you compared against nums[l] instead, you couldn't always tell which half contains the rotation point — e.g. nums[mid] > nums[l] is true both when mid is in the "still ascending from l" region and sometimes even across the rotation. 
# Comparing to nums[r] avoids this ambiguity: nums[mid] > nums[r] unambiguously means the breakpoint is between mid and r.