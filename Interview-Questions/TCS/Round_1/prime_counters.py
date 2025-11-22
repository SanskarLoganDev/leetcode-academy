# Given a number N, let CP(N) denote the  number of prime numbers between 1 and N (both inclusive).
# We call N a prime counter if CP(N) is prime (N need not be a prime number).

# For example, CP(3) = 2, CP(10) = 4, CP(11) = 5.

# Input format: An integer T, number of test cases T lines each containing two positive integers L, R separated by space.

# Output format: For each test case, print the count of prime counters between L and R (both inclusive) in a new line.

# Note: We iterate only up to the square root of n because if n has any divisor greater than its square root, 
# there must also be a corresponding divisor smaller than the square root. So, checking beyond sqrt(n) is unnecessary and would only waste computation.
def is_prime(n):
    if n<=1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def prime_counters(l, r):
    d = {}
    prime = 0
    for i in range(1, r+1):
        if is_prime(i):
            prime += 1
        d[i] = prime
    p_counter = 0
    for key, value in d.items():
        if key<l:
            continue
        if is_prime(value):
            p_counter+=1
    return p_counter

print(prime_counters(2, 10))