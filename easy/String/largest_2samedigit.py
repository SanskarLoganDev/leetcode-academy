# 2264. Largest 3-Same-Digit Number in String

# You are given a string num representing a large integer. An integer is good if it meets the following conditions:

# It is a substring of num with length 3.
# It consists of only one unique digit.
# Return the maximum good integer as a string or an empty string "" if no such integer exists.

# Note:

# A substring is a contiguous sequence of characters within a string.
# There may be leading zeroes in num or a good integer.
 

# Example 1:

# Input: num = "6777133339"
# Output: "777"
# Explanation: There are two distinct good integers: "777" and "333".
# "777" is the largest, so we return "777".
# Example 2:

# Input: num = "2300019"
# Output: "000"
# Explanation: "000" is the only good integer.
# Example 3:

# Input: num = "42352338"
# Output: ""
# Explanation: No substring of length 3 consists of only one unique digit. Therefore, there are no good integers.
 
# Constraints:

# 3 <= num.length <= 1000
# num only consists of digits.

# time complexity: O(n), a bit more complex but generic solution
# space complexity: O(1)

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        l = 0
        r = l+2
        max_num = float("-inf")
        while r<len(num):
            if num[l]==num[r]==num[l+1]:
                max_num = max(max_num, int(num[l:r+1]))
            l+=1
            r+=1
        if max_num==0:
            return "000"
        elif max_num>0:
            return str(max_num)
        else:
            return ""

# time complexity: O(n), a bit less generic solution
# space complexity: O(1)

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        repeats = ["999","888","777","666","555","444","333","222","111","000"]
        for rep in repeats:
            if rep in num:
                return rep
        return ""