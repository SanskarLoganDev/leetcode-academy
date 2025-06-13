# 485. Max Consecutive Ones

# Given a binary array nums, return the maximum number of consecutive 1's in the array.


# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 2
 
# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.

# both solutions have time complexity O(n), space complexity O(1)

from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        counts=[]
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            elif nums[i]==0:
                counts.append(count)
                count=0
        if count!=0:
            counts.append(count)
        
        return max(counts)


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_count = 0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            elif nums[i]==0:
                max_count = max(max_count, count)
                count=0
        if count!=0:
            max_count = max(max_count, count)
        
        return max_count