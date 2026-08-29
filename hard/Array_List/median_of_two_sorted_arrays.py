# 4. Median of Two Sorted Arrays 
# (Neetcode 150) Important

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

# Constraints:

# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106


from typing import List

# Time complexity: O((n+m)log(n+m)), space complexity: O(n+m)
class Solution(object):
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)==0 and len(nums2) == 0:
            return 0
        nums = nums1 + nums2
        nums.sort()
        l = len(nums)
        if l%2==1:
            return float(nums[l//2])
        else:
            return (nums[l//2]+nums[(l//2)-1])/2
       
# Time complexity: O(n+m), space complexity: O(n+m)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i=j=0
        nums = []
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                nums.append(nums1[i])
                i+=1
            else:
                nums.append(nums2[j])
                j+=1
        if i<len(nums1):
            nums = nums+nums1[i:len(nums1)]
        if j<len(nums2):
            nums = nums+nums2[j:len(nums2)]
        n = len(nums)
        if n%2==0:
            return (nums[(n//2)-1]+nums[n//2])/2
        else:
            return nums[n//2]
        
# Time complexity: O(n+m), space complexity: O(1)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # essentially, in this solution we pre-calulate the index we need and then compare the elements in both the arrays
        # we parallely keep count of the index of the combine sorted array
        m = len(nums1)
        n = len(nums2)
        i = 0
        j = 0
        idx1 = (m+n)//2-1
        idx2 = (m+n)//2
        count = 0 # to keep track of index of the combined array
        # these are the numbers at the indexes idx1 and idx2 in the combined sorted array
        element1 = 0
        element2 = 0
        while i<m and j<n:
            if nums1[i]<nums2[j]:
                if count==idx1:
                    element1 = nums1[i]
                if count==idx2:
                    element2 = nums1[i]
                i+=1
                count+=1
            else:
                if count==idx1:
                    element1 = nums2[j]
                if count==idx2:
                    element2 = nums2[j]
                j+=1
                count+=1

        # if nums1 elements are left
        while i<m:
            if count==idx1:
                element1 = nums1[i]
            if count==idx2:
                element2 = nums1[i]
            i+=1
            count+=1

        # if nums2 elements are left
        while j<n:
            if count==idx1:
                element1 = nums2[j]
            if count==idx2:
                element2 = nums2[j]
            j+=1
            count+=1

        # calculating median
        if (m+n)%2==1:
            return float(element2)
        else:
            return (element1+element2)/2   
        
        
# time complexity: O(log(min(n,m))), space complexity: O(1)
# here
# Explanation for (m+n+1)//2
# if nums1 has 3 elements and nums2 has 4 elements, and we split based on median index (length up till median index), (m+n+1)//2 = 4 (4th element) which is the median element on which we can divide the combined index on: [_ _ _ _][_ _ _]
# similarly we both had 4 elements (m+n+1)//2 = 4 and the split logic works fine in this confition too, so (m+n+1)//2 is a good way to find median index and split
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            return self.findMedianSortedArrays(nums2,nums1) # ensure nums1 is the smaller array, and dont forget to return
        m = len(nums1) # the smaller one
        n = len(nums2)

        l = 0 # picking up min of 0 elements from nums1 in first half
        r = m # piking up max of m elements from nums1 in first half

        while l<=r:
            # px and py are for left partition elemets of nums1 and nums2 respectively
            # px refers to number of elements from nums1 we take in the first partition
            # py = (m+n+1)//2 - px refers to number of elements from nums2 we take in the first partition
            px = (l+r)//2 # number of elemnts for nums1
            py = (m+n+1)//2 - px # number of elemnts for nums2

            # x1 = last element of nums1's left partition
            # x2 = last element of nums2's left partition
            # x3 = first element of nums1's right partition
            # x4 = first element of nums2's right partition
            
            # left half
            x1 = nums1[px-1] if px>0 else float("-inf") # here px-1 is the last element of left partition of nums1 and we use -inf if px is 0
            x2 = nums2[py-1] if py>0 else float("-inf") # here py-1 is the last element of left partition of nums2 and we use -inf if py is 0

            # right half
            x3 = nums1[px] if px<m else float("inf") # here px is the first element of right partition of nums1 and we use inf if px is m
            x4 = nums2[py] if py<n else float("inf") # here py is the first element of right partition of nums2 and we use inf if py is n

            if (x1<=x4 and x2<=x3):
                if (m+n)%2==1:
                    return max(x1, x2)
                else:
                    return (max(x1,x2)+min(x3,x4))/2

            elif (x1>x4):
                r = px-1
            else:
                l = px+1

        return -1


# Understanding the approach first

# The problem wants O(log(min(m,n))) — way faster than merging (O(m+n)). The way to achieve that: don't merge anything. Instead, binary search for the correct way to partition both arrays into a "left half" and "right half" such that:

# Left half has exactly (m+n+1)//2 elements total (this guarantees correct median position for both odd/even total length)
# Every element in the left half ≤ every element in the right half

# Once you find such a partition, the median is just derived from the border elements — no merging needed.

# The four boundary values

# For a given split px (elements taken from nums1's left) and py (elements taken from nums2's left):

# nums1: [ ... x1 | x3 ... ]     (px elements on the left)
# nums2: [ ... x2 | x4 ... ]     (py elements on the left)
# x1 = last element of nums1's left partition
# x2 = last element of nums2's left partition
# x3 = first element of nums1's right partition
# x4 = first element of nums2's right partition

# Valid partition condition: x1 <= x4 AND x2 <= x3 — this means everything in the combined left half is ≤ everything in the combined right half.

# If x1 > x4, our nums1 partition is taking too many elements (need to shrink px) → r = px - 1
# If it's not x1 > x4, by elimination x2 > x3 must be true, meaning we need more from nums1 → l = px + 1

# Dry run 1: nums1 = [2,4,8], nums2 = [9,12,19,20]

# m=3, n=4 (nums1 is already smaller, no swap). Total = 7 (odd). (m+n+1)//2 = 4

# l=0, r=3

# Iteration 1: l=0, r=3

# px = (0+3)//2 = 1 → take 1 element from nums1's left
# py = 4 - 1 = 3 → take 3 elements from nums2's left
# nums1 partition: [2 | 4, 8]        (px=1)
# nums2 partition: [9,12,19 | 20]    (py=3)
# x1 = nums1[0] = 2
# x2 = nums2[2] = 19
# x3 = nums1[1] = 4
# x4 = nums2[3] = 20

# Check: x1<=x4 → 2<=20 ✓, x2<=x3 → 19<=4 ✗ → invalid partition

# Since x1 > x4 is 2 > 20 → False, we go to else: l = px+1 = 2

# Interpretation: nums2's left side has too big a number (19) sitting where a right-side number should be — we need MORE elements from nums1 to "absorb" some of nums2's smaller elements into the left half.

# Iteration 2: l=2, r=3

# px = (2+3)//2 = 2
# py = 4-2 = 2
# nums1 partition: [2,4 | 8]      (px=2)
# nums2 partition: [9,12 | 19,20] (py=2)
# x1 = nums1[1] = 4
# x2 = nums2[1] = 12
# x3 = nums1[2] = 8
# x4 = nums2[2] = 19

# Check: x1<=x4 → 4<=19 ✓, x2<=x3 → 12<=8 ✗ → still invalid

# x1>x4? 4>19 → False → else: l = px+1 = 3

# Iteration 3: l=3, r=3

# px = (3+3)//2 = 3
# py = 4-3 = 1
# nums1 partition: [2,4,8 | ]     (px=3, ALL of nums1 on left, so x3 = +inf)
# nums2 partition: [9 | 12,19,20] (py=1)
# x1 = nums1[2] = 8
# x2 = nums2[0] = 9
# x3 = float('inf') since px=3=m (no elements left in nums1's right partition)
# x4 = nums2[1] = 12

# Check: x1<=x4 → 8<=12 ✓, x2<=x3 → 9<=inf ✓ → valid partition!

# (m+n)=7 is odd → return max(x1,x2) = max(8,9) = 9

# Verification: merged sorted array = [2,4,8,9,12,19,20] → the middle (4th) element is indeed 9 ✅

# Dry run 2: nums1 = [2,4,9], nums2 = [8,10,12]

# m=3, n=3. Total = 6 (even). (m+n+1)//2 = 3

# l=0, r=3

# Iteration 1: l=0, r=3

# px = (0+3)//2 = 1
# py = 3-1 = 2
# nums1: [2 | 4,9]     (px=1)
# nums2: [8,10 | 12]   (py=2)
# x1=nums1[0]=2, x2=nums2[1]=10, x3=nums1[1]=4, x4=nums2[2]=12

# Check: x1<=x4 → 2<=12 ✓, x2<=x3 → 10<=4 ✗ → invalid

# x1>x4? 2>12 False → l = px+1 = 2

# Iteration 2: l=2, r=3

# px = (2+3)//2 = 2
# py = 3-2 = 1
# nums1: [2,4 | 9]    (px=2)
# nums2: [8 | 10,12]  (py=1)
# x1=nums1[1]=4, x2=nums2[0]=8, x3=nums1[2]=9, x4=nums2[1]=10

# Check: x1<=x4 → 4<=10 ✓, x2<=x3 → 8<=9 ✓ → valid!

# (m+n)=6 is even → return (max(x1,x2) + min(x3,x4)) / 2 = (max(4,8) + min(9,10)) / 2 = (8+9)/2 = 8.5

# Verification: merged sorted array = [2,4,8,9,10,12] → middle two elements are 8 and 9 → average = 8.5 ✅
        
# Dry run 3
# Example: nums1 = [5,6,7], nums2 = [1,2,3,4]

# m=3, n=4 (nums1 is already smaller, no swap needed). Total = 7. (m+n+1)//2 = 4

# l=0, r=3

# Iteration 1: l=0, r=3

# px = (0+3)//2 = 1
# py = 4 - 1 = 3
# nums1 partition: [5 | 6,7]        (px=1)
# nums2 partition: [1,2,3 | 4]      (py=3)
# x1 = nums1[0] = 5
# x2 = nums2[2] = 3
# x3 = nums1[1] = 6
# x4 = nums2[3] = 4

# Check: x1<=x4 → 5<=4 → False → invalid partition

# Since x1 > x4 is 5 > 4 → True → r = px-1 = 0

# Interpretation: nums1's left-side element (5) is bigger than nums2's right-side element (4) — meaning we took TOO MANY elements from nums1's left. We need to shrink px.

# Iteration 2: l=0, r=0

# px = (0+0)//2 = 0 ← here it is, px=0
# py = 4 - 0 = 4
# nums1 partition: [ | 5,6,7]         (px=0, nothing on left)
# nums2 partition: [1,2,3,4 | ]       (py=4=n, everything on left)
# x1 = float('-inf') since px=0
# x2 = nums2[3] = 4
# x3 = nums1[0] = 5 since px<m
# x4 = float('inf') since py=4=n (nothing left in nums2's right partition)

# Check: x1<=x4 → -inf<=inf ✓, x2<=x3 → 4<=5 ✓ → valid!

# (m+n)=7 odd → return max(x1,x2) = max(-inf, 4) = 4

# Verification: merged = [1,2,3,4,5,6,7] → 4th element = 4 ✅

# The takeaway

# The binary search explores the entire valid range [0, m] for px across its iterations via the l/r pointers — 
# px=1 was simply where the first midpoint landed, not a fixed starting assumption. When that first guess turned out too high, 
# r shrank down to 0, and the next midpoint became px=0 naturally. So yes, the case "take everything from nums2" is fully covered — 
# it's just reached after one or more corrective iterations, exactly like any binary search converges to its answer from an initial guess.