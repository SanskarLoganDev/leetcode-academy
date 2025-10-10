# 2013. Detect Squares
# Neetcode 150 (Important)

# You are given a stream of points on the X-Y plane. Design an algorithm that:

# Adds new points from the stream into a data structure. Duplicate points are allowed and should be treated as different points.
# Given a query point, counts the number of ways to choose three points from the data structure such that the three points and the query point form an axis-aligned square with positive area.
# An axis-aligned square is a square whose edges are all the same length and are either parallel or perpendicular to the x-axis and y-axis.

# Implement the DetectSquares class:

# DetectSquares() Initializes the object with an empty data structure.
# void add(int[] point) Adds a new point point = [x, y] to the data structure.
# int count(int[] point) Counts the number of ways to form axis-aligned squares with point point = [x, y] as described above.
 

# Example 1:

# https://assets.leetcode.com/uploads/2021/09/01/image.png
# Input
# ["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
# [[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]
# Output
# [null, null, null, null, 1, 0, null, 2]

# Explanation
# DetectSquares detectSquares = new DetectSquares();
# detectSquares.add([3, 10]);
# detectSquares.add([11, 2]);
# detectSquares.add([3, 2]);
# detectSquares.count([11, 10]); // return 1. You can choose:
#                                //   - The first, second, and third points
# detectSquares.count([14, 8]);  // return 0. The query point cannot form a square with any points in the data structure.
# detectSquares.add([11, 2]);    // Adding duplicate points is allowed.
# detectSquares.count([11, 10]); // return 2. You can choose:
#                                //   - The first, second, and third points
#                                //   - The first, third, and fourth points


from typing import List
class DetectSquares:

    def __init__(self):
        self.ptsCount = {}

    def add(self, point: List[int]) -> None:
        if tuple(point) in self.ptsCount:
            self.ptsCount[tuple(point)]+=1
        else:
            self.ptsCount[tuple(point)] = 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.ptsCount:
            # cases where queare is impossible
            if abs(px-x)!=abs(py-y) or x==px or y==py:
                continue
            # now checking how to prove a square
            c = self.ptsCount[(x, y)]
            
            # in res below we multiply by c because there can be multiple points at (x,y)
            # we multiply by self.ptsCount.get((x, py),0) because there can be multiple points at (x, py)
            # we multiply by self.ptsCount.get((px, y),0) because there can be multiple points at (px, y)
            # if there are no points at (x, py) or (px, y) then we multiply by 0 and that square is not possible
            # we use get method to avoid key error if (x, py) or (px, y) is not in the dictionary
            res = res + c*self.ptsCount.get((x, py),0)*self.ptsCount.get((px, y),0)
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)