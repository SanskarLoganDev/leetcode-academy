# During a data integrity audit at Rubrik, every server is organized as part of a rooted dependency tree. The root server is numbered 1.
# Each server i stores a positive integer A[i], representing its integrity signature.
# A backup chain is defined as any path that starts at a server and ends at one of its descendants (possibly the same server). Thus, every backup chain follows only parent-to-child links.
# For reliability reasons, a backup chain is considered stable if the product of the integrity signatures of all servers on that chain is a perfect square.
# Given the dependency tree, determine the total number of stable backup chains.

# 1<=A[i]<=100
# 1<=N<=1000000

# Time complexity: O(depth), worst case: O(N^2)
# Worst case (a completely skewed tree, i.e., essentially a straight line — same shape as our example), depth can be O(N) for every node → O(N²) total.
# space: O(1)

import math
# The math.isqrt(n) function in Python returns the exact integer square root of a non-negative integer n
def is_perfect_square(x):
    r = math.isqrt(x)
    return r * r == x

def count_stable_chains_brute(n, parent, A):
    total = 0
    for v in range(1, n + 1):
        product = 1
        node = v
        while node != 0:
            product *= A[node]
            if is_perfect_square(product):
                total += 1
            node = parent[node]
    return total