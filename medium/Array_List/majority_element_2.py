# 229. Majority Element II

# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

# Example 1:

# Input: nums = [3,2,3]
# Output: [3]

# Example 2:

# Input: nums = [1]
# Output: [1]

# Example 3:

# Input: nums = [1,2]
# Output: [1,2]
 

# Constraints:

# 1 <= nums.length <= 5 * 104
# -109 <= nums[i] <= 109
 

# Follow up: Could you solve the problem in linear time and in O(1) space?

from typing import List

# time complexity: O(nlogn), space: O(N) but if we exclude the result array: O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = set()
        cand = nums[0]
        count = 0
        for n in nums:
            if n == cand:
                count+=1
            else:
                cand = n
                count = 1
            if count > len(nums)//3 and n not in res:
                    res.add(n)
        return list(res)
    
# Boyer-Moore majority vote algorithm
# Time complexity: O(N), space complexity: O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # at max there can be 2 majority elements having elemnts more than floor(n/3)
        count1 = 0
        count2 = 0
        cand1 = None
        cand2 = None

        # Assumption

        for n in nums:
            # do not put the count == 0 check first as it may result in assigning the most frequent element to the other cand
            if n == cand1: # if the element is same as candidate 1
                count1+=1
            elif n == cand2: # if the element is same as candidate 2
                count2+=1
            elif count1==0: # if the element does not match either but count1 is 0
                cand1 = n
                count1 = 1 # resetting the value as the count needs to include current value when switching majority element candidate
            elif count2==0: # if the element does not match either but count2 is 0 but count1 is not 0
                cand2 = n
                count2 = 1
            else:           # # if the element does not match either but neither count is 0
                count1-=1
                count2-=1

        # Verification
        res = []
        freq1 = 0 # frequency counter for both the assumed majority elements
        freq2 = 0
        for n in nums:
            if n==cand1:
                freq1+=1
            if n==cand2:
                freq2+=1
        if freq1 > len(nums)//3:
            res.append(cand1)
        if freq2 > len(nums)//3:
            res.append(cand2)

        return res

    