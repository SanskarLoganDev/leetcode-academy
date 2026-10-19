# 2089. Find Target Indices After Sorting Array

# You are given a 0-indexed integer array nums and a target element target.

# A target index is an index i such that nums[i] == target.

# Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

# Example 1:

# Input: nums = [1,2,5,2,3], target = 2
# Output: [1,2]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The indices where nums[i] == 2 are 1 and 2.

# Example 2:

# Input: nums = [1,2,5,2,3], target = 3
# Output: [3]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The index where nums[i] == 3 is 3.

# Example 3:

# Input: nums = [1,2,5,2,3], target = 5
# Output: [4]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The index where nums[i] == 5 is 4.
 

# Constraints:

# 1 <= nums.length <= 100
# 1 <= nums[i], target <= 100

# time complexity: O(N)
# space complexity: O(N)
class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        count_less = 0
        count_target = 0
        for n in nums:
            if n<target:
                count_less+=1
            elif n==target:
                count_target+=1
        res = []
        while count_target>0:
            res.append(count_less)
            count_less+=1
            count_target-=1

        return res
        