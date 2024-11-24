# 844. BACKSPACE STRING COMPARE

# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

 

# Example 1:

# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".

# Example 2:

# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".

# Example 3:

# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".

# Example 4:

# Input: s = "a#c#", t = "#a#c"

from collections import deque

def backspaceStringCompare(s, t):
    if s==t:
        return True
    dqs = deque()
    dqt = deque()
    for i in range(len(s)):
        if s[i]=='#':
            if dqs:
                dqs.pop()
            else:
                continue
        else:
            dqs.append(s[i])
    for i in range(len(t)):
        if t[i]=='#':
            if dqt:
                dqt.pop()
            else:
                continue
        else:
            dqt.append(t[i])
    return dqs==dqt

print(backspaceStringCompare( s = "a#c#", t = "#a#c"))
    