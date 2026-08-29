# 87. Scramble String

# We can scramble a string s to get a string t using the following algorithm:

# If the length of the string is 1, stop.
# If the length of the string is > 1, do the following:
# Split the string into two non-empty substrings at a random index, i.e., if the string is s, divide it to x and y where s = x + y.
# Randomly decide to swap the two substrings or to keep them in the same order. i.e., after this step, s may become s = x + y or s = y + x.
# Apply step 1 recursively on each of the two substrings x and y.
# Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1, otherwise, return false.

# Example 1:

# Input: s1 = "great", s2 = "rgeat"
# Output: true
# Explanation: One possible scenario applied on s1 is:
# "great" --> "gr/eat" // divide at random index.
# "gr/eat" --> "gr/eat" // random decision is not to swap the two substrings and keep them in order.
# "gr/eat" --> "g/r / e/at" // apply the same algorithm recursively on both substrings. divide at random index each of them.
# "g/r / e/at" --> "r/g / e/at" // random decision was to swap the first substring and to keep the second substring in the same order.
# "r/g / e/at" --> "r/g / e/ a/t" // again apply the algorithm recursively, divide "at" to "a/t".
# "r/g / e/ a/t" --> "r/g / e/ a/t" // random decision is to keep both substrings in the same order.
# The algorithm stops now, and the result string is "rgeat" which is s2.
# As one possible scenario led s1 to be scrambled to s2, we return true.

# Example 2:

# Input: s1 = "abcde", s2 = "caebd"
# Output: false

# Example 3:

# Input: s1 = "a", s2 = "a"
# Output: true
 

# Constraints:

# s1.length == s2.length
# 1 <= s1.length <= 30
# s1 and s2 consist of lowercase English letters.

# Brute force solution
# Time complexity: 4^n, Each iteration of i makes up to 4 recursive calls
# Space Complexity: O(n²)

# Two things contribute to space here:

# Call stack depth: each recursive call strictly shrinks the string (since 1 ≤ i ≤ n-1), so the deepest possible chain of nested calls is bounded by O(n).
# Per-frame cost: each stack frame holds string slices (str1[0:i], str2[i:], etc.), and creating these slices costs O(n) time and space at that level (Python strings are immutable — slicing copies).

# Multiply depth × per-frame size: O(n) × O(n) = O(n²)

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        
        def solve(str1, str2):
            if str1==str2:
                return True

            res = False
            n = len(str1)
            for i in range(1, n):
                not_swapped = solve(str1[0:i], str2[0:i]) and solve(str1[i:], str2[i:])
                swapped = solve(str1[i:], str2[0:n-i]) and solve(str1[0:i], str2[n-i:])
                if swapped or not_swapped:
                    res = True
                    break
            return res

        return solve(s1,s2)
    
    
# Optimised solution, using memoization
# also removing res to avoid confusion and simply returning True or False
# Complexity

# Time: O(n⁴)
# Distinct subproblems are indexed by choosing a substring length, a start index into s1, and a start index into s2 → O(n³) states. 
# Each state does O(n) work in its loop (plus O(n) slicing/concatenation). Total: O(n³) × O(n) = O(n⁴).

# Space: O(n³)
# The memo dict holds up to O(n³) entries, each key itself O(n) long, dominating over the O(n) recursion stack depth.

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        memo = {}
        def solve(str1, str2):
            if str1==str2:
                return True

            key = str1+"_"+str2 # having a separator as "a" + "bc" is not "ab" + "c"
            if key in memo:
                return memo[key]

            n = len(str1)
            for i in range(1, n):
                not_swapped = solve(str1[0:i], str2[0:i]) and solve(str1[i:], str2[i:])
                swapped = solve(str1[i:], str2[0:n-i]) and solve(str1[0:i], str2[n-i:])
                if swapped or not_swapped:
                    memo[key] = True
                    return memo[key]
            memo[key] = False
            return memo[key] # if neither swapped nor not_swapped return True

        return solve(s1,s2)
    
# Dry Run
# CALL #1: solve("great","eatgr")
#     key="great_eatgr" not cached, n=5

#     i=1, split: x="g", y="reat"

#         not_swapped:
#             CALL #2: solve("g","e")
#                 n=1, loop empty -> memo["g_e"]=False -> return False
#             solve("reat","atgr") SKIPPED (short-circuit)
#             not_swapped = False

#         swapped:
#             CALL #3: solve("reat","eatg")
#                 n=4

#                 i=1, split: x="r", y="eat"
#                     not_swapped:
#                         CALL #4: solve("r","e")  # current words are "reat" "eatg"
#                             n=1, loop empty -> memo["r_e"]=False -> return False
#                         solve("eat","atg") SKIPPED
#                         not_swapped = False
#                     swapped:
#                         CALL #5: solve("eat","eat") # current words are "reat" "eatg"
#                             str1==str2 -> return True
#                         CALL #6: solve("r","g")
#                             n=1, loop empty -> memo["r_g"]=False -> return False
#                         swapped = True and False = False
#                     i=1 result: both False -> continue

