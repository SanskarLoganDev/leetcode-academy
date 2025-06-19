# 15. 3Sum (Neetcode 150) Important

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
 
# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105

from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i]>0: # if the first element is greater than 0, then no triplet can sum to 0
                break 
            if i>0 and nums[i]==nums[i-1]: # to skip duplicates
                # if the current element is same as the previous element, then we skip it
                continue
            l,r=i+1, len(nums)-1
            while l<r: # becaus l and r cannot be same therefore l<=r is not chosen
                total = nums[i]+nums[l]+nums[r]
                if total==0:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1 # to move to next element
                    r-=1
                    # below two while loops are used to skip duplicates
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
                elif total<0:
                    l+=1
                else:
                    r-=1

        return res