""" 
Challenge 169

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Running in main() function:
Array: [1, 2, 2]
Majority elem in the array: 2
"""

from typing import List

class MajorityElement(object):
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        count=1
        for i in range(0, n-1):
            if nums[i] == nums[i+1]:
                count += 1
                if count > (n/2):
                    return nums[i]
            else:
                count=1
        return nums[0]


if __name__ == "__main__":
    nums=[2,2,1]
    majorElem = MajorityElement()
    result = majorElem.majorityElement(nums)
    print(f"Array: {nums}")
    print(f"Majority elem in the array: {result}")
