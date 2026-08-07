# 528. Random Pick with Weight

# You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.

# You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).

# For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).
 

# Example 1:

# Input
# ["Solution","pickIndex"]
# [[[1]],[]]
# Output
# [null,0]

# Explanation
# Solution solution = new Solution([1]);
# solution.pickIndex(); // return 0. The only option is to return 0 since there is only one element in w.

# Example 2:

# Input
# ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
# [[[1,3]],[],[],[],[],[]]
# Output
# [null,1,1,1,1,0]

# Explanation
# Solution solution = new Solution([1, 3]);
# solution.pickIndex(); // return 1. It is returning the second element (index = 1) that has a probability of 3/4.
# solution.pickIndex(); // return 1
# solution.pickIndex(); // return 1
# solution.pickIndex(); // return 1
# solution.pickIndex(); // return 0. It is returning the first element (index = 0) that has a probability of 1/4.

# Since this is a randomization problem, multiple answers are allowed.
# All of the following outputs can be considered correct:
# [null,1,1,1,1,0]
# [null,1,1,1,1,1]
# [null,1,1,1,0,0]
# [null,1,1,1,0,1]
# [null,1,0,1,0,0]
# ......
# and so on.
 

# Constraints:

# 1 <= w.length <= 104
# 1 <= w[i] <= 105
# pickIndex will be called at most 104 times.

from typing import List

import random
class Solution:
    # Time: O(n) — building indexes, summing w, and building probabilities are each O(n), so total is O(n)
    # Space: O(n) — both self.indexes and self.probabilities store n elements each → O(n)
    def __init__(self, w: List[int]):
        self.probabilities = []
        self.indexes = [i for i in range(len(w))]
        total = sum(w)
        for i in range(len(w)):
            self.probabilities.append(w[i]/total)

    # Time: O(n) per call
    # Space: O(n) per call — the cumulative weights list built internally by random.choices is a temporary O(n)-sized list 
    # (garbage collected after the call returns, but still counts as space used during execution)
    def pickIndex(self) -> int:
        return random.choices(self.indexes, self.probabilities, k=1)[0] # randomly picks up an element based on probabilities
    # k=1 determines how many elements to return. At the end we have [0] as random.choices returns list of k elements


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

# Optimised solution using binary search on prefix sum

import random
import bisect
class Solution:

    def __init__(self, w: List[int]):
        self.prefixSum = [] # Space: O(N)
        self.cumSum = 0
        for i in range(len(w)): # O(N)
            self.cumSum+=w[i]
            self.prefixSum.append(self.cumSum)
        

    def pickIndex(self) -> int:
        target = random.randint(1, self.cumSum) # O(1)
        return bisect.bisect_left(self.prefixSum, target) # essentially binary search, so O(log(n))


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

# Dry run of your exact __init__, with w = [1, 3, 6]

# self.prefixSum = [], self.cumSum = 0

# i=0: w[0]=1. self.cumSum += 1 → cumSum=1. self.prefixSum.append(1) → prefixSum=[1]
# i=1: w[1]=3. self.cumSum += 3 → cumSum=4. self.prefixSum.append(4) → prefixSum=[1,4]
# i=2: w[2]=6. self.cumSum += 6 → cumSum=10. self.prefixSum.append(10) → prefixSum=[1,4,10]

# After __init__: self.prefixSum = [1,4,10], self.cumSum = 10. Each entry in prefixSum marks "the running total of weight up through and including this index."

# Dry run of pickIndex(), using bisect_left

# Say random.randint(1, 10) returns target = 4 (a boundary value, chosen deliberately since it's the interesting case).

# bisect.bisect_left(self.prefixSum, 4) performs binary search: lo=0, hi=3. mid=1, prefixSum[1]=4. Question: "is 4 < 4?" False → since the array value isn't less than target, this position is a valid candidate, so search narrows left: hi=1. Now lo=0, hi=1: mid=0, prefixSum[0]=1. Is 1 < 4? True → search right: lo=1. Loop ends (lo==hi==1) → returns 1.

# So pickIndex() returns 1. This is correct: target=4 is the last value belonging to index 1's range (target=2,3,4, since w[1]=3 means index 1 should own exactly 3 of the 10 possible target values).