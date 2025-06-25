# 414. Third Maximum Number

# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

# Example 1:

# Input: nums = [3,2,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2.
# The third distinct maximum is 1.
# Example 2:

# Input: nums = [1,2]
# Output: 2
# Explanation:
# The first distinct maximum is 2.
# The second distinct maximum is 1.
# The third distinct maximum does not exist, so the maximum (2) is returned instead.
# Example 3:

# Input: nums = [2,2,3,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2 (both 2's are counted together since they have the same value).
# The third distinct maximum is 1.
 
# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1
 

# Follow up: Can you find an O(n) solution?

# Time complexity O(N), space complexity O(N) where N is the number of distinct elements in nums.

from typing import List
import heapq
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max_heap = [-x for x in set(nums)]
        heapq.heapify(max_heap)
        if len(max_heap)>=3:
            heapq.heappop(max_heap)
            heapq.heappop(max_heap)
            return -(heapq.heappop(max_heap))
        else:
            return -(heapq.heappop(max_heap))
        
# Time complexity O(N), space complexity O(1) where N is the length of nums.

import heapq
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums =set(nums)
        if len(nums)<3:
            return max(nums)
        else:
            nums.remove(max(nums))
            nums.remove(max(nums))
            return max(nums)
        
        