# Rubrik is processing a string consisting of three types of symbols: A, B, and C.

# You are given a string S of length N. The system allows certain adjacent symbols to be swapped according to the following rules:

# Allowed Operations

# In one operation, you may perform exactly one of the following transformations:

# Replace an adjacent occurrence of AB with BA.
# Replace an adjacent occurrence of BC with CB.

# In other words:

# AB -> BA

# BC -> CB

# Only adjacent characters can participate in an operation.

# Your task is to determine the maximum number of operations that can be performed on the string.

# Example:
# Start: A B C C
# Positions 2,3 = "BC" -> flip to "CB"
# Op 1: A C B C
# Check for "AB" or "BC":
#   position1,2 = "AC" -> no match
#   position2,3 = "CB" -> no match
#   position3,4 = "BC" -> match!
# Positions 3,4 = "BC" -> flip to "CB"
# Op 2: A C C B
# Check for "AB" or "BC":
#   "AC" -> no, "CC" -> no, "CB" -> no
# No moves left. STUCK.
# Total operations = 2

# Time complexity: Total time  ≈ (number of distinct states) × (work per state)
            # ≈ O(2^N) × O(N²)
            # ≈ O(N² · 2^N)
            
# Because of the memo dictionary, we only ever do the "work per call" computation once per distinct string ever reached — repeated states are O(1) lookups after the first time.

# The problem is how many distinct strings can be reached. Every operation is a single adjacent swap, and the brute force explores every possible order 
# in which those swaps could be applied (not just the optimal order). Since:
# there can be multiple Bs, each independently choosing to drift left or right, or partially move and pause while other Bs move,
# and operations from different Bs can be freely interleaved in time,
# the number of distinct intermediate strings produced by all these interleavings grows very fast — 
# in the worst case, exponentially in N (roughly O(2^N) distinct reachable states for adversarial strings with many Bs each having real left/right choices

# Space complexity
# memo dictionary: up to O(2^N) distinct string keys, each of length O(N) → O(N · 2^N) space for the memo itself.
# Recursion stack: depth bounded by the max number of operations possible (each recursive call = one operation), 
# which is at most O(N²) (each of up to N Bs can cross at most N other characters) → O(N²) stack depth in the worst case.
# Overall space: O(N · 2^N), dominated by the memo table.

def max_operations_brute(s):
    memo = {}

    def solve(s):
        if s in memo:
            return memo[s]
        best = 0
        for i in range(len(s) - 1):
            if s[i:i+2] == 'AB': # 2 choices here therefore 2^N
                next_state = s[:i] + 'BA' + s[i+2:] # O(N)
                best = max(best, 1 + solve(next_state)) # we do 1+ as we have already found 1 pair in the form of "AB" or "BC"
            elif s[i:i+2] == 'BC':
                next_state = s[:i] + 'CB' + s[i+2:]
                best = max(best, 1 + solve(next_state))
        memo[s] = best
        return best

    return solve(s)

# Dry Run: Brute Force on s = "ABCC"
# CALL: solve("ABCC")
#   memo = {}                (empty, "ABCC" not in memo)
#   best = 0
#   s = "ABCC"   (indices: 0=A, 1=B, 2=C, 3=C)

#   Loop i from 0 to len(s)-1 = 3: i=0, i=1, i=2

#   i = 0:
#     s[0:2] = "AB"  -> MATCH (AB rule)
#     next_state = s[:0] + "BA" + s[2:]
#                = ""     + "BA" + "CC"
#                = "BACC"
#     -> RECURSE: solve("BACC")

#       CALL: solve("BACC")
#         memo = {}                ("BACC" not in memo)
#         best = 0
#         s = "BACC"   (indices: 0=B, 1=A, 2=C, 3=C)

#         Loop i from 0 to 2:
#         i = 0: s[0:2] = "BA" -> no match
#         i = 1: s[1:3] = "AC" -> no match
#         i = 2: s[2:4] = "CC" -> no match

#         No matches found. best stays 0.
#         memo = {"BACC": 0}
#         RETURN 0

#     back in solve("ABCC"), i=0:
#       best = max(best, 1 + 0) = max(0, 1) = 1

#   i = 1:
#     s[1:3] = "BC"  -> MATCH (BC rule)
#     next_state = s[:1] + "CB" + s[3:]
#                = "A"   + "CB" + "C"
#                = "ACBC"
#     -> RECURSE: solve("ACBC")

#       CALL: solve("ACBC")
#         memo = {"BACC": 0}      ("ACBC" not in memo)
#         best = 0
#         s = "ACBC"   (indices: 0=A, 1=C, 2=B, 3=C)

#         Loop i from 0 to 2:
#         i = 0: s[0:2] = "AC" -> no match
#         i = 1: s[1:3] = "CB" -> no match
#         i = 2: s[2:4] = "BC" -> MATCH (BC rule)
#           next_state = s[:2] + "CB" + s[4:]
#                      = "AC"  + "CB" + ""
#                      = "ACCB"
#           -> RECURSE: solve("ACCB")

#             CALL: solve("ACCB")
#               memo = {"BACC": 0}   ("ACCB" not in memo)
#               best = 0
#               s = "ACCB"   (indices: 0=A, 1=C, 2=C, 3=B)

#               Loop i from 0 to 2:
#               i = 0: s[0:2] = "AC" -> no match
#               i = 1: s[1:3] = "CC" -> no match
#               i = 2: s[2:4] = "CB" -> no match

#               No matches found. best stays 0.
#               memo = {"BACC": 0, "ACCB": 0}
#               RETURN 0

#           back in solve("ACBC"), i=2:
#             best = max(best, 1 + 0) = max(0, 1) = 1

