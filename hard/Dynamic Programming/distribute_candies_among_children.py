# 2928, 2929, 2927. Distribute Candies Among Children I

# You are given two positive integers n and limit.

# Return the total number of ways to distribute n candies among 3 children such that no child gets more than limit candies.

# Example 1:

# Input: n = 5, limit = 2
# Output: 3
# Explanation: There are 3 ways to distribute 5 candies such that no child gets more than 2 candies: (1, 2, 2), (2, 1, 2) and (2, 2, 1).

# Example 2:

# Input: n = 3, limit = 3
# Output: 10
# Explanation: There are 10 ways to distribute 3 candies such that no child gets more than 3 candies: (0, 0, 3), (0, 1, 2), (0, 2, 1), (0, 3, 0), (1, 0, 2), (1, 1, 1), (1, 2, 0), (2, 0, 1), (2, 1, 0) and (3, 0, 0).
 

# 2928) Constraints:

# 1 <= n <= 50
# 1 <= limit <= 50

# 2929) Constraints:

# 1 <= n <= 106
# 1 <= limit <= 106

# 2027) Constraints:

# 1 <= n <= 108
# 1 <= limit <= 108

# Time: O(min(limit,n)³) — three levels of recursion (countChild goes 0→1→2→3), each branching up to limit+1 ways in the worst case. 
# Space: O(1) extra, since recursion depth is fixed at exactly 3 regardless of n or limit.
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def solve(countChild, n_candy):
            if countChild==3:
                if n_candy==0:
                    return 1
                else:
                    return 0
        
            ways = 0
            for assign in range(min(limit, n_candy)+1): # cannot assign more than limit
                ways+=solve(countChild+1, n_candy-assign)
            return ways
        return solve(0, n)
    
# Dry run: n=5, limit=2

# We're distributing 5 candies among 3 children, each getting between 0 and 2 candies (inclusive), 
# summing to exactly 5.

# Call solve(0, 5) — child 0, 5 candies left to distribute

# Loop range: min(2,5)+1 = 3 → assign ∈ {0,1,2}
# Branch assign=0 → solve(1, 5)
# Branch assign=1 → solve(1, 4)
# Branch assign=2 → solve(1, 3)

# Let's resolve each branch fully before summing.

# Branch: solve(1, 5) — child 1, 5 candies left

# Loop range: min(2,5)+1 = 3 → assign ∈ {0,1,2}
# assign=0 → solve(2,5)
# assign=1 → solve(2,4)
# assign=2 → solve(2,3)

# At countChild=2, this is the last child — whatever it's given must exactly use up all remaining candy, 
# or the distribution fails.

# solve(2,5): range min(2,5)+1=3 → tries assign∈{0,1,2}, calling solve(3,5), solve(3,4), solve(3,3) — all have countChild==3 with n_candy≠0 → each returns 0. Sum = 0
# solve(2,4): similarly tries solve(3,4), solve(3,3), solve(3,2) — none hit n_candy==0. Sum = 0
# solve(2,3): tries solve(3,3), solve(3,2), solve(3,1) — none hit 0. Sum = 0

# So solve(1,5) = 0 + 0 + 0 = 0 — makes sense: with 5 candies left and only 2 children remaining (max 2 each = 4 total), there's no way to use up 5 candies with just 2 children capped at 2 each. Correctly returns 0.

# Branch: solve(1, 4) — child 1, 4 candies left

# Loop range: min(2,4)+1=3 → assign ∈ {0,1,2}
# assign=0 → solve(2,4) = 0 (already computed above)
# assign=1 → solve(2,3) = 0 (already computed above)
# assign=2 → solve(2,2) — new, let's resolve:
# Range min(2,2)+1=3 → assign∈{0,1,2}, calling solve(3,2)→0, solve(3,1)→0, solve(3,0) → countChild==3 and n_candy==0 → returns 1
# Sum = 0+0+1 = 1

# So solve(1,4) = 0 + 0 + 1 = 1

# Interpretation: this represents the distribution where child 0 got 1, child 1 got 2, child 2 got 2 → 1+2+2=5 ✅ — exactly one valid way through this branch.

# Branch: solve(1, 3) — child 1, 3 candies left

# Loop range: min(2,3)+1=3 → assign ∈ {0,1,2}
# assign=0 → solve(2,3) = 0 (already computed)
# assign=1 → solve(2,2) = 1 (already computed)
# assign=2 → solve(2,1) — new, let's resolve:
# Range min(2,1)+1=2 → assign∈{0,1}, calling solve(3,1)→0, solve(3,0)→1
# Sum = 0+1 = 1

