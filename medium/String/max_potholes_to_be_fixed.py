# 3119. Maximum Number of Potholes That Can Be Fixed Important

# You are given a string road, consisting only of characters "x" and ".", where each "x" denotes a pothole and each "." denotes a smooth road, and an integer budget.

# In one repair operation, you can repair n consecutive potholes for a price of n + 1.

# Return the maximum number of potholes that can be fixed such that the sum of the prices of all of the fixes doesn't go over the given budget.

# Example 1:

# Input: road = "..", budget = 5

# Output: 0

# Explanation:

# There are no potholes to be fixed.

# Example 2:

# Input: road = "..xxxxx", budget = 4

# Output: 3

# Explanation:

# We fix the first three potholes (they are consecutive). The budget needed for this task is 3 + 1 = 4.

# Example 3:

# Input: road = "x.x.xxx...x", budget = 14

# Output: 6

# Explanation:

# We can fix all the potholes. The total cost would be (1 + 1) + (1 + 1) + (3 + 1) + (1 + 1) = 10 which is within our budget of 14.

class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:
        # Step 1: Extract lengths of contiguous pothole groups.
        groups = []
        i = 0
        n = len(road)
        while i < n:
            if road[i] == 'x':
                start = i
                while i < n and road[i] == 'x':
                    i += 1
                groups.append(i - start)
            else:
                i += 1

        # Step 2: Sort groups in descending order (largest groups first).
        groups.sort(reverse=True)

        total_fixed = 0
        # Step 3: Allocate the budget to the groups.
        for length in groups:
            # If the remaining budget is less than 2, we can't fix any potholes 
            # because fixing even 1 pothole costs 1 (for the pothole) + 1 (overhead).
            if budget < 2:
                break

            # If we can fix the entire group
            if length + 1 <= budget:
                total_fixed += length
                budget -= (length + 1)
            else:
                # Otherwise, fix as many as possible from this group.
                # With a budget of B (< length+1), we can fix at most (B - 1) potholes.
                fixed = budget - 1
                total_fixed += fixed
                # Budget is then exhausted (or reduced to 1, which is insufficient to fix any potholes).
                budget = 1

        return total_fixed

# Example usage:
sol = Solution()
print(sol.maxPotholes("x.xxxx", 5))  # Expected output: 4