#                 i=2, split: x="re", y="at"
#                     not_swapped:
#                         CALL #7: solve("re","ea")
#                             n=2
#                             i=1, split: x="r", y="e"
#                                 not_swapped:
#                                     CALL #8: solve("r","e")
#                                         memo hit "r_e" -> False
#                                     solve("e","a") SKIPPED
#                                     not_swapped = False
#                                 swapped:
#                                     CALL #9: solve("e","e")
#                                         str1==str2 -> return True
#                                     CALL #10: solve("r","a")
#                                         n=1, loop empty -> memo["r_a"]=False -> return False
#                                     swapped = True and False = False
#                                 i=1 result: both False -> continue
#                             loop ends (n=2, only i=1 exists) -> memo["re_ea"]=False -> return False
#                         <- back in CALL #3, i=2
#                         not_swapped = False (CALL #7's result) and SKIPPED solve("at","tg")
#                         not_swapped = False
#                     swapped:
#                         CALL #11: solve("at","ea")
#                             n=2
#                             i=1, split: x="a", y="t"
#                                 not_swapped:
#                                     CALL #12: solve("a","e")
#                                         n=1, loop empty -> memo["a_e"]=False -> return False
#                                     solve("t","a") SKIPPED
#                                     not_swapped = False
#                                 swapped:
#                                     CALL #13: solve("t","e")
#                                         n=1, loop empty -> memo["t_e"]=False -> return False
#                                     solve("a","a") SKIPPED
#                                     swapped = False
#                                 i=1 result: both False -> continue
#                             loop ends -> memo["at_ea"]=False -> return False
#                         <- back in CALL #3, i=2
#                         swapped = False
#                     i=2 result: both False -> continue

#                 i=3, split: x="rea", y="t"
#                     not_swapped:
#                         CALL #14: solve("rea","eat")
#                             n=3
#                             i=1, split: x="r", y="ea"
#                                 not_swapped:
#                                     CALL #15: solve("r","e")
#                                         memo hit "r_e" -> False
#                                     solve("ea","at") SKIPPED
#                                     not_swapped = False
#                                 swapped:
#                                     CALL #16: solve("ea","ea")
#                                         str1==str2 -> return True
#                                     CALL #17: solve("r","t")
#                                         n=1, loop empty -> memo["r_t"]=False -> return False
#                                     swapped = True and False = False
#                                 i=1 result: both False -> continue
#                             i=2, split: x="re", y="a"
#                                 not_swapped:
#                                     CALL #18: solve("re","ea")
#                                         memo hit "re_ea" -> False
#                                     solve("a","t") SKIPPED
#                                     not_swapped = False
#                                 swapped:
#                                     CALL #19: solve("a","e")
#                                         memo hit "a_e" -> False
#                                     solve("re","at") SKIPPED
#                                     swapped = False
#                                 i=2 result: both False -> continue
#                             loop ends (n=3, i went 1,2) -> memo["rea_eat"]=False -> return False
#                         <- back in CALL #3, i=3
#                         not_swapped = False
#                     swapped:
#                         CALL #20: solve("t","e")
#                             memo hit "t_e" -> False
#                         solve("rea","atg") SKIPPED
#                         swapped = False
#                     i=3 result: both False -> continue

#                 loop ends (n=4, i went 1,2,3) -> memo["reat_eatg"]=False -> return False
#         <- back in CALL #1, i=1
#         swapped = False (CALL #3's result) and SKIPPED solve("g","r")
#         swapped = False

#     i=1 result: not_swapped=False, swapped=False -> continue

#     i=2, split: x="gr", y="eat"

#         not_swapped:
#             CALL #21: solve("gr","ea")
#                 n=2
#                 i=1, split: x="g", y="r"
#                     not_swapped:
#                         CALL #22: solve("g","e")
#                             memo hit "g_e" -> False
#                         solve("r","a") SKIPPED
#                         not_swapped = False
#                     swapped:
#                         CALL #23: solve("r","e")
#                             memo hit "r_e" -> False
#                         solve("g","a") SKIPPED
#                         swapped = False
#                     i=1 result: both False -> continue
#                 loop ends -> memo["gr_ea"]=False -> return False
#         <- back in CALL #1, i=2
#         not_swapped = False (CALL #21's result) and SKIPPED solve("eat","tgr")
#         not_swapped = False

#         swapped:
#             CALL #24: solve("eat","eat")
#                 str1==str2 -> return True
#             CALL #25: solve("gr","gr")
#                 str1==str2 -> return True
#             swapped = True and True = True

#     i=2 result: swapped=True -> res=True, BREAK

#     memo["great_eatgr"] = True
#     return True

# FINAL RESULT: True

# Total: 25 calls, 13 unique memo entries. Notice "r_e" gets reused 3 times (calls #8, #15, #23), and "re_ea", "g_e", "a_e", "t_e" each get reused once — none of these are recomputed once cached.

