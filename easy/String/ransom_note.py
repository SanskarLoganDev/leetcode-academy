# 383 RANSOM NOTE

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

 

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true

def canConstruct(ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for char in ransomNote:
            if char in magazine:
                magazine = magazine.replace(char, '',1)
                continue

            return False
        
        return True
    
print(canConstruct(ransomNote = "aab", magazine = "baa")) # False
# print(canConstruct(ransomNote = "bg", magazine = "abcdefgh"))  # True

# Alt way (No difference in time complexity)

def canConstruct(ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        for c in set(ransomNote):
            if magazine.count(c) < ransomNote.count(c):
                return False

        return True