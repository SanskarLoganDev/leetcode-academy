# 219. Contains Duplicate II
# Neetcode 250

# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true

# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true

# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
 

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
# 0 <= k <= 105

from typing import List

# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map = {}
        for i in range(len(nums)):
            if nums[i] in hash_map:
                if abs(hash_map[nums[i]]-i)<=k:
                    return True
            hash_map[nums[i]] = i
        return False

# Sliding window approach
# Time complexity: O(N)
# Space complexity: O(K) or O(min(N, K)) as we delete the elements that go out of the window
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        k = min(len(nums), k)
        if k==0:
            return False
        hashmap = {}
        j = 0
        for i in range(len(nums)):
            if i-j>k:
                del hashmap[nums[j]]
                j+=1
            if nums[i] in hashmap:
                if abs(i - hashmap[nums[i]]) <= k:
                    return True
            hashmap[nums[i]] = i
        return False