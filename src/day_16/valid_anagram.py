"""
Challenge 242
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Running in main() func:
Word "gramana" is anagram of the word "anagram": True
"""

class Solution:
    """ Check if string is an anagram """
    def isAnagram(self, original: str, anagram: str) -> bool:
        #Use dictionary
        origDict = {}
        anagramDict = {}

        if (len(original) != len(anagram)):
            return False

        for i in range(len(original)):
            if (original[i] not in origDict.keys()):
                origDict[original[i]] = 1
            else:
                origDict[original[i]] += 1

            if (anagram[i] not in anagramDict.keys()):
                anagramDict[anagram[i]] = 1
            else:
                anagramDict[anagram[i]] += 1

        if (anagramDict != origDict):
            return False

        return True

    def isAnagramSort(self, original: str, anagram: str) -> bool:
        #Use strings
        if sorted(original) == sorted(anagram):
            return True
        return False

if __name__ == "__main__":
    s = "anagram"
    t = "gramana"
    checkAnagram = Solution()
    res = checkAnagram.isAnagram(s,t)
    print(f"Word \"{t}\" is anagram of the word \"{s}\": {res}")