# So solve(1,3) = 0 + 1 + 1 = 2

# Interpretation: two valid distributions pass through here — child 0 got 2, then either (child1=1,child2=2) or (child1=2,child2=1) → 2+1+2=5 and 2+2+1=5, both valid.

# Using iteration
# Time complexity = O(N^3)
# Space complexity = O(1)

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ways = 0
        for ch1 in range(min(n, limit)+1):
            for ch2 in range(min(n-ch1, limit)+1):
                for ch3 in range(min(n-ch1-ch2, limit)+1):
                    if n-ch1-ch2-ch3==0:
                        ways+=1
        return ways
    
# Using iteration
# Time complexity = O(N^2)
# Space complexity = O(1)    
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ways = 0
        for ch1 in range(min(n, limit)+1):
            for ch2 in range(min(n-ch1, limit)+1):
                ch3 = n-ch1-ch2
                if ch3<=limit and n-ch1-ch2-ch3==0:
                    ways+=1
        return ways
    
# Further optimised, video: https://www.youtube.com/watch?v=eL_3cDp0zjE
# Time complexity: O(N)
# space complexity: O(1)

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ways = 0
        min_ch1 = max(0,n-2*limit) # we are taking max with 0 as number of candies child 1 can have, 
        # cannot be less than 0. We have 2*limit by giving limit candies to child 2 and 3, 
        # therefore minimizing the number of candies child 1 can have
        max_ch1 = min(n, limit) # cannot have more than limit
        for ch1 in range(min_ch1, max_ch1+1):
            N = n - ch1
            min_ch2 = max(0, N - limit) # we take max, as we cannot have less that 0 candies assigned
            max_ch2 = min(N, limit)     # we take max of N and limit as if candies are 5 and limit is 100, you can still only give maximum of 5 candies
            ways+= max_ch2 - min_ch2 + 1

        return ways
    
    
# Most Optimised solution
# Time complexity: O(1)
# Space complexity: O(1)

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def calc(val):
            if val < 0:
                return 0
            return (val+2)*(val+1)//2
        
        total = calc(n)
        extra = 3*calc(n - 1*(limit+1)) # got deleted
        double_extra = 3*calc(n - 2*(limit+1)) # extra part got deleted, needs to bb added
        common_extra = 1*calc(n - 3*(limit+1)) # common extra part that got added in double_extra, needs to be deleted
        return total - extra + double_extra - common_extra
    

# DETAILED EXPLANATION
# Part 1: 
# What does calc(val) compute? it essentially computes: (n+2) C 2 (Combinations), as according to stars and bars theorem
# the universal or total set (possible ways without limit) would be (n+2) C 2
# python
# def calc(val):
#     if val < 0:
#         return 0
#     return ((val+1)*(val+2)) // 2

# This counts: "in how many ways can val identical candies be split among 3 children, with no upper limit on any child?" 
# (This is exactly the "no limit" question from your last message — we found calc(3) = 10.)

# Part 2: Why do we need extra, doubleextra, common?

# calc(n) counts every way to split n candies among 3 children with no cap. But we do have a cap — each child can get at most limit. So we need to subtract off all the distributions where some child got more than limit.

# This is where inclusion-exclusion comes in — a technique for correctly subtracting overlapping "bad" cases without double-subtracting or under-subtracting.

# Define three "violation" sets:

# A = distributions where child 1 got more than limit
# B = distributions where child 2 got more than limit
# C = distributions where child 3 got more than limit

# We want: total - (distributions where at least one child violates the limit).

# Part 3:
# The problem in plain terms

# We want: "how many ways to give 3 children some candies, totaling exactly n, where no child gets more than limit?"

# We already know how to count without the "no more than limit" rule — that's calc(n). 
# The rest of the formula exists purely to subtract out the bad cases (where someone got too much) — but doing that subtraction correctly is trickier than it first looks. 
# Let's see why with real numbers.

# Example: n=8, limit=3

# Step 1 — count everything, no limit:

# total = calc(8) = (9×10)/2 = 45

# So there are 45 ways to split 8 candies among 3 children if nobody has a cap.

# Step 2 — figure out how many of those 45 are "bad" (some child got more than 3).

# Counting "child 1 got too much" on its own

# If child 1 got more than 3 (i.e., at least 4), here's a neat trick: hand child 1 their mandatory 4 candies right away, 
# then freely distribute whatever's left among all three children (with no cap, since we've already accounted for the "at least 4" requirement).

