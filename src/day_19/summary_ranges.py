"""
Challenge 228
You are given a sorted unique integer array nums.
A range [a,b] is the set of all integers from a to b (inclusive).
Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
That is, each element of nums is covered by exactly one of the ranges, and there is no integer x
such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:
"a->b" if a != b
"a" if a == b

Example 1:
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

Example 2:
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"

Running in main():
For the list [0, 1, 2, 4, 5, 7] summary ranges are: ['0->2', '4->5', '7']
"""
from typing import List

class SummaryRanges:
    def findSumRanges(self, nums: List[int]) -> List[str]:
        """Using for loops and workin with values from the list"""
        summary_ranges_list = []

        if len(nums):
            temp_res = nums[0]

            for i in range(len(nums)):
                if i<len(nums)-1 and nums[i+1] - nums[i] <= 1:
                    continue

                if temp_res != nums[i]:
                    summary_ranges_list.append(str(temp_res) + "->" + str(nums[i]))
                else:
                    summary_ranges_list.append(str(nums[i]))

                if i<len(nums)-1:
                    temp_res = nums[i+1]

        return summary_ranges_list

    def findSumRangesOptimized(self, nums: List[int]) -> List[str]:
        """ Using while loop and working with indexes of the list"""
        summary_ranges_list = []
        i = 0

        while i < len(nums):
            start = i
            while i < len(nums) - 1 and nums[i] + 1 == nums[i+1]:
                i += 1

            if start == i:
                summary_ranges_list.append(str(nums[start]))
            else:
                summary_ranges_list.append(str(nums[start]) + "->" + str(nums[i]))
            i += 1

        return summary_ranges_list

if __name__ == "__main__":
    test = SummaryRanges()
    test_nums = [0,1,2,4,5,7]
    res = test.findSumRangesOptimized(test_nums)
    print(f"For the list {test_nums} summary ranges are: {res}")
