# 14 LONGEST COMMON PREFIX

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.



def longestCommonPrefix(strs) -> str:
    prefix = ""
    strs.sort()
    first = strs[0]
    last = strs[len(strs)-1]
    print(first, last)
    min_len = min(len(first),len(last))
    print(min_len)
    for i in range(min_len):
        if first[i]!=last[i]:
            break
        else:
            prefix=prefix+first[i]    
        
    return prefix
print(longestCommonPrefix(["dog","racecar","car"]))

