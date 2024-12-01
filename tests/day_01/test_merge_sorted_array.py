"""
 Tests for MergeSortedArray
"""
import src.day_01.merge_sorted_array as merge_array

class TestMergeSortedArray:

    def test_01(self):
        """ Expected result: num1 = [1,2,2,3,5,6] """
        nums1 = [1,2,3,0,0,0]
        m = 3
        nums2 = [2,5,6]
        n = 3
        result = [1,2,2,3,5,6]

        merge_sorted_arrays = merge_array.MergeSortedArray()
        merge_sorted_arrays.merge(nums1, m, nums2, n)
        assert nums1 == result

    def test_02(self):
        """ Expected result: num1 = [1] """
        nums1 = [1]
        m = 1
        nums2 = []
        n = 0
        result = [1]

        merge_sorted_arrays = merge_array.MergeSortedArray()
        merge_sorted_arrays.merge(nums1, m, nums2, n)
        assert nums1 == result

    def test_03(self):
        """ Expected result: num1 = [1] """
        nums1 = [0]
        m = 0
        nums2 = [1]
        n = 1
        result = [1]

        merge_sorted_arrays = merge_array.MergeSortedArray()
        merge_sorted_arrays.merge(nums1, m, nums2, n)
        assert nums1 == result
