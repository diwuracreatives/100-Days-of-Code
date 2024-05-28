"""
100 Days of Code - Day 4

Topic:
-----
Strings

Question:
---------
Ransom Note
Given two strings ransomNote and magazine, return true if ransomNote can be constructed
by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Solution:
---------
"""
 def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_dict = {}

        for i in range(len(magazine)):
            if mag_dict.get(magazine[i]) == None:
                mag_dict[magazine[i]] = 1
            else:
                mag_dict[magazine[i]] += 1
        

        for i in range(len(ransomNote)):
            if mag_dict.get(ransomNote[i]) == None or  mag_dict[ransomNote[i]] == 0:
                return False
            else:
                mag_dict[ransomNote[i]] -= 1
        return True
"""
Reflection:
-----------
Learnt about accessing and manipulating dictionary and strings.

Additional Notes:
-----------------
Leetcode Link - https://leetcode.com/problems/ransom-note/

"""

