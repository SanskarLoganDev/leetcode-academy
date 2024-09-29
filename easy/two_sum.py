# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

# def two_sum(nos, target):
#     length = len(nos)
#     for i in range(length):
#         for j in range(i+1,length):
#             if nos[i]+nos[j]==target:
#                 return [i,j] # we could simply return in this way instead of adding another list and appending to it
#     return "No Match"           
        
# print(two_sum([3,3],6))

# Optimised (O(n))

# def two_sum_opt(nums, target):
#     inverse_dict = {}
#     for i in range(len(nums)):
#         complement = target - nums[i]
#         if complement in inverse_dict:
#             return [inverse_dict[complement],i]
#         inverse_dict[nums[i]] = i
        
#     return "No Match"           
        
# print(two_sum_opt([2, 7, 11, 15],9))

# Optimised (O(n)) my solu

def two_sum_opt(nums, target):
    inverse_list = []
    for i in range(len(nums)):
        complement = target - nums[i]
        if nums[i] in inverse_list:
            return [inverse_list.index(nums[i]),i]
        inverse_list.append(complement)
        
    return "No Match"           
        
print(two_sum_opt([3,4,5,7,9],11))
