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

