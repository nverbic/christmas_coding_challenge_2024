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
from collections import Counter

class MajorityElement(object):
    def majorityElement(self, nums: List[int]) -> int:
        """ Find majority element """
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

    def majorityElementCounter(self, nums: List[int]) -> int:
        """ Find majority element - faster solution """
        counter_nums = Counter(nums)
        val, _ = counter_nums.most_common(1)[0]
        return val


if __name__ == "__main__":
    nums=[2,1,2]
    majorElem = MajorityElement()
    #result = majorElem.majorityElement(nums)
    result = majorElem.majorityElementCounter(nums)
    print(f"Array: {nums}")
    print(f"Majority elem in the array: {result}")
