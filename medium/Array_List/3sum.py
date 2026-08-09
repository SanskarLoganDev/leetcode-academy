# 15. 3Sum (Neetcode 150) Important
# Topics: Array, Two Pointers, Sorting
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

# Brute force:
# Time complexity: O(N^3), we do not consider time complexity of sorted or type casting as it is a fixed size of 3 (3log3)
# Space complexity: O(N) for set
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hashset = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                        triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                        hashset.add(triplet)
        return list(hashset)

# Using 2 sum solution
# time complexity: O(n^2)
# Space complexity: O(n)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result_set = set()  # stores distinct triplets to avoid duplicates
        
        for i in range(n):
            seen = set()  # tracks numbers seen so far in the inner loop
            target = -nums[i]  # we need two numbers from the rest that sum to this
            
            for j in range(i + 1, n):
                complement = target - nums[j]
                if complement in seen:
                    # found a valid triplet: nums[i], nums[j], complement
                    triplet = tuple([nums[i], nums[j], complement])
                    result_set.add(triplet)
                seen.add(nums[j])
        
        return [list(t) for t in result_set]

# # Time Complexity: O(n^2)  (O(n log n) for sorting + O(n^2) for the two-pointer approach)
# # Space Complexity: O(1)

from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i]>0: # if the first element is greater than 0, then no triplet can sum to 0
                break  # you can also return here as the future solutions will start with a positive solution too
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