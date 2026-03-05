# 1758. Minimum Changes To Make Alternating Binary String

# You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

# The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.

# Return the minimum number of operations needed to make s alternating.


# Example 1:

# Input: s = "0100"
# Output: 1
# Explanation: If you change the last character to '1', s will be "0101", which is alternating.

# Example 2:

# Input: s = "10"
# Output: 0
# Explanation: s is already alternating.
# Example 3:

# Input: s = "1111"
# Output: 2
# Explanation: You need two operations to reach "0101" or "1010".
 

# Constraints:

# 1 <= s.length <= 104
# s[i] is either '0' or '1'.

# time complexity: O(N)
# space complexity: O(N)
class Solution:
    def minOperations(self, s: str) -> int:
        s0 = ""
        s1 = ""
        n = len(s)
        for i in range(n):
            if i%2==0:
                s0+="0"
            else:
                s0+="1"

        for i in range(n):
            if i%2==0:
                s1+="1"
            else:
                s1+="0"
        count_s0 = 0
        count_s1 = 0
        for i in range(n):
            if s[i]!=s0[i]:
                count_s0+=1
            if s[i]!=s1[i]:
                count_s1+=1
        return min(count_s0, count_s1)
    
    
# Optimised solution
# time complexity: O(N)
# space complexity: O(1)

class Solution:
    def minOperations(self, s: str) -> int:
        count_s0 = 0 # starting with 0
        count_s1 = 0 # starting with 1
        for i in range(len(s)):
            if i%2==0: # we want starting with 0: 010101...
                if s[i]=='0': # when starting with 0, we want the even indexes to be 0 thats why we increase the count_s1
                    count_s1+=1
                else:
                    count_s0+=1
            else:
                if s[i]=='1': # # when starting with 0, we want the odd indexes to be 1 thats why we increase the count_s1
                    count_s1+=1
                else:
                    count_s0+=1
        return min(count_s0, count_s1)
                

        
                