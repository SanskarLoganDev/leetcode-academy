# 350. INTERSECTION OF TWO ARRAYS II

# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

def intersect(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        # iterating through the list with lesser elements
        if len(nums1)<len(nums2):
            for i in range(len(nums1)):
                if nums1[i] in nums2:
                    res.append(nums1[i])
                    nums2.remove(nums1[i])
        else:
            for i in range(len(nums2)):
                if nums2[i] in nums1:
                    res.append(nums2[i])
                    nums1.remove(nums2[i])
        return res
    
print(intersect( nums1 = [4,9,5], nums2 = [9,4,9,8,4]))

# Optimsed solution using Counter()

def intersect2(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        res = []
        count = Counter(nums1)
        for num in nums2:
            if count[num]>0:
                res.append(num)
                count[num]-=1
        return res
    
print(intersect2( nums1 = [4,9,5], nums2 = [9,4,9,8,4]))