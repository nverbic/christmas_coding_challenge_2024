"""
 Tests for RemoveElement
"""
import src.day_02.remove_elem as remove_element

class TestRemoveElement:

    def test_01(self):
        """ Expected result: k=2"""
        nums = [3,2,2,3]
        val = 3
        result = [2,2]

        remove_el = remove_element.RemoveElement()
        k = remove_el.remove_element(nums, val)

        assert k == len(result)
        nums.sort()
        
        for i in range(len(result)):
            assert nums[i] == result[i]

    def test_02(self):
        """ Expected result: k=5"""
        nums = [0,1,2,2,3,0,4,2]
        val = 2
        result = [0,0,1,3,4]

        remove_el = remove_element.RemoveElement()
        k = remove_el.remove_element(nums, val)

        assert k == len(result)
        nums.sort()
        
        for i in range(len(result)):
            assert nums[i] == result[i]