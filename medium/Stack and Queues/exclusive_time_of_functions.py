# 636. Exclusive Time of Functions

# On a single-threaded CPU, we execute a program containing n functions. Each function has a unique ID between 0 and n - 1.

# Function calls are stored in a call stack: when a function call starts, its ID is pushed onto the stack, and when a function call ends, its ID is popped off the stack. The function whose ID is at the top of the stack is the current function being executed. Each time a function starts or ends, we write a log with the ID, whether it started or ended, and the timestamp.

# You are given a list logs, where logs[i] represents the ith log message formatted as a string "{function_id}:{"start" | "end"}:{timestamp}". For example, "0:start:3" means a function call with function ID 0 started at the beginning of timestamp 3, and "1:end:2" means a function call with function ID 1 ended at the end of timestamp 2. Note that a function can be called multiple times, possibly recursively.

# A function's exclusive time is the sum of execution times for all function calls in the program. For example, if a function is called twice, one call executing for 2 time units and another call executing for 1 time unit, the exclusive time is 2 + 1 = 3.

# Return the exclusive time of each function in an array, where the value at the ith index represents the exclusive time for the function with ID i.

# Example 1:


# Input: n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
# Output: [3,4]
# Explanation:
# Function 0 starts at the beginning of time 0, then it executes 2 for units of time and reaches the end of time 1.
# Function 1 starts at the beginning of time 2, executes for 4 units of time, and ends at the end of time 5.
# Function 0 resumes execution at the beginning of time 6 and executes for 1 unit of time.
# So function 0 spends 2 + 1 = 3 units of total time executing, and function 1 spends 4 units of total time executing.

# Example 2:

# Input: n = 1, logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
# Output: [8]
# Explanation:
# Function 0 starts at the beginning of time 0, executes for 2 units of time, and recursively calls itself.
# Function 0 (recursive call) starts at the beginning of time 2 and executes for 4 units of time.
# Function 0 (initial call) resumes execution then immediately calls itself again.
# Function 0 (2nd recursive call) starts at the beginning of time 6 and executes for 1 unit of time.
# Function 0 (initial call) resumes execution at the beginning of time 7 and executes for 1 unit of time.
# So function 0 spends 2 + 4 + 1 + 1 = 8 units of total time executing.

# Example 3:

# Input: n = 2, logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]
# Output: [7,1]
# Explanation:
# Function 0 starts at the beginning of time 0, executes for 2 units of time, and recursively calls itself.
# Function 0 (recursive call) starts at the beginning of time 2 and executes for 4 units of time.
# Function 0 (initial call) resumes execution then immediately calls function 1.
# Function 1 starts at the beginning of time 6, executes 1 unit of time, and ends at the end of time 6.
# Function 0 resumes execution at the beginning of time 7 and executes for 1 unit of time.
# So function 0 spends 2 + 4 + 1 = 7 units of total time executing, and function 1 spends 1 unit of total time executing.
 

# Constraints:

# 1 <= n <= 100
# 2 <= logs.length <= 500
# 0 <= function_id < n
# 0 <= timestamp <= 109
# No two start events will happen at the same timestamp.
# No two end events will happen at the same timestamp.
# Each function has an "end" log for each "start" log.

# time complexity: O(N)
# space complexity: O(N)
class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        exclusive_times = [0]*n # exclusive_times[i] = total CPU time spent executing function i
        stack = [] # will hold id of starts of time periods, # Top of stack is the function currently using the CPU.
        prev_start_time = 0 # Beginning of the unaccounted execution interval
        for log in logs:
            log_id, typ, timestamp = log.split(":") # Example: "1:start:2" -> ["1", "start", "2"]
            log_id = int(log_id)
            timestamp = int(timestamp)
            if typ == "start":
                # Current function stops running because a new function starts.
                # Credit it for [prev_time, timestamp).
                if stack:
                    prev_id = stack[-1]
                    exclusive_times[prev_id]+= timestamp - prev_start_time
                stack.append(log_id) # New function is now executing.
                prev_start_time = timestamp # Its execution starts at this timestamp.
            else: # typ = "end"
                popped_id = stack.pop() # Function at top of stack is the one ending.
                exclusive_times[popped_id]+= timestamp - prev_start_time + 1 # End timestamp is inclusive, hence +1.
                prev_start_time = timestamp + 1 # Parent function, if any, resumes at next timestamp.
        return exclusive_times 
    
# Example 1: nested functions
# n = 2
# logs = [
#     "0:start:0",
#     "1:start:2",
#     "1:end:5",
#     "0:end:6"
# ]

