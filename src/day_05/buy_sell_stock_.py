""" 
Challenge 121

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Running in main() function:
Array: [3, 2, 6, 5, 0, 3]
Max profit: 4
"""

from typing import List

class MaxProfit:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = prices[0]

        for item in prices[1:]:
            profit = max(profit, item - min_price)
            min_price = min(min_price, item)

        return profit

if __name__ == "__main__":
    #nums=[5,1,2,7]
    #nums=[5,5,4,5]
    nums=[3,2,6,5,0,3]
    print(f"Array: {nums}")
    maxProf = MaxProfit()
    result = maxProf.maxProfit(nums)
    print(f"Max profit: {result}")
