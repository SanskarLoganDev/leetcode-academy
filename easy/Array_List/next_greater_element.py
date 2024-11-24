# 496. NEXT GREATER ELEMENT I

# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

 

# Example 1:

# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
# - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
# - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
# Example 2:

# Input: nums1 = [2,4], nums2 = [1,2,3,4]
# Output: [3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
# - 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.

def nextGreaterElement(nums1, nums2):
    res = []
    for i in range(len(nums1)):
        j = nums2.index(nums1[i])
        if j==len(nums2)-1:
            res.append(-1)
            continue
        j+=1
        max = nums1[i]
        while j<len(nums2):
            if nums2[j]>max:
                max = nums2[j]
                res.append(max)
                break
            j+=1
        if max == nums1[i]:
            res.append(-1)
    return res

print(nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))

# The following solution uses Monotonic Stack Approach
from typing import List

def nextGreaterElement2(nums1: List[int], nums2: List[int]) -> List[int]:
    hm = {}
    st = []

    # Fill the hashmap with next greater elements for nums2
    for num in reversed(nums2):
        while st and st[-1] < num:
            st.pop()
        hm[num] = st[-1] if st else -1
        st.append(num)

    # Generate the result for nums1 based on the hashmap
    return [hm[num] for num in nums1]

print(nextGreaterElement2(nums1 = [4,1,2], nums2 = [1,3,4,2]))

            
            