#         (loop ends, i only went up to 2)
#         memo = {"BACC": 0, "ACCB": 0, "ACBC": 1}
#         RETURN 1

#     back in solve("ABCC"), i=1:
#       best = max(best, 1 + 1) = max(1, 2) = 2

#   i = 2:
#     s[2:4] = "CC" -> no match

#   (loop ends)
#   memo = {"BACC": 0, "ACCB": 0, "ACBC": 1, "ABCC": 2}
#   RETURN 2

# FINAL ANSWER: 2

# Optimized solution
# core logic:
# As and Cs never swap with each other, so their left-to-right order is frozen forever — a B can only move left through As or right through Cs, 
# and once it moves one way even once, its new neighbor blocks it from ever going the other way, so each B must pick one direction for its entire lifetime.

# Time: O(N)
# Space: O(N)

def max_operations_optimized_3loops(s):
    n = len(s)

    # Loop 1: for every position, count C's to the right before hitting an A
    right_c = [0] * n
    cnt = 0
    for i in range(n - 1, -1, -1):
        if s[i] == 'A':
            cnt = 0
        elif s[i] == 'C':
            cnt += 1
        right_c[i] = cnt

    # Loop 2: for every position, count A's to the left since the last C
    left_a = [0] * n
    cnt = 0
    for i in range(n):
        if s[i] == 'C':
            cnt = 0
        elif s[i] == 'A':
            cnt += 1
        left_a[i] = cnt

    # Loop 3: for every B, take the bigger of the two counts, sum it up
    ans = 0
    for i in range(n):
        if s[i] == 'B':
            ans += max(left_a[i], right_c[i])

    return ans

# Dry Run: s = "AABCBCC"
# s      = A A B C B C C
# index  = 0 1 2 3 4 5 6
# n = 7
# PASS 1 — building right_c (scanning RIGHT to LEFT)
# right_c = [0, 0, 0, 0, 0, 0, 0]   (initialized to all zeros)
# cnt = 0

# i = 6, s[6] = 'C'
#   s[i] == 'C' -> cnt += 1
#   cnt: 0 -> 1
#   right_c[6] = cnt = 1
#   right_c so far = [0, 0, 0, 0, 0, 0, 1]

# i = 5, s[5] = 'C'
#   s[i] == 'C' -> cnt += 1
#   cnt: 1 -> 2
#   right_c[5] = cnt = 2
#   right_c so far = [0, 0, 0, 0, 0, 2, 1]

# i = 4, s[4] = 'B'
#   s[i] is neither 'A' nor 'C' -> cnt unchanged
#   cnt stays = 2
#   right_c[4] = cnt = 2
#   right_c so far = [0, 0, 0, 0, 2, 2, 1]

# i = 3, s[3] = 'C'
#   s[i] == 'C' -> cnt += 1
#   cnt: 2 -> 3
#   right_c[3] = cnt = 3
#   right_c so far = [0, 0, 0, 3, 2, 2, 1]

# i = 2, s[2] = 'B'
#   s[i] is neither 'A' nor 'C' -> cnt unchanged
#   cnt stays = 3
#   right_c[2] = cnt = 3
#   right_c so far = [0, 0, 3, 3, 2, 2, 1]

# i = 1, s[1] = 'A'
#   s[i] == 'A' -> cnt = 0
#   cnt: 3 -> 0
#   right_c[1] = cnt = 0
#   right_c so far = [0, 0, 3, 3, 2, 2, 1]

# i = 0, s[0] = 'A'
#   s[i] == 'A' -> cnt = 0
#   cnt stays = 0
#   right_c[0] = cnt = 0
#   right_c so far = [0, 0, 3, 3, 2, 2, 1]

# FINAL right_c = [0, 0, 3, 3, 2, 2, 1]

# What this array means: right_c[i] = how many Cs sit to the right of position i, before hitting the next A (or the end of the string). Note it's only meaningful where s[i] == 'B' (positions 2 and 4) — the values at A/C positions are just leftover scratch values from the scan and are never used.

# PASS 2 — computing the answer (scanning LEFT to RIGHT)
# ans = 0
# cnt = 0   (tracks: A's seen since the last C, going left to right)

# i = 0, s[0] = 'A'
#   s[i] == 'A' -> cnt += 1
#   cnt: 0 -> 1
#   (not a 'B', so ans unchanged)
#   ans = 0

# i = 1, s[1] = 'A'
#   s[i] == 'A' -> cnt += 1
#   cnt: 1 -> 2
#   ans = 0

# i = 2, s[2] = 'B'
#   s[i] == 'B' -> ans += max(cnt, right_c[2])
#   cnt = 2, right_c[2] = 3
#   max(2, 3) = 3
#   ans: 0 -> 3
#   (meaning: this B is better off moving RIGHT through 3 C's than LEFT through 2 A's)

# i = 3, s[3] = 'C'
#   s[i] == 'C' -> cnt = 0
#   cnt: 2 -> 0
#   ans = 3

# i = 4, s[4] = 'B'
#   s[i] == 'B' -> ans += max(cnt, right_c[4])
#   cnt = 0, right_c[4] = 2
#   max(0, 2) = 2
#   ans: 3 -> 5
#   (meaning: this B has 0 A's before it since the last C, so it moves RIGHT through 2 C's)

# i = 5, s[5] = 'C'
#   s[i] == 'C' -> cnt = 0
#   cnt stays = 0
#   ans = 5

# i = 6, s[6] = 'C'
#   s[i] == 'C' -> cnt = 0
#   cnt stays = 0
#   ans = 5

# Loop ends.
# RETURN ans = 5