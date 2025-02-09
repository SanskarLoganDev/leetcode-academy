# 169 MAJORITY ELEMENT

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

# Most Efficient Solution

# When count becomes 0:
# This signals that we have "used up" the confidence we had in the previous candidate.
# At this point, we choose the current element (num) as the new candidate.
# Why this works:
# The intuition is that if there is a majority element, it will eventually remain as the candidate because it appears more than 
# all other elements combined. It works on the principle mentioned in the question:
# "The majority element is the element that appears more than ⌊n / 2⌋ times"

def majorityElement(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        candidate = None
        for n in nums:
            if count == 0:
                candidate = n
            if n == candidate:
                count+=1
            else:
                count-=1
        return candidate


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
        hash[n] = 1 + hash.get(n, 0)   # This method checks if n already exists as a key in hash.
# If n is found, it returns its current count; if not, it returns 0. Basically working as a counter
        if hash[n] > majority:
            res = n
            majority = hash[n]
    
    return res

# Not that efficient solution but short
from collections import Counter
def majorityElement(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = Counter(nums)
        return c.most_common(1)[0][0]