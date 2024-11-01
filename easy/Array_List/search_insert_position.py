# 35. Search Insert Position

# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4

# O(n) time complexity

def searchInsert(nums, target):
    if target in nums:
        return nums.index(target)
    elif target<nums[0]:
        return 0
    elif target>nums[len(nums)-1]:
        return len(nums)
    else:
        for i in range(len(nums)-1):
            if target > nums[i] and target < nums[i+1]:
                return i+1
            
print(searchInsert([1,3,5,6,7,8,11],4))

# O(log n) time complexity using Binary Search algorithm (but in leetcode this is shown having more space complextiy)

def searchInsert_binarySearch(nums, target):
    left = 0
    right = len(nums)-1
    while left<=right:
        mid = (left+right)//2
        if nums[mid]==target:
            return mid
        if nums[mid] > target:
            right = mid-1
        else:
            left = mid+1
        
    return left # In all other scenarios we are returning the left element

