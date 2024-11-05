# 283. MOVE ZEROS

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]

def moveZeroes(nums):
    count = nums.count(0)
    for i in range(count):
        nums.remove(0)
        nums.append(0)
    return nums
    
            
print(moveZeroes([0,1,0,3,12]))

# With better time complexity
def moveZeroes2(nums):
    i=0
    for num in nums:
        if num!=0:
            nums[i]=num
            i+=1
    while i<len(nums):
        nums[i]=0
        i+=1

    return nums
print(moveZeroes2([0,1,0,3,12]))