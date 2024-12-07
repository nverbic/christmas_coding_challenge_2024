""" 
Challenge 125

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Running in main() function:
Is palindrome: --- A man, a plan, a canal: Panama --- : True
"""

class Palindrome:
    """ Check if phrase is palindrome """
    def isPalindrome(self, phrase: str) -> bool:
        lower_str = phrase.lower()
        clean_str = ""
        for char in lower_str:
            if char.isalnum():
                clean_str += char

        return clean_str == clean_str[::-1]

if __name__ == "__main__":
    str_1 = "A man, a plan, a canal: Panama"
    palindrome = Palindrome()
    res = palindrome.isPalindrome(str_1)
    print(f"Is palindrome: --- {str_1} --- : {res}")
