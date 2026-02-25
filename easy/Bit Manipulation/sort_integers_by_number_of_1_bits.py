# 1356. Sort Integers by The Number of 1 Bits
# You are given an integer array arr. Sort the integers in the array in ascending order by the number of 1's in their binary representation and in case of two or more integers have the same number of 1's you have to sort them in ascending order.

# Return the array after sorting it.
 

# Example 1:

# Input: arr = [0,1,2,3,4,5,6,7,8]
# Output: [0,1,2,4,8,3,5,6,7]
# Explantion: [0] is the only integer with 0 bits.
# [1,2,4,8] all have 1 bit.
# [3,5,6] have 2 bits.
# [7] has 3 bits.
# The sorted array by bits is [0,1,2,4,8,3,5,6,7]

# Example 2:

# Input: arr = [1024,512,256,128,64,32,16,8,4,2,1]
# Output: [1,2,4,8,16,32,64,128,256,512,1024]
# Explantion: All integers have 1 bit in the binary representation, you should just sort them in ascending order.
 

# Constraints:

# 1 <= arr.length <= 500
# 0 <= arr[i] <= 104

# time complexty: O(nlogn)
# space complexity: O(n)
from typing import List
import heapq
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def countBits(n): # essentially O(1) as there can't be more than 32 numbers of 1 in a number
            x = n
            count = 0
            while x:
                x = x & x-1 # and of current and current-1 helps count the number of set bits in binary
                count+=1
            return count
        heap = []
        for n in arr:
            count = countBits(n)
            heapq.heappush(heap, (count, n))
        res = []
        for i in range(len(heap)):
            res.append(heapq.heappop(heap)[1]) # ensure the numbers in the heap are extracted properly
        return res
