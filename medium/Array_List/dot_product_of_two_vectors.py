# 1570. Dot Product of Two Sparse Vectors

# Given two sparse vectors, compute their dot product.

# Implement class SparseVector:

# SparseVector(nums) Initializes the object with the vector nums
# dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
# A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.

# Follow up: What if only one of the vectors is sparse?

 

# Example 1:

# Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
# Output: 8
# Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
# v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8
# Example 2:

# Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
# Output: 0
# Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
# v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0
# Example 3:

# Input: nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
# Output: 6
 

# Constraints:

# n == nums1.length == nums2.length
# 1 <= n <= 10^5
# 0 <= nums1[i], nums2[i] <= 100

from typing import List

class SparseVector:
    def __init__(self, nums: List[int]):
        self.vector = nums
        self.length = len(nums)
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        vec_sum = 0
        print(vec.vector)
        for i in range(self.length):
            vec_sum+=self.vector[i]*vec.vector[i]
        return vec_sum
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

# Follow-Up: Handling Only One Sparse Vector
# If only one of the vectors is sparse (the other is dense):

# Optimal Strategy:

# Iterate through the sparse vector and compute the dot product only for non-zero elements.

# Time Complexity:

# For a sparse vector of size m and a dense vector of size n, the dot product can be computed in O(m) time, where m is the number of non-zero elements in the sparse vector.

# Example Adjustment
# Here’s how you might adjust the dotProduct method to handle a scenario where only one vector is sparse (assuming self.vector is sparse):

# def dotProduct(self, vec: 'SparseVector') -> int:
#     vec_sum = 0
#     if self.vector is not None and vec.vector is not None:
#         for i in range(self.length):
#             if self.vector[i] != 0:
#                 vec_sum += self.vector[i] * vec.vector[i]
#     return vec_sum