""" 
Challenge 27

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
The remaining elements of nums are not important as well as the size of nums. Return k.

Example:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

Running in main() function:
Array nums: [0, 1, 2, 2, 3, 0, 4, 2]
Items to remove: 2
After removing items nums: [0, 0, 1, 3, 4]
"""

class RemoveElement(object):
    def remove_element(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        nums_copy = nums.copy()

        for i, item in enumerate(nums_copy):
            if item == val:
                nums.remove(val)


        return len(nums)

if __name__ == "__main__":
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    result = [0,0,1,3,4]

    print(f"Array nums: {nums}")
    print(f"Items to remove: {val}")
    remove_el = RemoveElement()
    k = remove_el.remove_element(nums, val)
    nums.sort()

    print(f"After removing items nums: {nums}")