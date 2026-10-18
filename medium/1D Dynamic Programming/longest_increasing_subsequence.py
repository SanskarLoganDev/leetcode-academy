# 300. Longest Increasing Subsequence
# Neetcode 150 (Important)

# Given an integer array nums, return the length of the longest strictly increasing subsequence.

# Example 1:

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

# Example 2:

# Input: nums = [0,1,0,3,2,3]
# Output: 4

# Example 3:

# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 2500
# -104 <= nums[i] <= 104
 
# Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?

# Brute force recursion
# time complexity: O(2^N)
# space complexity: O(N) of recursion call-stack/depth

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        max_count = 0
        n = len(nums)
        def solve(i, prev):
            if i>=n:
                return 0

            # take
            take = 0
            if nums[i]>prev:
                take = 1+solve(i+1, nums[i])
            # skip
            skip = solve(i+1, prev)
            return max(take, skip)
        return solve(0, float("-inf"))
                
# Using memoization we get memory time exceeded error for large test cases on leetcode because of large state space taken my memo dictionary. 
# Adding to python dictionary is expensive operation.
# time complexity O(N^2) and 
# space complexity O(N^2) for memoization and O(N) for recursion stack
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {} # (i, prev) -> int
        n = len(nums)

        def solve(i, prev): # here prev is the value of previous element in the subsequence
            if i>=n:
                return 0

            key = (i, prev)
            if key in memo:
                return memo[key]
            # take
            # here take = 0 does not stop/interfere with recursion; It just ensures that the invalid “take” option contributes nothing
            take = 0 # default value if we don't take current element
            if nums[i]>prev: # can only take if current number is greater than previous number in subsequence
                take = 1+solve(i+1, nums[i])
            # skip
            skip = solve(i+1, prev)
            memo[key] = max(take, skip)
            return memo[key]
        return solve(0, float("-inf"))
    
# Same memoization approach with index of previous element instead of value

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {} # (i_prev, prev) -> int
        n = len(nums)

        def solve(i, prev_i):
            if i>=n:
                return 0

            key = (i, prev_i) # prev_i is index of previous element in subsequence
            if key in memo:
                return memo[key]
            # take
            take = 0
            # new check of prev_i==-1
            if prev_i==-1 or nums[i]>nums[prev_i]: # if prev_i==-1 means no previous element taken yet
                take = 1+solve(i+1, i)
            # skip
            skip = solve(i+1, prev_i)
            memo[key] = max(take, skip)
            return memo[key]
        return solve(0, -1)
    
# Using bottom-up DP approach
# time complexity O(N^2) and space complexity O(N)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums) # dp[i] = length of longest increasing subsequence ending at index i
        # all values initialized to 1 because minimum length of increasing subsequence ending at any index is 1 (the element itself)

        for i in range(len(nums)):
            for j in range(i+1):
                if nums[i]<=nums[j]: # nums[i] must be greater than nums[j] to form increasing subsequence
                    continue
                
                new_sub_len = dp[j]+1 # length of increasing subsequence ending at i if we take nums[i] after nums[j]
                if dp[i]>=new_sub_len: # if current length is already greater than or equal to new_sub_len
                    continue
                dp[i] = new_sub_len # update dp[i] to new_sub_len
        return max(dp)
                
                
# Using patience sorting with binary search
# time complexity O(N log N) and 
# space complexity O(N)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        for i in range(len(nums)): # iterate through all numbers
            if not res: # if res is empty
                res.append(nums[i])
                continue
            # binary search for the index of the smallest number >= nums[i]
            l = 0
            r = len(res)-1
            idx = float("inf") # index of smallest number >= nums[i]

            while l<=r:
                mid = (l+r)//2
                if res[mid]>=nums[i]: # found a number >= nums[i]
                    idx = mid
                    r = mid-1
                else:
                    l = l+1
            if idx == float("inf"): # means no number in res is >= nums[i]
                res.append(nums[i]) # append nums[i] to the end
            else:
                res[idx] = nums[i] # replace the number at idx with nums[i]
        return len(res) # length of res is the length of longest increasing subsequence
                
# Summary of dry run:
# Entire process summarized
# nums[i]     res after processing nums[i]

