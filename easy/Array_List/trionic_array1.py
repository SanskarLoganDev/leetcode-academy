# 3637. Trionic Array I

# You are given an integer array nums of length n.

# An array is trionic if there exist indices 0 < p < q < n − 1 such that:

# nums[0...p] is strictly increasing,
# nums[p...q] is strictly decreasing,
# nums[q...n − 1] is strictly increasing.
# Return true if nums is trionic, otherwise return false.

 

# Example 1:
# Input: nums = [1,3,5,4,2,6]
# Output: true

# Explanation:
# Pick p = 2, q = 4:
# nums[0...2] = [1, 3, 5] is strictly increasing (1 < 3 < 5).
# nums[2...4] = [5, 4, 2] is strictly decreasing (5 > 4 > 2).
# nums[4...5] = [2, 6] is strictly increasing (2 < 6).

# Example 2:
# Input: nums = [2,1,3]
# Output: false
# Explanation:
# There is no way to pick p and q to form the required three segments.

# Constraints:

# 3 <= n <= 100
# -1000 <= nums[i] <= 1000

from typing import List
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        p = -1 # index where increasing changes to decreasing
        q = -1 # index where decreasing changes to increasing
        n = len(nums)
        if nums[n-1]<nums[n-2]: # if last part is not increasing
            return False
        phase = 0
        for i in range(1, n):
            if nums[i]==nums[i-1]: # equal elements are not allowed
                return False
            if phase == 0: # increasing phase
                if nums[i]>nums[i-1]:
                    continue
                else:
                    phase = 1
                    p = i-1

            if phase == 1: # decreasing phase
                if nums[i]<nums[i-1]:
                    continue
                else:
                    phase = 2
                    q = i-1
                
            if phase == 2: # 2nd increasing phase
                if nums[i]>nums[i-1]:
                    continue
                else:
                    return False
        # ensure that we had all 3 phases and valid p and q indices
        return  p>0 and p<q and q<n-1 and phase==2 