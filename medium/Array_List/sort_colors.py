# 75. Sort Colors

# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

 

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]
 

# Constraints:

# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.
 

# Follow up: Could you come up with a one-pass algorithm using only constant extra space?

# time complexity: O(n)
# space complexity: O(1) since the hashmap will have at most 3 keys

from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Counting sort
        mn = min(nums)
        mx = max(nums)
        mp = {}
        for n in nums:
            mp[n] = mp.get(n, 0)+1 
        i = 0
        for num in range(mn, mx+1):
            if num in mp:
                while mp[num]>0:
                    nums[i] = num
                    mp[num]-=1
                    i+=1
        return nums
    
# time complexity: O(n)
# space complexity: O(1) since we are using only 3 pointers    
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0 # monitors 0 
        j = 0 # monitors 1
        k = len(nums)-1 # monitors 2
        while j<=k: # we will be essentially moving j forward and swap with i and k when we encounter 0 and 2 respectively
            if nums[j]==1: # j is the pointer for 1 so we can just move forward
                j+=1
            elif nums[j]==2: # 2 is in the end, swap with k and move k backward
                nums[j], nums[k] = nums[k], nums[j] 
                k-=1
            else: # nums[j]==0
                nums[j], nums[i] = nums[i], nums[j]
                i+=1 # we forward i and j both because we know that the swapped value at j is 1 and we can just move forward
                j+=1
