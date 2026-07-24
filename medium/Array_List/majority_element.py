# 229. Majority Element II

# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

# Example 1:

# Input: nums = [3,2,3]
# Output: [3]

# Example 2:

# Input: nums = [1]
# Output: [1]

# Example 3:

# Input: nums = [1,2]
# Output: [1,2]
 

# Constraints:

# 1 <= nums.length <= 5 * 104
# -109 <= nums[i] <= 109
 

# Follow up: Could you solve the problem in linear time and in O(1) space?

from typing import List

# time complexity: O(nlogn), space: O(N) but if we exclude the result array: O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = set()
        cand = nums[0]
        count = 0
        for n in nums:
            if n == cand:
                count+=1
            else:
                cand = n
                count = 1
            if count > len(nums)//3:
                    res.add(n)
        return list(res)
    