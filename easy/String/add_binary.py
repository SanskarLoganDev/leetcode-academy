# 67. ADD BINARY

# Given two binary strings a and b, return their sum as a binary string.

 

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"

def addBinary(a,b):
    length = max(len(a), len(b))
    a_int = [int(x) for x in a]
    b_int = [int(x) for x in b]
    
    if len(a_int)> len(b_int):
        for i in range(len(a_int)-len(b_int)):
            b_int.insert(0,0)
    if len(b_int)> len(a_int):
        for i in range(len(b_int)-len(a_int)):
            a_int.insert(0,0)
            
    i=length-1
    res=[]
    while i>=0:
        sum=a_int[i]+b_int[i]
        
        
        if sum == 0 or sum ==1:
            res.insert(0,sum)
        if sum == 2:
            res.insert(0,0)
            a_int[i-1]+=1
        if sum == 3:
            res.insert(0,1)
            a_int[i-1]+=1
        if i == 0 and (sum ==2 or sum==3):
            res.insert(0,1)
        i-=1
    result =""
    for i in res:
        result+=str(i)
    return result
            
print(addBinary("11111","1"))
             
# Alternative Optimised solution using direct binary conversion

def addBinary2(a,b):
    res = bin(int(a,2)+int(b,2))
    return res[2:]
print(addBinary2("11111","1"))
        