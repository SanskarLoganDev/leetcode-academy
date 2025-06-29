# 239. Sliding Window Maximum (Neetcode 150) Important

# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

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

# Time Complexity: O(n*k) (if k=n, O(n^2)), Space Complexity: O(n)
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
    
# Efficent Solution: Using Deque (Monotonic Queue)

## Time Complexity: O(n), Space Complexity: O(n)

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = r = 0
        q = deque() # indexes
        output = []

        while r<len(nums):
            # pop smaller values from q
            while q and nums[r]>nums[q[-1]]:
                q.pop()
            q.append(r)

            # if left value is out of bounds, remove the left val from window
            if l>q[0]:
                q.popleft()

            if (r+1)>=k:
                output.append(nums[q[0]])
                l+=1
            r+=1

        return output
    
# Explanation:
# You need two separate checks because, on each slide of the window, these two events—“we’ve just gathered enough elements to start reporting a max” and “the old max has slid off the left edge so we must evict it”—don’t always happen at exactly the same time. If you collapse them into one if (r+1)>=k: … popleft() … you end up popping your deque even when the index at the front is still in the window.

# Walk-through on [1,3,-1,-3,5,...], k=3

# r=0 (window size 1)
# q building: [0]
# (r+1)>=k? 1>=3 → False, so no output, no pop, no l++.

# r=1 (window size 2)
# q: you pop smaller than 3 so q → [1]
# (r+1)>=k? 2>=3 → False again.

# r=2 (window size 3, now big enough to report)
# q: append index 2 → q = [1,2]

# Correct code:

# if l > q[0]:       # 0 > 1 ? no → don’t pop
#     q.popleft()

# if (r+1) >= k:     # 3 >= 3 ? yes → output nums[q[0]] == nums[1] == 3; l+=1
#     output.append(3)
#     l = 1
# q stays [1,2].

# Collapsed code would do:

# if (r+1)>=k:      # 3>=3 → yes
#     output.append(nums[q[0]])  # 3
#     q.popleft()                # WRONG: pops 1 although 1 is still in the window [0..2]
#     l += 1                     # l=1
# Now q becomes [2] even though index 1 (the max) is still in the legal window [1..2].

# r=3 (window is now [1..3])

# Correct deque after step r=2 was [1,2], so at r=3—before pop—you’d compare window [3,-1,-3] and pop index 1 only if l > q[0] (1 > 1? no). You still see 3 at q[0] and report 3 again.

# With the collapsed version, you lost that 1 prematurely, so your max becomes nums[2] == -1, which is wrong.

# The takeaway
# Eviction (if l > q[0]: q.popleft()) must only happen when the left pointer has actually moved past the index at the front of your deque.

# Output (if r+1 >= k:) must happen exactly when the window first reaches size k and on every slide thereafter.

# They can coincide sometimes, but not always—so you need two separate if statements.

# Keeping them apart guarantees you only ever drop an index once it truly falls out of the window, while still printing your max exactly once per slide.