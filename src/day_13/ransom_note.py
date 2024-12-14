"""
Challenge 383

Given two strings ransomNote and magazine, return true if ransomNote can be
constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote. 

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

Running in main() func:
From the word "sasa" it is possible to construct the "aass" : True
"""
from collections import Counter

class Solution:
    """ Check if ransomNote can be constructed by using the letters 
    from magazine."""
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineCounter = Counter(magazine)

        for char in ransomNote:
            if char in magazineCounter.keys() and magazineCounter[char] > 0:
                magazineCounter[char] += -1
            else:
                return False

        return True

if __name__ == "__main__":
    ransomNote = "aass"
    magazine = "sasa"
    constructWord = Solution()
    res = constructWord.canConstruct(ransomNote, magazine)
    print(f"From the word \"{magazine}\" it is possible to construct the \"{ransomNote}\" : {res}")
