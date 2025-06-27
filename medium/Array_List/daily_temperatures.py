# 739. Daily Temperatures (Neetcode 150) Important

# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]
 

# Constraints:

# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100

from typing import List

# Time Complexity: O(n^2), space Complexity: O(n)
# My Solution: Brute Force
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            if i==len(temperatures)-1:
                res.append(0)
                break
            j=i
            count = 1
            while j<len(temperatures)-1 and temperatures[i]>=temperatures[j+1]:
                count+=1
                j+=1
            if j==len(temperatures)-1:
                res.append(0)
            else:
                res.append(count)
        return res
    
# Optimized Solution: Using Stack (Monotonic Stack)
# Time Complexity: O(n), Space Complexity: O(n)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = [] # [temp, index] # to keep track of the temperatures and their indices
        for i in range(len(temperatures)):
            while stack and temperatures[i]>stack[-1][0]: # if current temperature is greater than the last temperature in the stack, here we have -1 and 0 as indices for the last temperature and its index respectively
                temp, index = stack.pop()
                res[index] = i - index # calculate the difference between the current index and the index of the last temperature in the stack
            stack.append([temperatures[i], i])
        
        return res