# Initial state:

# exclusive_times = [0, 0]
# stack = []
# prev_start_time = 0
# "0:start:0"

# We reach:

# if typ == "start":

# The stack is empty, so no previous function needs to be credited.

# Push function 0:

# stack = [0]
# prev_start_time = 0

# Function 0 starts executing at time 0.

# "1:start:2"

# Before function 1 starts, function 0 has been running:

# time 0
# time 1

# That's:

# 2 - 0 = 2

# The code:

# if stack:
#     prev_id = stack[-1]
#     exclusive_times[prev_id] += timestamp - prev_start_time

# becomes:

# prev_id = 0

# exclusive_times[0] += 2 - 0
#                    += 2

# Now:

# exclusive_times = [2, 0]

# Push function 1:

# stack = [0, 1]

# and:

# prev_start_time = timestamp

# so:

# prev_start_time = 2

# Now function 1 owns the CPU starting at time 2.

# "1:end:5"

# Function 1 has run from the beginning of 2 through the end of 5:

# 2, 3, 4, 5

# That's 4 units.

# The code:

# popped_id = stack.pop()

# gives:

# popped_id = 1
# stack = [0]

# Then:

# exclusive_times[popped_id] += timestamp - prev_start_time + 1

# becomes:

# exclusive_times[1] += 5 - 2 + 1
#                    += 4

# Now:

# exclusive_times = [2, 4]

# Then:

# prev_start_time = timestamp + 1

# so:

# prev_start_time = 6

# Why 6?

# Because function 1 occupied the entire timestamp 5. Function 0 can resume only at the beginning of timestamp 6.

# "0:end:6"

# Function 0 resumed at time 6 and ends at the end of 6.

# Therefore it gets:

# 6 - 6 + 1 = 1

# Final:

# exclusive_times = [3, 4]

# which is correct.

# A compact timeline is:

# time:       0   1   2   3   4   5   6
# function:   0   0   1   1   1   1   0

# function 0 = 3
# function 1 = 4
# Why a "start" uses no +1

# This line:

# exclusive_times[prev_id] += timestamp - prev_start_time

# can initially seem inconsistent with:

# timestamp - prev_start_time + 1

# for an end.

# Suppose:

# 0:start:0
# 1:start:2

# When function 1 starts at the beginning of time 2, function 0 has already stopped executing.

# So function 0 used:

# 0, 1

# not:

# 0, 1, 2

# Therefore:

# 2 - 0 = 2

# No +1.

# But if you have:

# 1:start:2
# 1:end:5

# the end is at the end of time 5, so function 1 owns:

# 2,3,4,5

# Hence:

# 5 - 2 + 1 = 4

# That's probably the single most important detail in this problem.

# Example 2: recursion

# Now:

# n = 1

# logs = [
#     "0:start:0",
#     "0:start:2",
#     "0:end:5",
#     "0:start:6",
#     "0:end:6",
#     "0:end:7"
# ]

# The same function can appear multiple times in the stack:

# stack = [0, 0]

# because these represent different calls of function 0.

# First:

# 0:start:0

# Stack:

# [0]

# Then:

# 0:start:2

# Before the recursive call begins, the original call gets:

# 2 - 0 = 2

# So:

# exclusive_times = [2]
# stack = [0, 0]
#              ↑
#       recursive call

# Then:

# 0:end:5

# recursive call gets:

# 5 - 2 + 1 = 4

# Total:

# exclusive_times = [6]

# The inner call is popped:

# stack = [0]

# Original call resumes at:

# prev_start_time = 6

# Then another:

# 0:start:6

# The original call gets:

# 6 - 6 = 0

# That's correct: it resumed and immediately called itself again.

# Now stack:

# [0,0]

# Then:

# 0:end:6

# This recursive call starts and ends at timestamp 6.

# Its duration is:

# 6 - 6 + 1 = 1

# Total becomes:

# 7

# Then original function resumes at:

# 7

# and:

# 0:end:7

# adds:

# 7 - 7 + 1 = 1

# Final:

# [8]

# Notice why storing only the ID still works with recursion. The stack can simply contain:

# [0,0,0,...]

# Each entry represents a separate active invocation.

# Example 3: one function starts and ends at the same timestamp
# logs = [
#     "0:start:5",
#     "0:end:5"
# ]

# When it starts:

# stack = [0]
# prev_start_time = 5

# When it ends:

# 5 - 5 + 1 = 1

# Answer:

# [1]

# This example is useful for remembering why +1 exists.