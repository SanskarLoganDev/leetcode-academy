# 239. Sliding Window Maximum 
# (Neetcode 150) Important

# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. 
# You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.


# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7

# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# 1 <= k <= nums.length

# Brute Force Solution

from typing import List

# Time Complexity: O(n*k) (if k=n, O(n^2)), Space Complexity: O(k) since the subarray we create is of size k
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = l+k
        res = []
        while r<=len(nums):
            res.append(max(nums[l:r]))
            l+=1
            r+=1
        return res
    
# Efficent Solution: Using Deque (Monotonic Decreasing Queue)

# Time Complexity: O(n), Space Complexity: O(K) since the queue can have a maximum of K values in it

from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()  # stores indices, maintained in decreasing order of values (front=max, back=min)
        output = []
        
        for i in range(len(nums)):
            # step 1: remove indices from front that are out of current window [i-k+1, i]
            while q and q[0] <= i-k:
                q.popleft()
                
            # step 2: remove indices from back whose values are smaller than nums[i]
            # no point keeping them since nums[i] is larger and will stay in window longer
            while q and nums[i] > nums[q[-1]]:
                q.pop()
                
            # step 3: push current index to back
            q.append(i)
            
            # step 4: once we have processed at least k elements, front of deque is always the max
            if i >= k-1:
                output.append(nums[q[0]])  # q[0] = front = index of maximum value

        return output

sol = Solution()
ans = sol.maxSlidingWindow(nums=[1,3,-1,-3,5,3,6,7], k=3)
print(ans)  # [3,3,5,5,6,7]
    
# Detailed Dry Run
# nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
# window valid from i = k-1 = 2 onwards

# i=0, nums[0]=1

# step 1: q empty → skip
# step 2: q empty → skip
# step 3: q.append(0) → q = [0]
# step 4: i=0 < k-1=2 → skip

# q = [0]  (values: [1])
# output = []

# i=1, nums[1]=3

# step 1: q[0]=0, 0 <= 1-3=-2? → No → skip
# step 2: nums[1]=3 > nums[q[-1]]=nums[0]=1? → Yes → pop 0
#         q = []
#         q empty → stop
# step 3: q.append(1) → q = [1]
# step 4: i=1 < k-1=2 → skip

# q = [1]  (values: [3])
# output = []

# i=2, nums[2]=-1

# step 1: q[0]=1, 1 <= 2-3=-1? → No → skip
# step 2: nums[2]=-1 > nums[q[-1]]=nums[1]=3? → No → skip
# step 3: q.append(2) → q = [1, 2]
# step 4: i=2 >= k-1=2 → output.append(nums[q[0]])=nums[1]=3

# q = [1, 2]  (values: [3, -1])
# output = [3]
# window = [1, 3, -1] → max=3 ✅

# i=3, nums[3]=-3

# step 1: q[0]=1, 1 <= 3-3=0? → No → skip
# step 2: nums[3]=-3 > nums[q[-1]]=nums[2]=-1? → No → skip
# step 3: q.append(3) → q = [1, 2, 3]
# step 4: i=3 >= 2 → output.append(nums[q[0]])=nums[1]=3

# q = [1, 2, 3]  (values: [3, -1, -3])
# output = [3, 3]
# window = [3, -1, -3] → max=3 ✅

# i=4, nums[4]=5

# step 1: q[0]=1, 1 <= 4-3=1? → Yes → popleft → q = [2, 3]
#         q[0]=2, 2 <= 1? → No → stop
# step 2: nums[4]=5 > nums[q[-1]]=nums[3]=-3? → Yes → pop 3 → q = [2]
#         nums[4]=5 > nums[q[-1]]=nums[2]=-1? → Yes → pop 2 → q = []
#         q empty → stop
# step 3: q.append(4) → q = [4]
# step 4: i=4 >= 2 → output.append(nums[q[0]])=nums[4]=5

# q = [4]  (values: [5])
# output = [3, 3, 5]
# window = [-1, -3, 5] → max=5 ✅

# i=5, nums[5]=3

# step 1: q[0]=4, 4 <= 5-3=2? → No → skip
# step 2: nums[5]=3 > nums[q[-1]]=nums[4]=5? → No → skip
# step 3: q.append(5) → q = [4, 5]
# step 4: i=5 >= 2 → output.append(nums[q[0]])=nums[4]=5

# q = [4, 5]  (values: [5, 3])
# output = [3, 3, 5, 5]
# window = [-3, 5, 3] → max=5 ✅

# i=6, nums[6]=6

# step 1: q[0]=4, 4 <= 6-3=3? → No → skip
# step 2: nums[6]=6 > nums[q[-1]]=nums[5]=3? → Yes → pop 5 → q = [4]
#         nums[6]=6 > nums[q[-1]]=nums[4]=5? → Yes → pop 4 → q = []
#         q empty → stop
# step 3: q.append(6) → q = [6]
# step 4: i=6 >= 2 → output.append(nums[q[0]])=nums[6]=6

# q = [6]  (values: [6])
# output = [3, 3, 5, 5, 6]
# window = [5, 3, 6] → max=6 ✅

# i=7, nums[7]=7

# step 1: q[0]=6, 6 <= 7-3=4? → No → skip
# step 2: nums[7]=7 > nums[q[-1]]=nums[6]=6? → Yes → pop 6 → q = []
#         q empty → stop
# step 3: q.append(7) → q = [7]
# step 4: i=7 >= 2 → output.append(nums[q[0]])=nums[7]=7

# q = [7]  (values: [7])
# output = [3, 3, 5, 5, 6, 7]
# window = [3, 6, 7] → max=7 ✅
# return [3, 3, 5, 5, 6, 7] ✅