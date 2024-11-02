# 448. FIND ALL NUMBERS DISAPPEARED IN AN ARRAY

# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.


# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:

# Input: nums = [1,1]
# Output: [2]

# Takes too long to solve when lenth of array is too long: Time Complexity: 𝑂(𝑛^2), Reason: Iterates through n elements. 
# Each membership check i+1 not in nums is o(n) because checking for membership in a list requires scanning the list from start to end in the worst case.

def findDisappearedNumbers(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        res=[]
        for i in range(len(nums)):
            if (i+1) not in nums:
                res.append(i+1)
        return res
    
print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))

# Using Hash set and list comprehension

def findDisappearedNumbers2(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = set(nums) # In Python, adding an element to a set is an average O(1) operation due to its hash table implementation.
        return [i+1 for i in range(len(nums)) if i+1 not in s] # Iterates through n elements. Each membership check i+1 not in s is O(1) due to the set's hash table.
    
print(findDisappearedNumbers2([4,3,2,7,8,2,3,1]))