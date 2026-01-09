# 17. Letter Combinations of a Phone Number
# Neetcode 150 (Important)

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# https://assets.leetcode.com/uploads/2022/03/15/1200px-telephone-keypad2svg.png
 
# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# Example 2:

# Input: digits = "2"
# Output: ["a","b","c"]
 

# Constraints:

# 1 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].

# Solution using Backtracking
# Time complexity: O(N*4^N) where N is length of digits; because in the worst case, each digit can map to 4 letters (like digit '7' or '9').
# Space complexity: O(N) for the recursion stack and temporary storage

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []
        temp = []
        def backtrack(idx): # here idx is the index of the digit we are processing
            if idx>=len(digits):
                key = "".join(temp.copy())
                res.append(key)
                return
            ch = digits[idx] # get the digit at index idx
            s = letter[ch] # get the letters mapped to the digit
            for i in range(len(s)): # here i is the index of the letter mapped to the digit
                temp.append(s[i])
                backtrack(idx+1) # here er put idx+1 and not i+1 because we are moving to the next digit
                temp.pop()
        
        backtrack(0)
        return res


# Brute force without backtracking
# Time complexity: O(N*4^N) where N is length of digits
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []
        temp = []
        if len(digits)==1:
            return list(letter[digits])

        if len(digits)==2:
            res = []
            for i in letter[digits[0]]:
                for j in letter[digits[1]]:
                    temp = ""
                    temp+=i
                    temp+=j
                    res.append(temp)
            return res

        if len(digits)==3:
            res = []
            for i in letter[digits[0]]:
                for j in letter[digits[1]]:
                    for k in letter[digits[2]]:
                        temp = ""
                        temp+=i
                        temp+=j
                        temp+=k
                        res.append(temp)
            return res

        if len(digits)==4:
            res = []
            for i in letter[digits[0]]:
                for j in letter[digits[1]]:
                    for k in letter[digits[2]]:
                        for l in letter[digits[3]]:
                            temp = ""
                            temp+=i
                            temp+=j
                            temp+=k
                            temp+=l
                            res.append(temp)
            return res

# Below is a clear dry run for `digits = "279"`.

# ### Setup

# * `digits = "279"`
# * Mapping:

#   * `'2' -> "abc"`
#   * `'7' -> "pqrs"`
#   * `'9' -> "wxyz"`
# * `temp` holds the current partial combination.
# * `idx` tells which digit we are currently expanding.

# The recursion builds combinations in this order:

# * pick one letter for `'2'`
# * then one for `'7'`
# * then one for `'9'`
# * once `idx == 3` (len("279")), join `temp` and append to `res`

# ---

# ## Call trace (structured)

# ### Start

# `backtrack(0)`, `temp = []`
# `idx=0`, `ch='2'`, `s="abc"`

# ---

# ## Branch for `'2' = 'a'`

# * `temp = ['a']`
# * call `backtrack(1)`

#   * `idx=1`, `ch='7'`, `s="pqrs"`

# ### `'7' = 'p'`

# * `temp = ['a','p']`
# * call `backtrack(2)`

#   * `idx=2`, `ch='9'`, `s="wxyz"`

# Now loop over `"wxyz"`:

# * add `'w'`: `temp=['a','p','w']` → `backtrack(3)` → idx==3 ⇒ append `"apw"`

# * pop `'w'`: `temp=['a','p']`

# * add `'x'`: `temp=['a','p','x']` → append `"apx"`

# * pop → `temp=['a','p']`

# * add `'y'`: `temp=['a','p','y']` → append `"apy"`

# * pop → `temp=['a','p']`

# * add `'z'`: `temp=['a','p','z']` → append `"apz"`

# * pop → `temp=['a','p']`

# Done with `'9'` letters, return to `idx=1`, `temp=['a']`

# ### `'7' = 'q'`

# * `temp=['a','q']` → `backtrack(2)` over `"wxyz"`:

#   * append `"aqw", "aqx", "aqy", "aqz"`
#     Return, `temp=['a']`

# ### `'7' = 'r'`

# * `temp=['a','r']` → `backtrack(2)`:

#   * append `"arw", "arx", "ary", "arz"`
#     Return, `temp=['a']`

# ### `'7' = 's'`

# * `temp=['a','s']` → `backtrack(2)`:

#   * append `"asw", "asx", "asy", "asz"`
#     Return, `temp=['a']`

# Done with `'7'`, return to `idx=0`, pop `'a'` → `temp=[]`

# ---

# ## Branch for `'2' = 'b'`

# Same pattern, but starting with `'b'`:

# You will append (in order):

# * `"bpw", "bpx", "bpy", "bpz"`
# * `"bqw", "bqx", "bqy", "bqz"`
# * `"brw", "brx", "bry", "brz"`
# * `"bsw", "bsx", "bsy", "bsz"`

# ---

# ## Branch for `'2' = 'c'`

# Append:

# * `"cpw", "cpx", "cpy", "cpz"`
# * `"cqw", "cqx", "cqy", "cqz"`
# * `"crw", "crx", "cry", "crz"`
# * `"csw", "csx", "csy", "csz"`

# ---

# ## Final result size

# * `'2'` gives 3 choices
# * `'7'` gives 4 choices
# * `'9'` gives 4 choices
#   Total = (3 \times 4 \times 4 = 48) combinations in `res`.

# ---

# ## First few and last few results (to confirm order)

# **First 8**:
# `apw, apx, apy, apz, aqw, aqx, aqy, aqz`

# **Last 4**:
# `csw, csx, csy, csz`

# ---

# ### Important visualization takeaway

# At any moment:

# * `temp` represents the current partial word
# * `append` = choose a letter
# * `pop` = undo choice (backtrack) so you can try the next letter



            