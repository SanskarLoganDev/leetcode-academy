# 26. Remove Dupliates from an array
# Neetcode 250

# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length
# int k = removeDuplicates(nums); // Calls your implementation
# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

# Example 1:

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).


# Time complexity: O(N^2)
# Space complexity: O(N)
# The for loop controls i independently, so modifying it within the loop doesn't impact the loop's progression.
# This is how I did it in first go:
def removeDuplicates(nums):
    if not nums:
        return 0
    res = []
    length = len(nums)
    for i in range(length): # O(N)
        if nums[i] in res: # O(N)
            continue
        else: 
            res.append(nums[i])
    for i in range(len(res)):
        nums[i]=res[i] # because it does not matter what is after the sorted unique elements
        
    return len(res)

print(removeDuplicates([1,1,2,2,3,3,3,4,4,4]))

from typing import List

# time complexity: O(nlogn)
# space complexity: O(n) for the set
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = list(set(nums)) # set does not guarantee order
        nums.sort()
        return len(nums)

# This is how it should be done using 2 pointers (more efficient)
# Time complexity: O(n)
# space complexity: O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        for i in range(1, len(nums)): # i starts from 1 and k starts from 0
            if nums[i] != nums[k]: # k only moves forward when repition ends or there is a unique element
                k += 1
                nums[k] = nums[i]
        
        return k + 1  # we return k+1 because k starts from 0 and we have to return number of unique elements