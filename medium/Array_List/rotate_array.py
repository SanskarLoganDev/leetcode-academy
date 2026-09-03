# 189. Rotate Array
# Neetcode 250

# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
 

# Constraints:

# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105
 

# Follow up:

# Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
# Could you do it in-place with O(1) extra space?

# time complexity: O(N)
# space complexity: O(N)
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 
        n = len(nums)
        if k>n:
            k = k%n
        temp = nums[n-k:] + nums[:n-k]
        nums[:] = temp
        
# time complexity: O(N)
# space complexity: O(1)

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 
        n = len(nums)
        if k>len(nums):
            k = k%n
        # reverse 3 times
        def reverse(arr, start, end): # to avoid extra space
            l = start
            r = end # length of array - 1
            while l<r:
                arr[l], arr[r] = arr[r], arr[l]
                l+=1
                r-=1
            return arr

        reverse(nums, 0, n-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, n-1)
        
        