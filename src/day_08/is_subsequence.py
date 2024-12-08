"""
Challenge 392

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters
without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 
Running in main() function:

"""

class Subsequence:
    """check if s is a subsequence of t. """
    def isSubsequnce(self, subsequence: str, word: str) -> bool:
        for char in subsequence:
            index =  word.find(char)
            if index > -1:
                word = word[index+1:len(word)]
            else:
                return False
        return True

if __name__ == "__main__":
    s = "abc"
    t = "ahbgdc"
    subs = Subsequence()
    res = subs.isSubsequnce(s, t)
    print(f"Is subsequence: --- {s} of {t}--- : {res}")
