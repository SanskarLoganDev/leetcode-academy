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

def containsNearbyDuplicate(nums, k):
    s1= []
    i=1
    j=0
    while i< len(nums):
        if nums[i]==nums[j]:
            print(i,j)
            if abs(i - j) <= k:
                return True
            j=i
            print("j: ",j)
        i+=1
        print("i: ",i)

    return False

print(containsNearbyDuplicate([1,2,3,1,2,3], 2))
    