# 349. INTERSECTION OF 2 ARRAYS

# Given two integer arrays nums1 and nums2, return an array of their 
# intersection
# . Each element in the result must be unique and you may return the result in any order.

 

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.
 
def intersection(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        if len(nums1)<len(nums2):
            for i in range(len(nums1)):
                if nums1[i] in nums2 and nums1[i] not in res:
                    res.append(nums1[i])
        else:
            for i in range(len(nums2)):
                if nums2[i] in nums1 and nums2[i] not in res:
                    res.append(nums2[i])
        return res
    
print(intersection(nums1 = [1,2,2,1], nums2 = [2,2]))

# Using sets
def intersection2(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    return list(set1.intersection(set2))

print(intersection2(nums1 = [1,2,2,1], nums2 = [2,2]))
