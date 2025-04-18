# 163. Missing Ranges

# You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are within the inclusive range.

# A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

# Return the shortest sorted list of ranges that exactly covers all the missing numbers. That is, no element of nums is included in any of the ranges, and each missing number is covered by one of the ranges.

# Example 1:

# Input: nums = [0,1,3,50,75], lower = 0, upper = 99
# Output: [[2,2],[4,49],[51,74],[76,99]]
# Explanation: The ranges are:
# [2,2]
# [4,49]
# [51,74]
# [76,99]
# Example 2:

# Input: nums = [-1], lower = -1, upper = -1
# Output: []
# Explanation: There are no missing ranges since there are no missing numbers.
 
# Constraints:

# -109 <= lower <= upper <= 109
# 0 <= nums.length <= 100
# lower <= nums[i] <= upper
# All the values of nums are unique.

from typing import List
# time complexity O(N)
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        res = []
        if not nums:
            return [[lower, upper]]
        if nums[0]!=lower:
            res.append([lower,nums[0]-1])
        for i in range(len(nums)-1):
            if nums[i]!=nums[i+1]-1:
                res.append([nums[i]+1, nums[i+1]-1])
        if nums[len(nums)-1]!=upper:
            res.append([nums[len(nums)-1]+1,upper])
        return res
    
# More efficient handling of edge cases

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        # prepend a “left” sentinel and append a “right” sentinel
        extended = [lower - 1] + nums + [upper + 1]
        res = []
        for i in range(len(extended) - 1):
            lo, hi = extended[i] + 1, extended[i + 1] - 1
            if lo <= hi:
                res.append([lo, hi])
        return res