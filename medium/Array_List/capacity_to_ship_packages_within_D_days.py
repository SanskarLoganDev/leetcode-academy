# 1011. Capacity To Ship Packages Within D Days
# Neetcode 250
# A conveyor belt has packages that must be shipped from one port to another within days days.

# The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

# Example 1:

# Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
# Output: 15
# Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
# 1st day: 1, 2, 3, 4, 5
# 2nd day: 6, 7
# 3rd day: 8
# 4th day: 9
# 5th day: 10

# Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.

# Example 2:

# Input: weights = [3,2,2,4,1,4], days = 3
# Output: 6
# Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
# 1st day: 3, 2
# 2nd day: 2, 4
# 3rd day: 1, 4

# Example 3:

# Input: weights = [1,2,3,1,1], days = 4
# Output: 3
# Explanation:
# 1st day: 1
# 2nd day: 2
# 3rd day: 3
# 4th day: 1, 1

# Constraints:

# 1 <= days <= weights.length <= 5 * 104
# 1 <= weights[i] <= 500

# Time complexity: O(N*sum(weights))
# Space complexity: O(1)
class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def number_of_days(capacity): # capacity is weights shipped per hour
            total_count = 0
            i = 0
            while i<len(weights): # we use a double while loop to also take care of multiple packages that can be shipped in 1 shipment
                w = 0
                while i<len(weights) and w<=capacity:
                    w+=weights[i]
                    if w>capacity:
                        w-=weights[i] # we remove it from shipment as the capacity limit is exceeded
                        break
                    i+=1
                total_count+=1 # total number of days
            return total_count

        for cap in range(max(weights), sum(weights)+1): # we start with max(weights) we cause we canot break a package in half, 
            # and we end in sum of all weights as we might have to ship all of them in 1 day
            count_days = number_of_days(cap)
            if count_days<=days:
                return cap

# Time complexity" O(N*log(sum(weights)))
# Space complexity: O(1)
class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def number_of_days(capacity): # capacity is weights shipped per hour
            total_count = 0
            i = 0
            while i<len(weights):
                w = 0
                while i<len(weights) and w<=capacity:
                    w+=weights[i]
                    if w>capacity:
                        w-=weights[i]
                        break
                    i+=1
                total_count+=1
            return total_count

        # binary search (similar to Koko eating bananas)
        l = max(weights)
        r = sum(weights)
        res = float("inf")
        while l<=r:
            mid = (l+r)//2
            ndays = number_of_days(mid)
            if ndays>days:
                l=mid+1
            else:
                res=min(res, mid)
                r=mid-1
        return res