# 10          [10]

# 9           [9]
#             replace 10 with 9

# 2           [2]
#             replace 9 with 2

# 5           [2, 5]
#             append

# 3           [2, 3]
#             replace 5 with 3

# 7           [2, 3, 7]
#             append

# 101         [2, 3, 7, 101]
#             append

# 18          [2, 3, 7, 18]
#             replace 101 with 18



# patience sorting using inbuilt bisect module for binary search

import bisect
# here bisect.bisect_left(res, x) returns the index of the first element in res which is >= x
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []  # res[k] = smallest possible tail of an LIS of length k+1
        for x in nums:
            idx = bisect.bisect_left(res, x)  # first position with res[idx] >= x
            if idx == len(res):
                res.append(x)
            else:
                res[idx] = x
        return len(res)

# detailed dry run for understanding:

# nums = [10, 9, 2, 5, 3, 7, 101, 18]
# res = []

# i=0, nums[i]=10
# res=[] -> append 10
# res=[10]
# Smallest ending value for subsequence length 1 is 10

# i=1, nums[i]=9
# res=[10], x=9
# Find leftmost index where res[index]>=9
# l=0, r=0, idx=inf
# mid=0, res[0]=10 >= 9 -> idx=0, r=-1
# Search ends -> replace res[0]=9
# res=[9]
# 9 is better than 10 because it is a smaller ending value for a length-1 subsequence

# i=2, nums[i]=2
# res=[9], x=2
# l=0, r=0, idx=inf
# mid=0, res[0]=9 >= 2 -> idx=0, r=-1
# Search ends -> replace res[0]=2
# res=[2]
# 2 is a better ending value than 9 for a length-1 subsequence

# i=3, nums[i]=5
# res=[2], x=5
# l=0, r=0, idx=inf
# mid=0, res[0]=2 < 5 -> l=1
# Search ends, idx=inf -> no value >=5
# append 5
# res=[2,5]
# LIS length increases to 2: 2 -> 5

# i=4, nums[i]=3
# res=[2,5], x=3
# Find leftmost value >=3
# l=0, r=1, idx=inf
# mid=0, res[0]=2 < 3 -> l=1
# mid=1, res[1]=5 >= 3 -> idx=1, r=0
# Search ends -> replace res[1]=3
# res=[2,3]
# LIS length is still 2, but 2->3 is better than 2->5 because 3 is a smaller ending value
# Example: if 4 appears later, 2->3->4 works but 2->5->4 does not

# i=5, nums[i]=7
# res=[2,3], x=7
# l=0, r=1, idx=inf
# mid=0, res[0]=2 < 7 -> l=1
# mid=1, res[1]=3 < 7 -> l=2
# Search ends, idx=inf -> append 7
# res=[2,3,7]
# LIS length increases to 3: 2 -> 3 -> 7

# i=6, nums[i]=101
# res=[2,3,7], x=101
# l=0, r=2, idx=inf
# mid=1, res[1]=3 < 101 -> l=2
# mid=2, res[2]=7 < 101 -> l=3
# Search ends, idx=inf -> append 101
# res=[2,3,7,101]
# LIS length increases to 4: 2 -> 3 -> 7 -> 101

# i=7, nums[i]=18
# res=[2,3,7,101], x=18
# Find leftmost value >=18
# l=0, r=3, idx=inf
# mid=1, res[1]=3 < 18 -> l=2
# mid=2, res[2]=7 < 18 -> l=3
# mid=3, res[3]=101 >= 18 -> idx=3, r=2
# Search ends -> replace res[3]=18
# res=[2,3,7,18]
# LIS length is still 4, but 18 is a better ending value than 101
# Example: if 20 appears later, 2->3->7->18->20 works, but 2->3->7->101->20 does not

# Summary:
# 10  -> [10]          append
# 9   -> [9]           replace 10
# 2   -> [2]           replace 9
# 5   -> [2,5]         append
# 3   -> [2,3]         replace 5
# 7   -> [2,3,7]       append
# 101 -> [2,3,7,101]   append
# 18  -> [2,3,7,18]    replace 101

# Final:
# res=[2,3,7,18]
# len(res)=4