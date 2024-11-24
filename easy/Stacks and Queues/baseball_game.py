# 682. BASEBALL GAME

# You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

# You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

# An integer x.
# Record a new score of x.
# '+'.
# Record a new score that is the sum of the previous two scores.
# 'D'.
# Record a new score that is the double of the previous score.
# 'C'.
# Invalidate the previous score, removing it from the record.
# Return the sum of all the scores on the record after applying all the operations.

# The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.

 

# Example 1:

# Input: ops = ["5","2","C","D","+"]
# Output: 30
# Explanation:
# "5" - Add 5 to the record, record is now [5].
# "2" - Add 2 to the record, record is now [5, 2].
# "C" - Invalidate and remove the previous score, record is now [5].
# "D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
# "+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
# The total sum is 5 + 10 + 15 = 30.
# Example 2:

# Input: ops = ["5","-2","4","C","D","9","+","+"]
# Output: 27
# Explanation:
# "5" - Add 5 to the record, record is now [5].
# "-2" - Add -2 to the record, record is now [5, -2].
# "4" - Add 4 to the record, record is now [5, -2, 4].
# "C" - Invalidate and remove the previous score, record is now [5, -2].
# "D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4].
# "9" - Add 9 to the record, record is now [5, -2, -4, 9].
# "+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].
# "+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].
# The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.
# Example 3:

# Input: ops = ["1","C"]
# Output: 0
# Explanation:
# "1" - Add 1 to the record, record is now [1].
# "C" - Invalidate and remove the previous score, record is now [].
# Since the record is empty, the total sum is 0.

from collections import deque

def baseballGame(operations):
    dq = deque()
    sum = 0
    for i in range(len(operations)):
        if operations[i]=="C":
            sum-=dq[-1]
            dq.pop()
            
        elif operations[i]=="D":
            sum+=dq[-1]*2
            dq.append(dq[-1]*2)
            
        elif operations[i]=="+":
            sum+=dq[-1]+dq[-2]
            dq.append(dq[-1]+dq[-2])
            
        else:
            sum+=int(operations[i])
            dq.append(int(operations[i]))
            
    return sum
print(baseballGame(["1","C"]))

def baseballGame1(operations):
    dq = deque()
    for i in range(len(operations)):
        if operations[i]=="C":
            dq.pop()
            
        elif operations[i]=="D":
            dq.append(dq[-1]*2)
            
        elif operations[i]=="+":
            dq.append(dq[-1]+dq[-2])
            
        else:
            dq.append(int(operations[i]))
            
    return sum(dq) # instead of having sum as avariable, simply use the in built method
print(baseballGame1(["5","-2","4","C","D","9","+","+"]))