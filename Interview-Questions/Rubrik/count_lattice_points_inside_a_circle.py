# 2249. Count Lattice Points Inside a Circle

# Given a 2D integer array circles where circles[i] = [xi, yi, ri] represents the center (xi, yi) and radius ri of the ith circle drawn on a grid, return the number of lattice points that are present inside at least one circle.

# Note:

# A lattice point is a point with integer coordinates.
# Points that lie on the circumference of a circle are also considered to be inside it.
 

# Example 1:

# Input: circles = [[2,2,1]]
# Output: 5
# Explanation:
# The figure above shows the given circle.
# The lattice points present inside the circle are (1, 2), (2, 1), (2, 2), (2, 3), and (3, 2) and are shown in green.
# Other points such as (1, 1) and (1, 3), which are shown in red, are not considered inside the circle.
# Hence, the number of lattice points present inside at least one circle is 5.

# Example 2:

# Input: circles = [[2,2,2],[3,4,1]]
# Output: 16
# Explanation:
# The figure above shows the given circles.
# There are exactly 16 lattice points which are present inside at least one circle. 
# Some of them are (0, 2), (2, 0), (2, 4), (3, 2), and (4, 4).
 

# Constraints:

# 1 <= circles.length <= 200
# circles[i].length == 3
# 1 <= xi, yi <= 100
# 1 <= ri <= min(xi, yi)

from typing import List

# time complexity: O(N*R^2) where N = len(circles) and R = maximum radius
# Space: O(N · r_max²) in the worst case, for the points set — bounded by the total number of (point, circle) checks, 
# though in practice the set only grows to the number of distinct points actually inside some circle, which is at most that same bound.

class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        lattice_set = set()
        for circle in circles:
            x = circle[0]
            y = circle[1]
            r = circle[2]
            for i in range(circle[0]-r, circle[0]+r+1):
                for j in range(circle[1]-r, circle[1]+r+1):
                    if (i-x)**2 + (j-y)**2 <= r*r:
                        lattice_set.add((i,j))

        return len(lattice_set)
    
    
# Optimised solution
# time complexity: O(N*R^2)
# Space complexity: O(1) since visited grid size is fixed
class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        grid_size = 201
        visited = [[False]*grid_size for _ in range(grid_size)]
        count = 0
        for circle in circles:
            x = circle[0]
            y = circle[1]
            r = circle[2]
            for i in range(circle[0]-r, circle[0]+r+1):
                for j in range(circle[1]-r, circle[1]+r+1):
                    if (i-x)**2 + (j-y)**2 <= r*r:
                        if not visited[i][j]:
                            count+=1
                            visited[i][j] = True

        return count
