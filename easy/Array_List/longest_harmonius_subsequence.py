# 594. Longest Harmonious Subsequence

# We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

# Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

# Example 1:

# Input: nums = [1,3,2,2,5,2,3,7]

# Output: 5

# Explanation:

# The longest harmonious subsequence is [3,2,2,2,3].

# Example 2:

# Input: nums = [1,2,3,4]

# Output: 2

# Explanation:

# The longest harmonious subsequences are [1,2], [2,3], and [3,4], all of which have a length of 2.

# Example 3:

# Input: nums = [1,1,1,1]

# Output: 0

# Explanation:

# No harmonic subsequence exists.

# Constraints:

# 1 <= nums.length <= 2 * 104
# -109 <= nums[i] <= 109

from typing import List

# Time Complexity: O(n log n) due to sorting, space complexity is O(1) if we ignore the input size.
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        l = 0
        r = 1
        max_len = 0
        if len(nums)==1:
            return max_len
        for r in range(len(nums)):
            # 1) Shrink from left if window no longer harmonious
            while nums[r] - nums[l] > 1:
                l += 1

            # 2) If it is harmonious, update answer
            if nums[r] - nums[l] == 1:
                max_len = max(max_len, r - l + 1)

        return max_len
            