# 152. Maximum Product Subarray
# Neetcode 150 (Important)

# Given an integer array nums, find a subarray that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

# Note that the product of an array with a single element is the value of that element.

# Example 1:
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# Example 2:
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

# Constraints:

# 1 <= nums.length <= 2 * 104
# -10 <= nums[i] <= 10
# The product of any subarray of nums is guaranteed to fit in a 32-bit integer.

from typing import List
# Brute force solution 
# time complexity O(N^3) and space complexity O(N)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxx = float("-inf")
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                subarray = nums[i:j+1]
                mult = 1
                for num in subarray:
                    mult*=num
                maxx = max(maxx, mult)
        return maxx
    
# Optimized Bruteforce solution
# time complexity O(N^2) and space complexity O(1)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxx = float("-inf")
        for i in range(len(nums)):
            mult = 1
            for j in range(i, len(nums)):
                mult*=nums[j]
                maxx = max(maxx, mult)
        return maxx
    
# Optimized solution using Dynamic Programming
# time complexity O(N) and space complexity O(1)

# Logic:
# Why this works (deep intuition, not “usual DP table”)
# The catch: negatives flip everything
# For sum problems (Kadane’s), you only track the best “ending here” sum.
# For product, negatives break that because:
# A negative number can turn a large positive into a large negative.
# More importantly: a negative number can turn a large negative into a large positive.
# Example:
# If you had curMin = -100 and current x = -2
# x * curMin = 200 becomes huge (best candidate!)
# So, at every index, the best product subarray ending here might come from:
# previous best (curMax)
# previous worst (curMin)
# or starting fresh at this index
# That’s why we track two states.

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # res stores the best (maximum) product seen so far.
        # Initialize with max(nums) to correctly handle cases like all negatives
        # or a single element array.
        res = max(nums)

        # curMax = maximum product of a subarray that MUST end at current index
        # curMin = minimum product of a subarray that MUST end at current index
        #
        # We track curMin because multiplying by a negative can turn a small
        # (very negative) product into a very large positive product.
        curMin, curMax = 1, 1

        for n in nums:
            # If x == 0:
            # Any subarray ending here has product 0, and any subarray continuing
            # past 0 would have product 0 if it includes it.
            # So we "reset" the running products and start fresh after the 0.
            if n == 0:
                curMin, curMax = 1, 1
                # res might already be 0 if max(nums) was 0 or if res updated earlier.
                # We can also do res = max(res, 0), but res=max(nums) already covers it.
                continue

            # IMPORTANT:
            # curMax gets updated using the old values of curMax and curMin.
            # So store old curMax before modifying it.
            tmp = curMax * n

            # The max product subarray ending at this index is one of:
            # 1) extend previous max-product subarray: n * old_curMax
            # 2) extend previous min-product subarray: n * old_curMin (if n is negative)
            # 3) start new subarray at this element alone: n
            curMax = max(tmp, n * curMin, n)

            # The min product subarray ending at this index is similarly:
            # 1) n * old_curMax (stored in tmp)
            # 2) n * old_curMin
            # 3) start new: n
            curMin = min(tmp, n * curMin, n)

            # Update global answer using best subarray ending here
            res = max(res, curMax)

        return res

# Detailed dry run: nums = [2, 3, -2, 4]

# Expected answer: 6 (subarray [2,3])

# Initialize:

# res = max(nums) = 4

# curMax = 1, curMin = 1

# 1) x = 2

# tmp = curMax * x = 1 * 2 = 2

# curMax = max(tmp=2, xcurMin=21=2, x=2) = 2

# curMin = min(tmp=2, x*curMin=2, x=2) = 2

# res = max(4, 2) = 4

# State: curMax=2, curMin=2, res=4

# 2) x = 3

# tmp = curMax * x = 2 * 3 = 6

# curMax = max(6, 3curMin=32=6, 3) = 6

# curMin = min(6, 6, 3) = 3

# res = max(4, 6) = 6

# State: curMax=6, curMin=3, res=6

# 3) x = -2

# tmp = curMax * x = 6 * (-2) = -12

# curMax = max(tmp=-12, xcurMin=-23=-6, x=-2) = -2

# best ending here is actually just -2 alone (starting fresh)

# curMin = min(tmp=-12, x*curMin=-6, x=-2) = -12

# res = max(6, -2) = 6

# State: curMax=-2, curMin=-12, res=6

# 4) x = 4

# tmp = curMax * x = -2 * 4 = -8

# curMax = max(tmp=-8, xcurMin=4(-12)=-48, x=4) = 4

# curMin = min(tmp=-8, -48, 4) = -48

# res = max(6, 4) = 6

# Final: res = 6