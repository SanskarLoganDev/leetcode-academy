# 1086. High Five

# Given a list of the scores of different students, items, where items[i] = [IDi, scorei] represents one score from a student with IDi, calculate each student's top five average.

# Return the answer as an array of pairs result, where result[j] = [IDj, topFiveAveragej] represents the student with IDj and their top five average. Sort result by IDj in increasing order.

# A student's top five average is calculated by taking the sum of their top five scores and dividing it by 5 using integer division.

# Example 1:

# Input: items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
# Output: [[1,87],[2,88]]
# Explanation: 
# The student with ID = 1 got scores 91, 92, 60, 65, 87, and 100. Their top five average is (100 + 92 + 91 + 87 + 65) / 5 = 87.
# The student with ID = 2 got scores 93, 97, 77, 100, and 76. Their top five average is (100 + 97 + 93 + 77 + 76) / 5 = 88.6, but with integer division their average converts to 88.
# Example 2:

# Input: items = [[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]
# Output: [[1,100],[7,100]]
from typing import List


# My solution using hash map
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        top = {}
        items.sort(reverse= True)
        n = len(items)
        for i in range(n):
            if items[i][0] not in top:
                top[items[i][0]] = [items[i][1]]
            else:
                top[items[i][0]].append(items[i][1])
        res = [[i,sum(top[i][0:5])//5] for i in top]
        return res[::-1]
    

# Solution using heap

# The heapreplace method pops and returns the smallest element from the heap then pushes the given element into the heap. This method is equivalent to heappop() followed by heappush().

import heapq
from typing import List

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        # Create a dictionary to map each student ID to a min‐heap of their top scores.
        student_scores = {}
        
        # Process each (ID, score) pair.
        for id, score in items:
            if id not in student_scores:
                # If this student hasn't been seen yet, create an empty list (heap).
                student_scores[id] = []
            # Get the current heap for this student.
            heap = student_scores[id]
            
            if len(heap) < 5:
                # If fewer than 5 scores are stored, push the current score onto the heap.
                heapq.heappush(heap, score)
            else:
                # If the heap already has 5 scores, then the smallest score is at the root.
                # If the new score is greater than the smallest (i.e. the root),
                # then it belongs in the top five and we replace the smallest.
                if score > heap[0]:
                    heapq.heapreplace(heap, score)
                    
        # Now compute the top five average for each student.
        # Sort the results by student ID in ascending order.
        result = []
        for id in sorted(student_scores.keys()):
            # The heap now contains the top 5 scores for the student.
            total = sum(student_scores[id])
            # Integer division by 5 gives the required average.
            result.append([id, total // 5])
        
        return result

# Example usage:
sol = Solution()
print(sol.highFive([[1,91],[1,92],[2,93],[2,97],[1,60],
                    [2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]))
# Expected output: [[1,87],[2,88]]

