# 3318. Find X-Sum of All K-Long Subarrays I  (Leetcode medium Important)

# You are given an array nums of n integers and two integers k and x.

# The x-sum of an array is calculated by the following procedure:

# Count the occurrences of all elements in the array.
# Keep only the occurrences of the top x most frequent elements. If two elements have the same number of occurrences, the element with the bigger value is considered more frequent.
# Calculate the sum of the resulting array.
# Note that if an array has less than x distinct elements, its x-sum is the sum of the array. (not explicitly mentioned but this case of for the sub-array windows that are created with the length k and not for the entire array)

# Return an integer array answer of length n - k + 1 where answer[i] is the x-sum of the subarray nums[i..i + k - 1].

 

# Example 1:

# Input: nums = [1,1,2,2,3,4,2,3], k = 6, x = 2

# Output: [6,10,12]

# Explanation:

# For subarray [1, 1, 2, 2, 3, 4], only elements 1 and 2 will be kept in the resulting array. Hence, answer[0] = 1 + 1 + 2 + 2.
# For subarray [1, 2, 2, 3, 4, 2], only elements 2 and 4 will be kept in the resulting array. Hence, answer[1] = 2 + 2 + 2 + 4. Note that 4 is kept in the array since it is bigger than 3 and 1 which occur the same number of times.
# For subarray [2, 2, 3, 4, 2, 3], only elements 2 and 3 are kept in the resulting array. Hence, answer[2] = 2 + 2 + 2 + 3 + 3.
# Example 2:

# Input: nums = [3,8,7,8,7,5], k = 2, x = 2

# Output: [11,15,15,15,12]

# Explanation:

# Since k == x, answer[i] is equal to the sum of the subarray nums[i..i + k - 1].

from typing import List
from collections import Counter

# time complexity O (N*K*log(K))

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        i=0
        j=k-1
        res = []
        
        while j<len(nums):
            window = nums[i:j+1]
            count = Counter(window)
            # Sort the keys (unique elements) in descending order by (frequency, digit)
            # For equal frequencies, a larger digit is considered “more frequent.”
            # Sort the keys in descending order based on a tuple (frequency, digit).
            # Since tuples are compared lexicographically, for two digits with the same count, the one with the higher numeric value appears earlier.
            sorted_digits = sorted(count, key = lambda digit: (count[digit], digit), reverse = True)
            summer = 0
            d=0
            s1 = set(sorted_digits)
            if len(s1)<x: # (not explicitly mentioned but this case of for the sub-array windows that are created with the length k and not for the entire array)
                summer = sum(window)
            else:
                while d<x and d<len(sorted_digits):
                    summer+=sorted_digits[d]*count[sorted_digits[d]]
                    d+=1
            res.append(summer)
            i+=1
            j+=1
        return res