"""
 Tests for FirstOccurrence
"""
from src.day_06 import first_occurrence

class TestFirstOccurrence:

    def test_01(self):
        """ Expected result: index=0 """
        haystack = "sadbutsad"
        needle = "sad"
        result = 0

        firstOccurrence = first_occurrence.FirstOccurrence()
        index = firstOccurrence.findFirstOccurrence(haystack, needle)

        assert index == result

    def test_02(self):
        """ Expected result: index=-1 """
        haystack = "leetcode"
        needle = "leeto"
        result = -1

        firstOccurrence = first_occurrence.FirstOccurrence()
        index = firstOccurrence.findFirstOccurrence(haystack, needle)

        assert index == result
