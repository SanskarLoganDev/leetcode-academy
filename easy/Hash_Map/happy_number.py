# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

 

# Example 1:

# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
# Example 2:

# Input: n = 2
# Output: false

def isHappy(n):
    if n==1:
        return True
    seen = set()
    temp = n
    while temp!=1:
        print(seen)
        if temp in seen:  # check if the number is already in seen, the numbers which are not happy numbers, usually follow a pattern
            return False
        seen.add(temp)
        sum = 0
        while temp:
            digit = temp%10
            sum+=digit**2
            temp//=10
        temp = sum
    return True

print(isHappy(4))
        
            