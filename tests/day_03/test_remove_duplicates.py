"""
 Tests for RemoveElement
"""
from src.day_03 import remove_duplicates

class TestRemoveDuplicates:

    def test_01(self):
        """ Expected result: k=5 """
        nums = [0,0,1,1,1,2,2,3,3,4]
        result = [0,1,2,3,4]

        remove_dpl = remove_duplicates.RemoveDuplicates()
        k = remove_dpl.removeDuplicatesTwoPointers(nums)

        assert k == len(result)

        for i in range(len(result)):
            assert nums[i] == result[i]
