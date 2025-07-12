# 875. Koko Eating Bananas (Neetcode 150) Important

# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.


# Example 1:

# Input: piles = [3,6,7,11], h = 8
# Output: 4
# Example 2:

# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
# Example 3:

# Input: piles = [30,11,23,4,20], h = 6
# Output: 23
 

# Constraints:

# 1 <= piles.length <= 104
# piles.length <= h <= 109
# 1 <= piles[i] <= 109

from typing import List

# Time complexity: O(n * max(piles)), where n is the number of piles and max(piles) is the maximum number of bananas in a pile.
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours(k):
            count = 0
            for bananas in piles:
                if bananas%k == 0:
                    count+=bananas//k
                else:
                    count = count + (bananas//k) + 1
            return count
                
        for k in range(1, max(piles)+1):
            count_hours = hours(k)
            if count_hours<=h:
                return k
            
# Time complexity: O(n log(max(piles))), where n is the number of piles and max(piles) is the maximum number of bananas in a pile.
class Solution:
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours(k): # function to calculate the number of hours required to eat all bananas at speed k
            count = 0
            for bananas in piles:
                if bananas%k == 0:
                    count+=bananas//k
                else:
                    count = count + (bananas//k) + 1
            return count
        # considering the minimum speed as 1 and maximum speed as max(piles) [range of k]
        l = 1
        r = max(piles)
        res = r
        while l<=r:
            mid_k = (l+r)//2
            count_hours = hours(mid_k)
            if count_hours>h:
                l = mid_k+1
            elif count_hours<=h:
                res = min(res, mid_k) # if we find a valid k, we update the result
                r = mid_k-1
        return res
        
        