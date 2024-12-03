""" 
Challenge 26

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element
appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements
in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the unique elements in the order they were
present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.

Example:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Running in main() function:
Array nums: [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
Number of unique elems: 5
After removing duplicates nums: [0, 1, 2, 3, 4, 2, 2, 3, 3, 4] 

"""

from typing import List

class RemoveDuplicates(object):

    def removeDuplicates(self, nums: List[int]) -> int:
        """ Remove duplicates from a list - slower version """
        nums_copy = nums.copy()

        for i in range(0, len(nums_copy)-1):
            if nums_copy[i] == nums_copy[i+1]:
                nums.remove(nums_copy[i])

        return len(nums)

    def removeDuplicatesTwoPointers(self, nums: List[int]) -> int:
        """ Remove duplicates from a list - faster version"""
        count_unique = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[count_unique] = nums[i]
                count_unique += 1

        return count_unique


if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    test_result = 5
    test_nums = [0,1,2,3,4,]

    print(f"Array nums: {nums}")
    remove_dpl = RemoveDuplicates()
    k = remove_dpl.removeDuplicatesTwoPointers(nums)
    print(f"Number of unique elems: {k}")
    print(f"After removing duplicates nums: {nums}")
