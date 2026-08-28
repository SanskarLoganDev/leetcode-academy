# 41. First Missing Positive
# Neetcode 250

# Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

# Example 1:

# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.
# Example 2:

# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.
# Example 3:

# Input: nums = [7,8,9,11,12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.
 

# Constraints:

# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1

from typing import List

# time complexity: O(N)
# space complexity: O(N)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        n = 1
        while True:
            if n not in set_nums:
                return n
            n+=1
            
# Same time and space
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        boolean = [False]*(n+1) # using nums as index to track if a number has occurred between [1, n]
        for i in range(n):
            if nums[i]<=0 or nums[i]>n: # out of required bound
                continue
            boolean[nums[i]] = True
        
        for i in range(1, len(boolean)): # checking which number has not occurred in nums
            if not boolean[i]:
                return i
        return n+1 # if all numbers in nums have occurred return the next number

# Optimised Solution

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        contains1 = False
        
        # Step 1: Check if 1 exists.
        # If 1 is missing, it is automatically the first missing positive.
        for num in nums:
            if num==1:
                contains1 = True
        if not contains1:
            return 1
        
        # Step 2: We only care about numbers in [1, n].
        # The answer can only be between 1 and n+1.
        # Replace negatives, 0s, and values > n with 1.
        # This is safe because we already know 1 exists.
        for i in range(n):
            if nums[i]<=0 or nums[i]>n:
                nums[i]=1
        
        # Step 3: Use indices as a presence map. SINCE NOW EVERY NUMBER IS IN BOUNDS OF [1,n] USE THE ALGO FOR IT
        # Number x maps to index x-1.
        # If x exists, make nums[x-1] negative.
        for i in range(n):
            num = abs(nums[i]) # abs because nums[i] may already be marked negative
            idx = num-1
            
            if nums[idx]<0: # Already marked => this number was already encountered
                continue
            nums[idx] = -nums[idx]

        # Step 4: First positive index means that number was never encountered.
        # index 0 -> number 1
        # index 1 -> number 2
        # ...
        for i in range(n):
            if nums[i]>0:
                return i+1
        return n+1

# Dry run

# Input:

# nums = [3, 4, -1, -2, 1, 5, 16, 0, 2, 0]
# n = 10

# We only care whether 1...10 exist.

# Step 1: Check for 1

# 1 exists, so continue.

# Step 2: Replace invalid values with 1

# Invalid means:

# <= 0 or > 10

# So:

# -1  -> 1
# -2  -> 1
# 16  -> 1
# 0   -> 1
# 0   -> 1

# Array becomes:

# [3, 4, 1, 1, 1, 5, 1, 1, 2, 1]

# Now every value is safely within [1,10].

# Step 3: Mark which numbers exist

# Remember:

# number x -> index x-1

# So:

# 1 -> index 0
# 2 -> index 1
# 3 -> index 2
# 4 -> index 3
# 5 -> index 4
# ...
# i = 0
# nums[0] = 3
# num = 3
# idx = 2

# Mark index 2 negative:

# [3, 4, -1, 1, 1, 5, 1, 1, 2, 1]

# Meaning:

# 3 exists
# i = 1
# nums[1] = 4
# idx = 3

# Mark index 3:

# [3, 4, -1, -1, 1, 5, 1, 1, 2, 1]

# Meaning:

# 4 exists
# i = 2
# nums[2] = -1
# num = abs(-1) = 1
# idx = 0

# Mark index 0:

# [-3, 4, -1, -1, 1, 5, 1, 1, 2, 1]

# Meaning:

# 1 exists

# This is why abs() is necessary. The -1 does not mean the original number was negative anymore; the negative sign is now just our marker.

# i = 3
# nums[3] = -1
# num = 1
# idx = 0

# But:

# nums[0] = -3

# already negative.

# So 1 was already marked. Do nothing.

# i = 4
# nums[4] = 1
# idx = 0

# Already negative → skip.

# i = 5
# nums[5] = 5
# idx = 4

# Mark index 4:

# [-3, 4, -1, -1, -1, 5, 1, 1, 2, 1]

# Meaning:

# 5 exists
# i = 6
# nums[6] = 1
# idx = 0

# Already marked → skip.

# i = 7

# Again 1 → already marked → skip.

# i = 8
# nums[8] = 2
# idx = 1

# Mark index 1:

# [-3, -4, -1, -1, -1, 5, 1, 1, 2, 1]

# Meaning:

# 2 exists
# i = 9

# 1 → already marked.

# Final marked array:

# [-3, -4, -1, -1, -1, 5, 1, 1, 2, 1]
# Step 4: Find first positive index

# Interpret each index:

# index 0 negative -> 1 exists
# index 1 negative -> 2 exists
# index 2 negative -> 3 exists
# index 3 negative -> 4 exists
# index 4 negative -> 5 exists
# index 5 positive -> 6 DOES NOT exist

# Therefore:

# return 5 + 1
#        = 6

# ✅ Answer = 6

# Complexity

# There are three separate O(n) passes:

# O(n) + O(n) + O(n) = O(n)

# and the array itself is reused as the presence map:

# Time: O(n)
# Auxiliary space: O(1)

# The core trick to remember is:

# For values 1...n, use index value - 1 as their presence marker, and make that position negative when the value exists.