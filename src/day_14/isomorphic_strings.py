"""
Challenge 205

Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.
 
Example 1:
Input: s = "egg", t = "add"
Output: true

Explanation:
The strings s and t can be made identical by:

Mapping 'e' to 'a'.
Mapping 'g' to 'd'.

Example 2:
Input: s = "foo", t = "bar"
Output: false

Explanation:
The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:
Input: s = "paper", t = "title"
Output: true

Running in main() func:
Are the strings "paper" and "title" isomorphic: True
"""

class Solution:
    """determine if two strings are isomorphic """
    def isIsomorphic(self, firstStr: str, secondStr: str) -> bool:
        resDict = {}
        if len(firstStr) == len(secondStr):
            for i in range(len(firstStr)):
                if (firstStr[i] in resDict.keys() and resDict[firstStr[i]] != secondStr[i]) or \
                (secondStr[i] in resDict.values() and firstStr[i] not in resDict.keys()):
                    return False
                resDict[firstStr[i]] = secondStr[i]

        return True

    def isIsomorphicTwoDict(self, s: str, t: str):
        char_index_s = {}
        char_index_t = {}

        for i in range(len(s)):
            if s[i] not in char_index_s:
                char_index_s[s[i]] = i

            if t[i] not in char_index_t:
                char_index_t[t[i]] = i

            if char_index_s[s[i]] != char_index_t[t[i]]:
                return False

        return True

if __name__ == "__main__":
    s = "paper"
    t = "title"

    isomorphic = Solution()
    res = isomorphic.isIsomorphicTwoDict(s, t)
    print(f"Are the strings {s} and {t} isomorphic: {res}")
