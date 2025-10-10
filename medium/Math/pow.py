# 50. Pow(x, n)
# Neetcode 150 (Important)

# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

# Example 1:

# Input: x = 2.00000, n = 10
# Output: 1024.00000

# Example 2:

# Input: x = 2.10000, n = 3
# Output: 9.26100

# Example 3:

# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25
 
# Constraints:

# -100.0 < x < 100.0
# -231 <= n <= 231-1
# n is an integer.
# Either x is not zero or n > 0.
# -104 <= xn <= 104

# time complexity: O(1)
# space complexity: O(1)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n
    
# time complexity: O(log n)
# space complexity: O(log n) due to recursion stack    
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n<0: # handle negative power
            return self.myPow(1/x, -n)
        if n%2==0: # even power
            return self.myPow(x*x, n/2)
        else: # odd power
            return x*self.myPow(x*x, (n-1)/2)
