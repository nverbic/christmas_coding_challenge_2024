"""
Challenge 13

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 
12 is written as XII, which is simply X + II. 
The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Example 1:
Input: s = "III"
Output: 3

Example 2:
Input: s = "LVIII"
Output: 58

Example 3:
Input: s = "MCMXCIV"
Output: 1994

Running in main() function:
Roman number MCMXCIV is 1994
"""

class RomanToInt:
    """ Convert roman number to integer number"""
    def romanToInt(self, s: str) -> int:
        """ Convert roman numbers to int """
        roman_dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        num = 0

        for i in range(len(s)):
            if i + 1 < len(s) and roman_dict[s[i]] < roman_dict[s[i+1]]:
                num -=  roman_dict[s[i]]
            else:
                num += roman_dict[s[i]]
        return num

if __name__ == "__main__":
    roman_num = "MCMXCIV"
    romToInt = RomanToInt()
    num = romToInt.romanToInt(roman_num)
    print(f"Roman number {roman_num} is {num}")
