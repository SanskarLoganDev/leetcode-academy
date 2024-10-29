# 136) SINGLE NUMBER

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 

# Example 1:

# Input: nums = [2,2,1]
# Output: 1
# Example 2:

# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:

# Input: nums = [1]
# Output: 1

# my solution

def singleNumber(nums):
    repeat = []
    for i in range(len(nums)):
        if nums[i] in repeat:
            repeat.remove(nums[i])
            continue
        repeat.append(nums[i])
        
    return repeat[0]

print(singleNumber([2,2,1]))

# More optimised solution

def singleNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result ^= num # ^ is a symbol for xor
        return result
    
# The XOR operation has two useful properties:

# ( x XOR x = 0 ): XORing a number with itself results in 0.
# ( x XOR 0 = x ): XORing a number with 0 keeps the number unchanged.
# By XORing all elements in the array, the elements that appear twice will cancel each other out (since ( x XOR x = 0 )), 
# leaving only the single element that appears once.