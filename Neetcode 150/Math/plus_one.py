# 66. Plus One
# Neetcode 150 (Important)

# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
# The digits are ordered from most significant to least significant in left-to-right order. 
# The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
# Example 2:

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
# Example 3:

# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].
 
 
# optimised solu: time complexity is O(N), space complexity (memory) is better O(1)

def plusOne(digits):
    l = len(digits)
    for i in range(l-1, -1, -1): # the stop index is -1 because stop part does not include the number in it, so stop = 0 would stop
    # the loop at i = 1 and not go till 0 that's why we used -1. Here -1 is not to be confused with -1 the last element
        if digits[i]!=9:
            digits[i]+=1
            return digits
        else:
            digits[i]=0
    return [1]+ digits # will only reach here if all the digits are 9 and therefore 1 needs to be added to the front of the list

print(plusOne([9,9,9,9]))

# time complexity: O(N) where N is the number of digits in the number
# space complexity: O(N) where N is the number of digits in the number
def plusOne(digits):
    l = len(digits)
    if digits[l-1] != 9:
        digits[l-1]+=1
    else:
        str_digit=""
        for digit in digits:
            str_digit+=str(digit)
        res = str(int(str_digit)+1)
        digits = [int(x) for x in res]
        
    return digits

print(plusOne([1,2,9,9]))  

