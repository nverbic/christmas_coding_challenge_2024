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
 

Running in main() func:
mississippi
The first occurence of a substring: issip is at index: 4

mississippi
The first occurence of a substring: issipi is at index: -1

"""

class Solution:
    def firstOccurrenceFind(self, haystack: str, needle: str) -> int:
        res = haystack.find(needle)
        return res


    def firstOccurrenceForLoop(self, haystack: str, needle: str) -> int:
        if len(needle) <= len(haystack):
            list_indexes = [i for i, ltr in enumerate(haystack) if ltr == needle[0]]

            for i in list_indexes:
                is_substring = 0
                start = i
                for j in range(0, len(needle)):
                    if start+j >= len(haystack) or haystack[start+j] != needle[j]:
                        is_substring = 0
                        break
                    is_substring += 1
                if(is_substring == len(needle)):
                    return i
        return -1



if __name__ == "__main__":
    haystack = "mississippi"
    needle = "issipi"
    var = Solution()
    res = var.firstOccurrenceForLoop(haystack, needle)
    print(res)
    print(f"{haystack}")
    print(f"The first occurence of a substring: {needle} is at index: {res}")
