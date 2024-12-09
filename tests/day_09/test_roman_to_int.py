"""
 Tests for RomanToInt
"""
from src.day_09 import roman_to_int

class TestRomanToInt:

    def test_01(self):
        roman_num = "MCMXCIV"
        expected_val = 1994

        romToInt = roman_to_int.RomanToInt()
        num = romToInt.romanToInt(roman_num)

        assert expected_val == num

    def test_02(self):
        roman_num = "III"
        expected_val = 3

        romToInt = roman_to_int.RomanToInt()
        num = romToInt.romanToInt(roman_num)

        assert expected_val == num

    def test_03(self):
        roman_num = "LVIII"
        expected_val = 58

        romToInt = roman_to_int.RomanToInt()
        num = romToInt.romanToInt(roman_num)

        assert expected_val == num
