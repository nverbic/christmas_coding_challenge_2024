''' 
Challenge 88

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should
be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n. 

Example:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Running in main() function:
nums1: [2, 3, 4, 0]
nums2: [1]
After merge nums1 and nums2: [1, 2, 3, 4]
'''


class MergeSortedArray(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        print(f"nums1: {nums1}")
        print(f"nums2: {nums2}")
        nums1[m:m+n] = nums2
        nums1.sort()
        print(f"After merge nums1 and nums2: {nums1}")

if __name__ == "__main__":
    nums1 = [2,3,4,0]
    m=3
    nums2 = [1]
    n=1

    merge_arrays = MergeSortedArray()
    merge_arrays.merge(nums1, m, nums2, n)
