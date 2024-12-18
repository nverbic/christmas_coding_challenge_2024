"""
Challenge 1

Given an array of integers nums and an integer target, return indices of the two numbers
such that they add up to target. You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order. 

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Running in main():
Input array: [2, 7, 11, 15, 2] and the target is: 4
Two indices that sum up to the target value are: [0, 4]
"""
from typing import List

class Solution:
    """ Return indices of the two numbers from a list such that they add up to target """
    def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
        """ Brute force """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i]+nums[j] == target:
                    return [i, j]
        return []
    
    def twoSumBruteForceOptimized(self, nums: List[int], target: int) -> List[int]:
        """ Hash table (dict) """
        dictNums = {}
        n = len(nums)

        for i in range(n):
            dictNums[nums[i]] = i

        print(dictNums)

        for i in range(n):
            y = target - nums[i]
            if y in dictNums and dictNums[y] != i:
                return [i, dictNums[y]]

        return []

if __name__ == "__main__":
    nums = [2,7,11,15,2]
    target = 4
    varSolution = Solution()
    res = varSolution.twoSumBruteForceOptimized(nums, target)
    print(f"Input array: {nums} and the target is: {target}")
    print(f"Two indices that sum up to the target value are: {res} ")
