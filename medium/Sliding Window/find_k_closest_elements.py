# 658. Find K Closest Elements
# Neetcode 250

# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

# An integer a is closer to x than an integer b if:

# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b
 

# Example 1:

# Input: arr = [1,2,3,4,5], k = 4, x = 3

# Output: [1,2,3,4]

# Example 2:

# Input: arr = [1,1,2,3,4,5], k = 4, x = -1

# Output: [1,1,2,3]

# Constraints:

# 1 <= k <= arr.length
# 1 <= arr.length <= 104
# arr is sorted in ascending order.
# -104 <= arr[i], x <= 104

from typing import List

# Time complexity: O(NlogN)
# Space complexity: O(N)
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        if x<=arr[0]:
            return arr[:k]
        if x>=arr[-1]:
            return arr[n-k:]
        res = []
        diff = [] # storing all differences along with value
        for i in range(n):
            diff.append((abs(arr[i] - x), arr[i]))
        diff.sort() # sorts lexicographically and automatocally handles condition: |a - x| == |b - x| and a < b
        for i in range(k):
            res.append(diff[i][1])
        res.sort()
        return res
    
    
# Optimized using 2 pointers
# time complexity: O(N)
# Space complexity: O(1) ignoring the result slice

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        if x<=arr[0]:
            return arr[:k]
        if x>=arr[-1]:
            return arr[n-k:]
        l = 0
        r = n-1
        while r-l+1>k: # just for the window, not adding to result
            left_val = abs(arr[l]-x)
            right_val = abs(arr[r]-x)
            if left_val<=right_val:
                r-=1
            else:
                l+=1
        
        return arr[l:r+1]
    
# Slightly more optimized solution using binary search
# Time complexity: O(log(n−k)+k)
# Space complexity: O(1)
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        l = 0
        r = n-k # here r is the maximum value the left boundary of the window, can have
        while l<r: # O(log(n-k))
            m = (l+r)//2
            if x - arr[m] > arr[m+k] - x:
                l = m+1
            else:
                r = m
        return arr[l:l+k] # O(k) for inserting the elements in the new array
      
# Explanation with examples
# The two values being compared are:

# arr[mid]          arr[mid + k]
#    ↑                   ↑
# left candidate     right candidate

# These are the two elements competing for the boundary of a k-sized window.

# The core question is:

# Between arr[mid] and arr[mid+k], which one is farther from x?

# If arr[mid] is worse, shift the window right. Otherwise, keep the left side.

# Case 1: x is to the LEFT of both

# Picture:

# x -------- arr[mid] ---------------- arr[mid+k]

# Example:

# arr = [10,20,30,40,50]
# k = 2
# x = 5

# mid = 1

# arr[mid]   = 20
# arr[mid+k] = 40

# Now calculate:

# x - arr[mid]
# = 5 - 20
# = -15

# arr[mid+k] - x
# = 40 - 5
# = 35

# Comparison:

# -15 > 35   ❌

# So:

# right = mid

# We search toward the left.

# And this makes sense intuitively: if x=5 is way over here:

# x=5    10    20    30    40    50

# then smaller numbers are obviously closer.

# So the best window should be farther left.

# Case 2: x is BETWEEN the two values, but closer to arr[mid]

# Picture:

# arr[mid] ---- x -------------------- arr[mid+k]

# Example:

# arr[mid]   = 3
# x          = 4
# arr[mid+k] = 8

# Distances:

# x - arr[mid]
# = 4 - 3
# = 1

# arr[mid+k] - x
# = 8 - 4
# = 4

# So:

# 1 > 4   ❌

# Again:

# right = mid

# Meaning:

# arr[mid] is closer, so don't discard the left side.

# Visual:

# 3 -- 4 ---------------- 8
# ↑    ↑                  ↑
# mid  x                mid+k

# distance = 1         distance = 4

# Clearly 3 is preferable to 8.

# So move/search left.

# Case 3: x is BETWEEN them, but closer to arr[mid+k]

# Picture:

# arr[mid] ---------------- x --- arr[mid+k]

# Example:

# arr[mid]   = 2
# x          = 8
# arr[mid+k] = 9

# Distances:

# x - arr[mid]
# = 8 - 2
# = 6

# arr[mid+k] - x
# = 9 - 8
# = 1

# Comparison:

# 6 > 1 ✅

# Therefore:

# left = mid + 1

# Why?

# Because arr[mid] = 2 is much farther from 8 than 9 is.

# 2 ---------------- 8 -- 9
# ↑                  ↑    ↑
# mid                x  mid+k

# distance 6             distance 1

# So we don't want a window starting as far left as mid.

# Shift right.

# Case 4: x is to the RIGHT of both

# Picture:

# arr[mid] ---------------- arr[mid+k] ---- x

# Example:

# arr[mid]   = 10
# arr[mid+k] = 30
# x          = 50

# Now:

# x - arr[mid]
# = 50 - 10
# = 40

# arr[mid+k] - x
# = 30 - 50
# = -20

# Comparison:

# 40 > -20 ✅

# So:

# left = mid + 1

# Search toward the right.

# That also makes intuitive sense:

# 10    20    30    40    50
#                         ↑
#                         x

# The values toward the right are closer to x.