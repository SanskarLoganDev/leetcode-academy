# 3606. Coupon Code Validator

# You are given three arrays of length n that describe the properties of n coupons: code, businessLine, and isActive. The ith coupon has:

# code[i]: a string representing the coupon identifier.
# businessLine[i]: a string denoting the business category of the coupon.
# isActive[i]: a boolean indicating whether the coupon is currently active.
# A coupon is considered valid if all of the following conditions hold:

# code[i] is non-empty and consists only of alphanumeric characters (a-z, A-Z, 0-9) and underscores (_).
# businessLine[i] is one of the following four categories: "electronics", "grocery", "pharmacy", "restaurant".
# isActive[i] is true.
# Return an array of the codes of all valid coupons, sorted first by their businessLine in the order: "electronics", "grocery", "pharmacy", "restaurant", and then by code in lexicographical (ascending) order within each category.

# Example 1:

# Input: code = ["SAVE20","","PHARMA5","SAVE@20"], businessLine = ["restaurant","grocery","pharmacy","restaurant"], isActive = [true,true,true,true]

# Output: ["PHARMA5","SAVE20"]

# Explanation:

# First coupon is valid.
# Second coupon has empty code (invalid).
# Third coupon is valid.
# Fourth coupon has special character @ (invalid).

# Example 2:

# Input: code = ["GROCERY15","ELECTRONICS_50","DISCOUNT10"], businessLine = ["grocery","electronics","invalid"], isActive = [false,true,true]

# Output: ["ELECTRONICS_50"]

# Explanation:

# First coupon is inactive (invalid).
# Second coupon is valid.
# Third coupon has invalid business line (invalid).
 

# Constraints:

# n == code.length == businessLine.length == isActive.length
# 1 <= n <= 100
# 0 <= code[i].length, businessLine[i].length <= 100
# code[i] and businessLine[i] consist of printable ASCII characters.
# isActive[i] is either true or false.


from typing import List

# Time complexity: O(n log n + n.L)  where n is the number of coupons and L is the maximum length of a coupon code.
# Space complexity: O(n) for storing the valid coupons.
class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        n = len(code)
        res = []
        bline = {"electronics": [], "grocery":[], "pharmacy":[], "restaurant":[]}
        for i in range(n): # iterate through all coupons: O(n), overall O(n.L)
            flag = True
            if not code[i]:
                flag = False
            for j in range(len(code[i])): # iterate through each character of the coupon code: O(L)
                if code[i][j].isalnum()==False and code[i][j]!="_": # check for alphanumeric and underscore
                    flag=False
            if businessLine[i] not in bline:
                flag=False
            if not isActive[i]:
                flag = False 
            
            if flag:
                bline[businessLine[i]].append(code[i])
        # print(bline)
        for key in bline: # iterate through the business lines in the required order: O(1) as there are only 4 business lines
            if bline[key]:
                bline[key].sort() # sort the coupon codes lexicographically: O(n log n) where in worst case all coupons belong to the same business line
                res.extend(bline[key])

        # print(bline)
        return res