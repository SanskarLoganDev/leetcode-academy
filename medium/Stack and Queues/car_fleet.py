# 853. Car Fleet 
# (Neetcode 150) Important

# There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.
# You are given two integer array position and speed, both of length n, where position[i] is the starting mile of the ith car and speed[i] is the speed of the ith car in miles per hour.
# A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.
# A car fleet is a car or cars driving next to each other. The speed of the car fleet is the minimum speed of any car in the fleet.
# If a car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet.
# Return the number of car fleets that will arrive at the destination.


# Example 1:
# Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
# Output: 3

# Explanation:
# The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12. The fleet forms at target.
# The car starting at 0 (speed 1) does not catch up to any other car, so it is a fleet by itself.
# The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.

# Example 2:
# Input: target = 10, position = [3], speed = [3]
# Output: 1

# Explanation:
# There is only one car, hence there is only one fleet.

# Example 3:
# Input: target = 100, position = [0,2,4], speed = [4,2,1]
# Output: 1

# Explanation:
# The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The car starting at 4 (speed 1) travels to 5.
# Then, the fleet at 4 (speed 2) and the car at position 5 (speed 1) become one fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
 
# Constraints:

# n == position.length == speed.length
# 1 <= n <= 105
# 0 < target <= 106
# 0 <= position[i] < target
# All the values of position are unique.
# 0 < speed[i] <= 106

# Key Rule: A car can only interact with the car directly ahead of it. If it cannot catch that car, nothing beyond matters. 
# If it does catch that car, the merged fleet time already accounts for everything ahead.

from typing import List
# time complexity: O(n log n) due to sorting, space complexity: O(n)
# without using stack, just logic
from typing import List

class Solution:

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n =  len(position)
        cars = []
        # step 1: pair position and speed together, sort by position descending
        # descending because we want to process cars closest to target first
        for i in range(n):
            cars.append([position[i], speed[i]])
        cars.sort(reverse=True) # sorting the cars

        # step 2: calculate time for each car to reach target
        time = []
        for i in range(n):
            time.append((target - cars[i][0])/cars[i][1])
        
        # step 3: count fleets
        # a car forms a new fleet if it takes LONGER than the car ahead
        # meaning it can never catch up to the car ahead
        # if it takes equal or less time, it catches up and merges into the fleet ahead
        # it then adopts the fleet's slower time (time of car ahead)

        fleet = 1 # first car (closest to target) always forms its own fleet
        for i in range(1, n):
            if time[i]>time[i-1]:
                fleet+=1
            # if it takes equal or less time, it catches up and merges into the fleet ahead, 
            # and we need to update the time of that car to that of the fleet
            else:
                time[i] = time[i-1]
        return fleet    

sol = Solution()
ans = sol.carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3])
print(ans)

# Same complexities, but using stack
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p, s in zip(position, speed)]
        stack = []
        for p, s in sorted(pair)[::-1]: # Reverse Sorted Order
            t = (target - p)/s
            stack.append(t) # Should be appended at the start because we are iterating in reverse order
            # stack[-2] is the front car and stack[-1] is the current/behind car
            # If the front car is slower than the current car, pop the front car
            if len(stack)>=2 and stack[-2] >= stack[-1]:
                stack.pop()
            
        return len(stack)