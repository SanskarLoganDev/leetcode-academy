# 3207. Maximum Points After Enemy Battles

# You are given an integer array enemyEnergies denoting the energy values of various enemies.

# You are also given an integer currentEnergy denoting the amount of energy you have initially.

# You start with 0 points, and all the enemies are unmarked initially.

# You can perform either of the following operations zero or multiple times to gain points:

# Choose an unmarked enemy, i, such that currentEnergy >= enemyEnergies[i]. By choosing this option:
# You gain 1 point.
# Your energy is reduced by the enemy's energy, i.e. currentEnergy = currentEnergy - enemyEnergies[i].
# If you have at least 1 point, you can choose an unmarked enemy, i. By choosing this option:
# Your energy increases by the enemy's energy, i.e. currentEnergy = currentEnergy + enemyEnergies[i].
# The enemy i is marked.
# Return an integer denoting the maximum points you can get in the end by optimally performing operations.

 

# Example 1:

# Input: enemyEnergies = [3,2,2], currentEnergy = 2

# Output: 3

# Explanation:

# The following operations can be performed to get 3 points, which is the maximum:

# First operation on enemy 1: points increases by 1, and currentEnergy decreases by 2. So, points = 1, and currentEnergy = 0.
# Second operation on enemy 0: currentEnergy increases by 3, and enemy 0 is marked. So, points = 1, currentEnergy = 3, and marked enemies = [0].
# First operation on enemy 2: points increases by 1, and currentEnergy decreases by 2. So, points = 2, currentEnergy = 1, and marked enemies = [0].
# Second operation on enemy 2: currentEnergy increases by 2, and enemy 2 is marked. So, points = 2, currentEnergy = 3, and marked enemies = [0, 2].
# First operation on enemy 1: points increases by 1, and currentEnergy decreases by 2. So, points = 3, currentEnergy = 1, and marked enemies = [0, 2].

# Example 2:

# Input: enemyEnergies = [2], currentEnergy = 10

# Output: 5

# Explanation:

# Performing the first operation 5 times on enemy 0 results in the maximum number of points.

# Constraints:

# 1 <= enemyEnergies.length <= 105
# 1 <= enemyEnergies[i] <= 109
# 0 <= currentEnergy <= 109




from typing import List

# Time complexity calculation: O(n×C)

# Action 1 — "defeat" (gain a point): Notice this branch does not set marked[min_idx] = True. 
# This means the same cheapest enemy can be selected again on the next iteration of the while loop, over and over, as long as currentEnergy remains large enough to afford it. Each time, currentEnergy shrinks by enemyEnergies[min_idx].

# Action 2 — "absorb" (no point, but marks permanently): This branch does mark the enemy, removing it from consideration forever. 
# This can happen at most n times total, since there are only n enemies to mark.
# Putting it together

# Let C = initial currentEnergy, and let m = smallest positive value in enemyEnergies (worst case m=1). The number of "defeat" iterations is bounded by O(C / m), and "absorb" iterations are bounded by O(n). 
# Each iteration (regardless of which branch) costs O(n) due to the linear scan for min or max.
# In the worst case (m=1), this simplifies to:
# O(n×C)

# Space complexity: O(n) for the marked list

class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        n = len(enemyEnergies)
        marked = [False] * n
        points = 0

        while True:
            # scan for the cheapest unmarked enemy right now
            min_idx = -1
            for i in range(n):
                if not marked[i]:
                    if min_idx == -1 or enemyEnergies[i] < enemyEnergies[min_idx]:
                        min_idx = i

            # if we can afford it, defeat it -- gain 1 point, does NOT mark it
            if min_idx != -1 and enemyEnergies[min_idx] <= currentEnergy:
                currentEnergy -= enemyEnergies[min_idx]
                points += 1
                continue

            # can't afford the cheapest one -- try absorbing the priciest unmarked enemy instead
            if points > 0:
                max_idx = -1
                for i in range(n):
                    if not marked[i]:
                        if max_idx == -1 or enemyEnergies[i] > enemyEnergies[max_idx]:
                            max_idx = i
                if max_idx != -1:
                    currentEnergy += enemyEnergies[max_idx]
                    marked[max_idx] = True
                    continue

            # neither action is possible -- we're stuck, 
            # do not use else for break here as it would only work if points == 0 and not for any other failure cases
            break

        return points

# slightly more optimised solution
# Time: O(nlogn) due to sorting
# Space: O(1)

class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        enemyEnergies.sort()
        n = len(enemyEnergies)
        points = 0
        lo = 0
        hi = n-1
        while lo<=hi:
            if currentEnergy >= enemyEnergies[lo]:
                # batch-defeat the cheapest available enemy as many times as affordable
                # (its value never changes, so no need to simulate one op at a time)
                times = currentEnergy//enemyEnergies[lo]
                currentEnergy-=enemyEnergies[lo]*times
                points+=times

            if currentEnergy < enemyEnergies[lo]:
                if points > 0:
                    # refill using the largest remaining enemy, then mark it (remove from pool)
                    currentEnergy += enemyEnergies[hi]
                    hi-=1
                else:
                    break # truly stuck: can't afford defeat, and no points to unlock absorb
        return points
    
    
# BEST OPTIMISED SOLUTION
# Time: O(N)
# Space: O(1)

# Logic: Absorbing is always worth doing since it's free energy that costs no points, 
# so the optimal play is to absorb every enemy except one — reserved permanently as a cheap, endlessly reusable defeat target. 
# Since addition doesn't care about order, the total energy you'll ever have access to is just currentEnergy + sum(all enemies) - mn, 
# with no need to simulate absorbing them one at a time. Dividing that total by the reserved enemy's cost gives the maximum points directly, 
# as long as you could afford that cheapest enemy in the first place to earn your bootstrap point.

class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        mn = float('inf')
        totalEnergy = currentEnergy

        for energy in enemyEnergies:
            if energy < mn:
                mn = energy          # track the cheapest enemy -- this is the one we'll keep
                                      # reserved forever as our repeatable defeat target
            totalEnergy += energy    # add every enemy's value in, as if we absorb ALL of them

        if currentEnergy < mn:
            return 0                 # can't even afford the cheapest enemy up front, so we can
                                      # never earn the first point needed to unlock absorbing at all

        totalEnergy -= mn            # undo adding in the reserved cheapest enemy -- we never
                                      # actually absorb it, we keep it around to defeat repeatedly
        return totalEnergy // mn     # every unit of energy we'll ever have access to, divided by
                                      # the cost of one repeatable defeat, gives max possible points