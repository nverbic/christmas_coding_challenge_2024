"""
Challenge 58

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

Running in main() function:
   fly me   to   the moon   
Length of the last word in string is: 4
"""

class LengthOfLastWord:
    """ Given a string s consisting of words and spaces,
        return the length of the last word in the string. 
    """
    def lengthOfLastWord(self, s: str) -> int:
        """ Find length of the last word """

        list_of_words = s.split()
        return len(list_of_words[-1])

if __name__ == "__main__":
    s = "   fly me   to   the moon  "
    len_of_word = LengthOfLastWord()
    print(f"{s} \nLength of the last word in string is: {len_of_word.lengthOfLastWord(s)}")
