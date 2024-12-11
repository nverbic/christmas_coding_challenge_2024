"""
Challenge 14

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 Example 1:
Input: strs = ["flower","flow","flight", "fler"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Running in main() func:
['dog', 'dom', 'done']
The longest common prefix of strings in a list is: do
"""
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = min(strs, key=len)

        for _ in range(len(prefix)):
            watch = True
            for i in range(len(strs)):
                if strs[i].startswith(prefix) == False:
                    prefix = prefix[:-1]
                    watch = False
                    break
            if watch:
                return prefix

        return ""
 
if __name__ == "__main__":
    s= ["dog","dom","done"]
    var = Solution()
    res = var.longestCommonPrefix(s)
    print(s)
    print(f"The longest common prefix of strings in a list is: {res}")
