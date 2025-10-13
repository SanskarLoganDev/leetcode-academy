# 268. Missing Number
# Neetcode 150 (Important)

# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Example 1:

# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
# Example 2:

# Input: nums = [0,1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
# Example 3:

# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

# time complexity: O(nlogn)
# space complexity: O(1)
def missingNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(len(nums)):
            if i!=nums[i]:
                return i
        return nums[-1]+1
print(missingNumber([9,6,4,2,3,5,7,0,1])) 


# time complexity: O(n)
# space complexity: O(1)    
def missingNumber2(nums):
    return sum(range(len(nums)+1)) - sum(nums)
print(missingNumber2([9,6,4,2,3,5,7,0,1]))