# Candies left after giving child 1 their 4: 8 - 4 = 4. So:

# ways where child 1 got ≥4  =  calc(4)  =  (5×6)/2  =  15

# By the same logic, "child 2 got ≥4" also has exactly 15 ways, and "child 3 got ≥4" also has 15 ways 
# (nothing special about which child — the counting is identical either way).

# This is exactly what extra computes:

# extra = 3 * calc(8 - 4) = 3 * calc(4) = 3 * 15 = 45

# It's just adding up "child 1 bad" + "child 2 bad" + "child 3 bad" = 15 + 15 + 15 = 45.

# Here's the problem — some distributions get counted twice

# Consider the distribution (4, 4, 0) — child 1 got 4, child 2 got 4, child 3 got 0. Total = 8. ✓

# This distribution shows up inside "child 1 got ≥4" (since child 1 has 4). It also shows up inside "child 2 got ≥4" (since child 2 also has 4).

# So when we computed extra = 15 + 15 + 15 = 45, this single distribution (4,4,0) got counted twice — once in the "child 1 bad" pile of 15, 
# and once again in the "child 2 bad" pile of 15.

# If we just did total - extra = 45 - 45 = 0, we'd have subtracted (4,4,0) out twice, when it should only be subtracted once. We over-corrected. 
# We need to add back one copy of every distribution that got double-subtracted.

# Counting "both child 1 AND child 2 got too much at the same time"

# Same trick as before, but now give the mandatory 4 candies to both child 1 and child 2 upfront: 4 + 4 = 8 candies handed out immediately. 
# What's left to freely distribute: 8 - 8 = 0.

# ways where child 1 ≥4 AND child 2 ≥4  =  calc(0)  =  (1×2)/2  =  1

# That single way is exactly (4,4,0) — the third child is forced to get 0, since there's nothing left.

# There are 3 different pairs of children we could pick to both be "bad" simultaneously: 
# (child1&child2), (child1&child3), (child2&child3). Each pair, by the same reasoning, gives calc(8 - 2×4) = calc(0) = 1 way. 
# So:
# doubleextra = 3 * calc(8 - 2*(limit+1)) = 3 * calc(0) = 3 * 1 = 3

# This represents the 3 distributions (4,4,0), (4,0,4), (0,4,4) — each one is a case where two children simultaneously went over the limit, 
# and each one was the "double-counted" victim we identified above. Adding these 3 back in fixes the over-subtraction.

# What about all three going over at once?

# If all three children needed at least 4 candies each, that's 4+4+4 = 12 candies minimum — but we only have 8 total. Impossible.

# common = calc(8 - 3*(limit+1)) = calc(8-12) = calc(-4) = 0

# calc returns 0 for negative input specifically to represent "impossible, zero ways" — so common = 0 here, 
# correctly signaling that no distribution has all three children simultaneously over the limit. 
# (This term exists in the formula for the general case — with a larger n, it could become nonzero, and we'd need to subtract it back out again, 
# since it would have been added too many times by the doubleextra step. 
# This alternating add/subtract pattern is the essence of the technique — each term corrects the over/under-correction of the previous one.)

# Putting it together
# answer = total - extra + doubleextra - common
#        = 45   -  45   +    3        -   0
#        = 3

# Let's sanity check this by hand. With n=8, limit=3, what distributions are actually valid (each child ≤ 3, summing to 8)? The maximum possible with everyone capped at 3 is 3+3+3=9, so we need to distribute 8, which is "9 minus 1" — meaning exactly one child has one less than the max. The valid distributions are the arrangements of {3, 3, 2}:

# (3,3,2), (3,2,3), (2,3,3)

# That's 3 valid distributions — matching our computed answer exactly. ✅

# The core intuition to hold onto
# total: count everything, ignore the limit completely.
# extra: subtract every case where at least one specific child went over — but this accidentally subtracts twice whenever two children both went over simultaneously.
# doubleextra: add back one copy for every pair of children that both went over together, correcting that double-subtraction.
# common: if it were ever possible for all three to go over simultaneously, that case would've been added back too many times by doubleextra, so we subtract it once more to balance it out.

# Each term is just "give away the mandatory excess to the guilty child(ren) upfront, then freely count what's left with calc" — and the alternating +/- pattern exists purely to make sure every "bad" distribution gets counted (and removed) exactly once, no matter how many children it happens to violate the limit for simultaneously.