""" 
Challenge 28

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

Running in main() function:
The first occurence of substring sad in the string sadbutsad is at the index: 0
"""

from typing import List

class FirstOccurrence:
    """ Find the first occurrence of the substring """
    def findFirstOccurrence(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


if __name__ == "__main__":
    haystack = "sadbutsad"
    needle = "sad"

    firstOccurrence = FirstOccurrence()
    index = firstOccurrence.findFirstOccurrence(haystack, needle)
    print(f"The first occurence of substring {needle} in the string {haystack} is at the index: {index}")

