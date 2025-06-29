# 128. Longest Consecutive Sequence

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.


# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# Example 3:

# Input: nums = [1,0,1,2]
# Output: 3
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109

from typing import List

# Solution 1: Using Sorting, time complexity O(n log n), space complexity O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums = list(set(nums))
        nums.sort()
        i = 0
        max_count = 1
        while i<len(nums)-1:
            count = 1
            while i<len(nums)-1 and (nums[i]+1)==nums[i+1]:
                count+=1
                i+=1
            i+=1
            max_count = max(max_count, count)
        return max_count


# Solution 2: Using Hash Set, time complexity O(n), space complexity O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums_set = set(nums)
        max_len = 0
        for n in nums_set:
            # check if it's start of a sequence
            if (n-1) in nums_set: # here can also use if n not in nums_set: to check if it's the start
                continue
            count = 0
            while (n+count) in nums_set:
                count+=1
            max_len = max(max_len, count)
        return max_len