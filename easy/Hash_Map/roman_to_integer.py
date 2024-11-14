def romanToInt(s):
    roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    sum = 0
    for i in range(len(s)):
        if i<(len(s)-1) and roman[s[i]]<roman[s[i+1]]:
            value = roman[s[i]]
            sum =sum-value # if it is IV, instead of doing 5-1 (V-I) and then skipping one iteration, simply subtract 1 (I) and then add 5 (V)
        else:
            value = roman[s[i]]
            sum=sum+value
                
    return sum
print(romanToInt("MCMXCIV"))