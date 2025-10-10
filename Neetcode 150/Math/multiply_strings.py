# 43. Multiply Strings
# Neetcode 150 (Important)

# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

# Example 1:

# Input: num1 = "2", num2 = "3"
# Output: "6"

# Example 2:

# Input: num1 = "123", num2 = "456"
# Output: "56088"

# Constraints:

# 1 <= num1.length, num2.length <= 200
# num1 and num2 consist of digits only.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.

# Basic solution (not asked)

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1)*int(num2))



# time complexity: O(m*n) where m and n are lengths of num1 and num2
# space complexity: O(m+n) for result array  
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2=="0": # edge case checking if any number is 0
            return "0"

        res = [0]*(len(num1)+len(num2))
        k = len(res)-1 # pointer to current position in result array
        power_factor = 0 # to handle the position of current digit in num2
        for d2 in range(len(num2)-1,-1,-1): # num2 (the one that comes below)
            carry = 0
            for d1 in range(len(num1)-1,-1,-1): # num1 (the one at top)
                mult = (ord(num1[d1])-ord('0'))*(ord(num2[d2])-ord('0')) + carry # multiply and add carry
                result = mult%10 # digit to be stored at current position
                carry = mult//10 # carry for next position
                res[k]+=result
                if res[k]>=10:
                    res[k-1] =res[k-1] + res[k]//10
                    res[k] = res[k]%10
                    
                k-=1
                # print(mult, result, carry, res)
            if carry:
                res[k]+=carry
            power_factor+=1 # increase power factor for next digit in num2
            k=len(res)-1-power_factor # reset k to last position - power factor

        beg_zero = 0
        while res and res[beg_zero]==0:
            beg_zero+=1
        res = map(str, res[beg_zero:]) # convert to string, here we have used map instead of str in loop as inbuilt functions were not allowed
        return "".join(res)