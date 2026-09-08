# 3870. Count Commas in Range

# You are given an integer n.

# Return the total number of commas used when writing all integers from [1, n] (inclusive) in standard number formatting.

# In standard formatting:

# A comma is inserted after every three digits from the right.
# Numbers with fewer than 4 digits contain no commas.
 

# Example 1:
# Input: n = 1002
# Output: 3
# Explanation:
# The numbers "1,000", "1,001", and "1,002" each contain one comma, giving a total of 3.

# Example 2:
# Input: n = 998
# Output: 0
# Explanation:
# All numbers from 1 to 998 have fewer than four digits. Therefore, no commas are used.

# Constraints:

# 1 <= n <= 105

# Brute force solution
# Time complexity: O(NlogN)
# Space complexity: O(logN)
class Solution:
    def countCommas(self, n: int) -> int:
        digits = len(str(n))
        if digits<=3:
            return 0
        count = 0
        for num in range(1000, n+1): # roughly O(N)
            number = len(str(num)) # a number N will have approx logN digits, therefore converting them to string will take logN time and logN space
            if number%3==0:
                count+=(number//3 - 1)
            else:
                count+= number//3
        return count
    
# Optimised solution
# Time complexity: O(logN)
# Space complexity: O(logN)

class Solution:
    def countCommas(self, n: int) -> int:
        digits = len(str(n)) # time: O(logN), space: O(logN)
        if digits<=3:
            return 0
        return n - 1000 + 1