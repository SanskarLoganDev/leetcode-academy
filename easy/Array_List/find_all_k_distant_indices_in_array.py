# 2200. Find All K-Distant Indices in an Array

# You are given a 0-indexed integer array nums and two integers key and k. A k-distant index is an index i of nums for which there exists at least one index j such that |i - j| <= k and nums[j] == key.

# Return a list of all k-distant indices sorted in increasing order.

# Example 1:

# Input: nums = [3,4,9,1,3,9,5], key = 9, k = 1
# Output: [1,2,3,4,5,6]
# Explanation: Here, nums[2] == key and nums[5] == key.
# - For index 0, |0 - 2| > k and |0 - 5| > k, so there is no j where |0 - j| <= k and nums[j] == key. Thus, 0 is not a k-distant index.
# - For index 1, |1 - 2| <= k and nums[2] == key, so 1 is a k-distant index.
# - For index 2, |2 - 2| <= k and nums[2] == key, so 2 is a k-distant index.
# - For index 3, |3 - 2| <= k and nums[2] == key, so 3 is a k-distant index.
# - For index 4, |4 - 5| <= k and nums[5] == key, so 4 is a k-distant index.
# - For index 5, |5 - 5| <= k and nums[5] == key, so 5 is a k-distant index.
# - For index 6, |6 - 5| <= k and nums[5] == key, so 6 is a k-distant index.
# Thus, we return [1,2,3,4,5,6] which is sorted in increasing order. 
# Example 2:

# Input: nums = [2,2,2,2,2], key = 2, k = 2
# Output: [0,1,2,3,4]
# Explanation: For all indices i in nums, there exists some index j such that |i - j| <= k and nums[j] == key, so every index is a k-distant index. 
# Hence, we return [0,1,2,3,4].

# Time complexity: O(N * M), where N is the length of nums and M is the number of occurrences of key in nums. (Worst case, every element is key, therefore time complexity is O(N^2)).
# Space complexity: O(N), where N is the length of nums, for storing the result

from typing import List
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        keys = []
        res = set()
        for i in range(len(nums)):
            if nums[i] == key:
                keys.append(i)
        if len(keys)==0:
            return []
        for i in range(len(nums)):
            for key in keys:
                if abs(i-key)<=k:
                    res.add(i)
                    
        return list(res)
    
# Using 2 pointers to optimize the solution.
# Time complexity: O(2*N), where N is the length of nums and we traverse nums twice (i and j)
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res = []
        for j in range(len(nums)):
            if nums[j]==key:
                start = max(0, j-k) # here we ensure that start is not less than 0
                end = min(j+k, len(nums)-1) # here we take min to ensure that end does not exceed the length of nums
                if len(res)!=0 and start<=res[-1]: # here we check if the start is less than or equal to the last element in res to avoid repition
                    start = res[-1]+1
                for i in range(start, end+1):
                    res.append(i)
        return res