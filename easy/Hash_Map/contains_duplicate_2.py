# 219. Contains Duplicate 2

# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that 
# nums[i] == nums[j] and abs(i - j) <= k.

 

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true

# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true

# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false

# Example 4:

# Input: nums = [1,4,2,3,1,2], k = 3
# Output: true

# Example 5:

# Input: nums = [0,1,2,3,4,0,0,7,8,9,10,11,12,0], k = 1
# Output: true

# My first solution

# def containsNearbyDuplicate(nums, k):
#         s1= {}
#         for i in range(len(nums)):
#             if nums[i] not in s1:
#                 s1[nums[i]] = [i]
#             elif nums[i] in s1:
#                 s1[nums[i]].append(i)
#         for num in s1.values():
#             if len(num)==2:
#                 if (num[-1] - num[-2])<=k:
#                     return True
#             elif len(num)>=3:
#                 for i in range(len(num)-1):
#                     diff = num[i+1]-num[i]
#                     if diff<=k:
#                         return True
#         return False

# print(containsNearbyDuplicate([0,1,2,3,4,0,0,7,8,9,10,11,12,0], 1))

# Optimised solution: just replace the index with the current index in dict instead of storing it as a list in dict

def containsNearbyDuplicate(nums, k):
    if len(nums)-len(set(nums))==0: # if there are no duplicates return False
        return False
    s1 = {}
    for i in range(len(nums)):
        if nums[i] in s1 and (i-s1[nums[i]])<=k:
            return True
        s1[nums[i]] = i
    return False

print(containsNearbyDuplicate([1,4,2,3,1,2], 3))

# Optimised solution without using hash map -> Best space complexity, worst time complexity

def containsNearbyDuplicate2(nums, k):
    for i in range(len(nums)):
        if nums[i] in nums[i+1:i+k+1]:
            return True
    return False

print(containsNearbyDuplicate2([1,4,2,3,1,2], 3))