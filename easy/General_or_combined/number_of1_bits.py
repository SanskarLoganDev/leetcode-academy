# 191. NUMBER OF 1 BITS

# Given a positive integer n, write a function that returns the number of 
# set bits
#  in its binary representation (also known as the Hamming weight).

 

# Example 1:

# Input: n = 11

# Output: 3

# Explanation:

# The input binary string 1011 has a total of three set bits.

# Example 2:

# Input: n = 128

# Output: 1

# Explanation:

# The input binary string 10000000 has a total of one set bit.

def hammingWeight(n):
        """
        :type n: int
        :rtype: int
        """
        s1 = bin(n)
        s2 = s1[2:]
        return s2.count('1')
    
print(hammingWeight(11))