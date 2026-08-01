# 18. 4Sum

# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:

# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
 

# Constraints:

# 1 <= nums.length <= 200
# -109 <= nums[i] <= 109
# -109 <= target <= 109

from typing import List
# Time complexity: O(N^3)
# Space complexity: O(N)

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        if len(nums)<4:
            return []
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    for l in range(k+1, n):
                        if nums[i]+nums[j]+nums[k]+nums[l]==target:
                            res.add(tuple(sorted([nums[i], nums[j], nums[k], nums[l]])))
        return list(res)


# Optimised solution, Time complexity: O(N^3), 2 for loops and then while loop
# Space complexity: O(N), Python's .sort() uses Timsort, 
# which — despite sorting in-place (no new array returned) — has a worst-case O(n) auxiliary space requirement internally, 
# due to the temporary merge buffers it uses during the merge step of its hybrid merge-sort/insertion-sort algorithm.
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort() # O(NlogN)
        res = []
        n = len(nums)
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]: # continue if the next digit is same as previous. Here we have i>0 so that we can at least consider that solution once and then ignore it in later iterations
                continue
            for j in range(i+1, n):
                if j>i+1 and nums[j]==nums[j-1]: # same reason as above
                    continue
                l = j+1
                r = n-1
                while l<r:
                    total = nums[i]+nums[j]+nums[l]+nums[r]
                    if total == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l+=1
                        r-=1
                        while l<r and nums[l]==nums[l-1]:
                            l+=1
                        while l<r and nums[r] == nums[r+1]:
                            r-=1
                    elif total<target:
                        l+=1
                    else:
                        r-=1
        return res