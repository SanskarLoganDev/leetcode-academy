# 76. Minimum Window Substring 
# (NeetCode 150) Important

# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
 

# Constraints:

# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s and t consist of uppercase and lowercase English letters.
 

# Follow up: Could you find an algorithm that runs in O(m + n) time?


# Brute force solution:
# time complexity : O(M^3) and space complexity: O(M+N)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        if n > m:
            return ""
        # Creating the hashmap counter of t
        count_t = {}
        for c in t: # O(N)
            count_t[c] = count_t.get(c, 0) + 1
        
        min_window = ""
        for i in range(m): # O(M)
            for j in range(i+n, m+1): # O(M)
                substr = s[i:j] # O(M)
                count_s = {}
                # Creating the hashmap counter of substr
                for char in substr:
                    count_s[char] = count_s.get(char, 0)+1

                # Now we compare the count of a character in counter of t and counter of s
                valid = True
                for c, cnt in count_t.items():
                    if count_s.get(c,0)<cnt:
                        valid = False
                        break # break when we find an invalid case: for example: a character in t does not exist in the substr
                
                # We only update min_window if the count for all characters in t is same as of those chars in substr
                if valid:
                    if min_window=="" or len(substr)<len(min_window):
                        min_window = substr
                    break # only break when valid, keep expanding j when invalid. 
                # After finding a valid case we try to reduce the length of min_window by moving i, thats why we break out the j loop
        return min_window 
        
sol = Solution()
ans = sol.minWindow(s = "ADOBECODEBANC", t = "ABC")
print(ans)

# Optimised solution
# Time complexity: O(m + n), where m is the length of s and n is the length of t. We traverse both strings once.
# Space complexity: O(1), problem guarantees only uppercase and lowercase English letters, there are at most 52 distinct keys ever for the map, regardless of how long s or t are.
# Code story with MIK video: https://www.youtube.com/watch?v=3Bp3OVD1EGc
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        if n > m:
            return ""
        
        mp = {} 
        for c in t: # for all the chars in t, their count is stored in map
            mp[c] = mp.get(c, 0) + 1
        
        count_required = len(t)
        i = 0 # shrinking the window
        j = 0 # expanding the window
        start_i = 0 # start index of the minimum window size
        minWindowSize = float("inf")
        
        while j<m:
            ch = s[j] 
            if mp.get(ch, 0)>0: # if a value whose count in map is greater than 0 (meaning that is a required character), we reduce the count_required
                count_required-=1

            mp[ch] = mp.get(ch, 0) - 1 # whatever we find with index j, we will decrement it in the map
            
            while count_required==0: # when the count_required is 0, meaning we found a possible solution and now we can try to shrink the window to get a better solution
                # start shrinking the window
                currWindowSize = j-i+1 # updateing the minimum window size
                if currWindowSize < minWindowSize:
                    minWindowSize = currWindowSize
                    start_i = i # the starting index of minimum window
                mp[s[i]] = mp.get(s[i],0)+1 # the values leaving the window with the increment of it will get a +1 in their map count
                if mp[s[i]]>0: # if a required value has left the window and their count now becomes greater than 0, thus count_required + 1 and the loop breaks since it is no longer 0
                    count_required+=1
                
                i+=1 # actual shrinking happens at the end of the loop after the required calculations are done
            j+=1
        # getting the exact minimum string window
        return  s[start_i : start_i + minWindowSize] if minWindowSize!=float("inf") else "" # if minWindowSize remains infinity that means we did not find a solution and we return ""
        


sol = Solution()
ans = sol.minWindow(s = "ADOBECODEBANC", t = "ABC")
print(ans)


# Time complexity: O(m + n), where m is the length of s and n is the length of t. We traverse both strings once.
# Space complexity: O(m + n), for storing the character counts in countT and window dictionaries.
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        countT, window = {}, {} # here we use dictionaries to count the characters in t and the current window in s
        for c in t:
            countT[c] = 1+countT.get(c, 0)
        
        have, need = 0, len(countT)
        res, reslen = [-1,-1], float("inf") # Here we use res to store the result (as we have to return the min string and not just its length) and reslen to store the length of the result window
        # l is the left pointer and r is the right pointer of the sliding window
        l=0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r],0)
            if s[r] in countT and window[s[r]] == countT[s[r]]: # here we check if the current character in s is in t and if its count in the window matches the count in t
                have+=1
            
            while have == need:
                # updating the result if the current window is smaller than the previous one
                if (r-l+1)<reslen:
                    res = [l,r]
                    reslen = r-l+1
                # removing the leftmost character from the window
                window[s[l]]-=1
                if s[l] in countT and window[s[l]] < countT[s[l]]: # here we check if the leftmost character is in t and if its count in the window is less than the count in t
                    have-=1
                l+=1
        l, r = res[0], res[1]
        
        return s[l:r+1] if reslen != float("inf") else ""