# 442. Find All Duplicates in an Array

# Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears at most twice, return an array of all the integers that appears twice.

# You must write an algorithm that runs in O(n) time and uses only constant auxiliary space, excluding the space needed to store the output

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]
# Example 2:

# Input: nums = [1,1,2]
# Output: [1]
# Example 3:

# Input: nums = [1]
# Output: []
 

# Constraints:

# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= n
# Each element in nums appears once or twice.

# IT IS MENTIONED IN QUESTION THAT THE VALUES ARE [1,n] SO WE USE THE ALGO FOR THIS 

from typing import List
# Time complexity: O(NlogN)
# Space complexity: O(1)
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                res.append(nums[i])
        return res
    
# time complexity: O(N)
# space complexity: O(N)
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hm = {}
        res = []
        for n in nums:
            hm[n] = hm.get(n, 0)+1
        for k, v in hm.items():
            if v==2:
                res.append(k)
        return res
    
# time complexity: O(N)
# Space complexity: O(1)    
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            num = abs(nums[i]) # so that if we face a negative value we can accurately calculate idx
            idx = num-1
            if nums[idx]<0:
                res.append(abs(nums[i])) # we do abs here to avoid adding -ve value to res
                continue
            nums[idx] = -nums[idx]
        return res
        