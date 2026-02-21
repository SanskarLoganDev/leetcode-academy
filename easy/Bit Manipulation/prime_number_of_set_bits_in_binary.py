# 762. Prime Number of Set Bits in Binary Representation

# Given two integers left and right, return the count of numbers in the inclusive range [left, right] having a prime number of set bits in their binary representation.

# Recall that the number of set bits an integer has is the number of 1's present when written in binary.

# For example, 21 written in binary is 10101, which has 3 set bits.
 

# Example 1:

# Input: left = 6, right = 10
# Output: 4
# Explanation:
# 6  -> 110 (2 set bits, 2 is prime)
# 7  -> 111 (3 set bits, 3 is prime)
# 8  -> 1000 (1 set bit, 1 is not prime)
# 9  -> 1001 (2 set bits, 2 is prime)
# 10 -> 1010 (2 set bits, 2 is prime)
# 4 numbers have a prime number of set bits.

# Example 2:

# Input: left = 10, right = 15
# Output: 5
# Explanation:
# 10 -> 1010 (2 set bits, 2 is prime)
# 11 -> 1011 (3 set bits, 3 is prime)
# 12 -> 1100 (2 set bits, 2 is prime)
# 13 -> 1101 (3 set bits, 3 is prime)
# 14 -> 1110 (3 set bits, 3 is prime)
# 15 -> 1111 (4 set bits, 4 is not prime)
# 5 numbers have a prime number of set bits.
 

# Constraints:

# 1 <= left <= right <= 106
# 0 <= right - left <= 104

# time complexity O(N*log(right)) where N is the number of integers in the range [left, right] and log(right) is the time taken to convert an integer to binary and count the set bits
# space complexity O(1)
import math
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def isBitPrime(n):
            bit = bin(n)[2:]
            c = 0
            for b in bit:
                if b=="1":
                    c+=1
            if c<=1:
                return False
            val = math.floor(math.sqrt(c))
            for i in range(2, val+1):
                if c%i==0:
                    return False
            return True


        count = 0    
        for i in range(left, right+1):
            if isBitPrime(i):
                count+=1
        return count

# time complexity O(N) 
# space complexity O(1) since the number of set bits in an integer is at most 32 (for 32-bit integers) and we are using a constant amount of space to count the set bits and check for primality
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = [2,3,5,7,11,13,17,19,23,29,31] # list of prime numbers up to 31 (since the maximum number of set bits in an integer up to 10^6 is 20)
        def isBitPrime(n):
            if n in primes:
                return True
            return False

        count = 0    
        for i in range(left, right+1):
            cnt = 0
            x = i
            while x: # constant number of iterations since the maximum number of set bits is 32
                x = x & x-1 # and of number ans number-1 will remove the last set bit from the number
                cnt+=1
            if isBitPrime(cnt):
                count+=1
        return count