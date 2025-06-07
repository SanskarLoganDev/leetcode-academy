# 347. Top K Frequent Elements Neetcode 150 Important

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
 
# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

# time complexity O(n log k) (leetcode says it is O(n))
# space complexity O(n) for storing the count of each element.
from typing import List
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return [x[0] for x in count.most_common(k)]
    
# Putting it together:

# Counting frequencies: O(n)
# Finding top k: O(u log k)
# Extracting keys: O(k)
# In the worst case u≈n, giving O(n log k + n), which is often written as O(n log k) when k≪n.

# n = the length of the input list nums.
# u = the number of distinct elements in nums (i.e. the size of count).
# k = the argument “how many top frequent elements” you want to return.

# Neetcode solution having O(n) time complexity using bucket sort reverse.
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freq = [[] for _ in range(len(nums)+1)]
        for n in nums:
            counts[n] = 1+counts.get(n, 0)
        for n, c in counts.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res

# Explanation:
# Let n = len(nums) and u be the number of distinct elements in nums (so u ≤ n). The code does:

# Build the frequency map

# for n in nums:
#     counts[n] = 1 + counts.get(n, 0)
# – One dictionary get + update per element → O(n).

# Bucket numbers by their counts

# freq = [[] for _ in range(n+1)]    # O(n) to allocate
# for num, c in counts.items():      # u items
#     freq[c].append(num)            # O(1) each
# – Allocating the list of n+1 buckets → O(n).
# – Distributing u keys into buckets → O(u), which is ≤ O(n).

# Collect top-k from the buckets

# for i in range(n, 0, -1):          # up to n iterations
#   for num in freq[i]:              # only as many as have frequency i
#     res.append(num)
#     if len(res) == k:
#       return res
# – You scan down from frequency n to 1.
# – In the worst case you touch each empty bucket once (n steps) and then visit exactly k elements before stopping.
# – Total here is O(n + k) = O(n) since k ≤ n.

# Putting it all together:

# O(n) to count

# + O(n) to build buckets

# + O(n) to scan buckets

# → Overall time complexity: O(n).

# (Space complexity is also O(n), for the count map and the bucket list.)
