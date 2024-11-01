# 169 MAJORITY ELEMENT

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

# My solu

def majorityElement(nums):
    unique = []
    max = 0
    max_num = nums[0]
    for i in range(len(nums)):
        if nums[i] in unique:
            continue
        unique.append(nums[i])
        if nums.count(nums[i])> max:
            max =nums.count(nums[i])
            max_num = nums[i]
    
    return max_num

print(majorityElement([2,2,1,1,1,2,2]))

# Optimised solu using Hash Map (dictionary)

def majorityElement2(nums):
    dict1 = {}
    maj = 0
    maj_num=nums[0]
    for i in range(len(nums)):
        if nums[i] not in dict1:
            dict1[nums[i]]=nums.count(nums[i])
            if nums.count(nums[i]) > maj:
                maj = nums.count(nums[i])
                maj_num = nums[i]
    return maj_num
    
print(majorityElement2([2,2,1,1,1,2,2]))

# Another way

def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    hash = {}
    res = majority = 0
    
    for n in nums:
        hash[n] = 1 + hash.get(n, 0)
        if hash[n] > majority:
            res = n
            majority = hash[n]
    
    return res