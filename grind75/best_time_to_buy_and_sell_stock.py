from typing import List


# You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize
# your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that
# stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit: int = 0
        # slow pointer
        buying_index: int = 0
        # fast pointer
        selling_index: int = 0

        while selling_index < len(prices):
            profit = prices[selling_index] - prices[buying_index]
            max_profit = max(max_profit, profit)
            buying_index = selling_index if prices[selling_index] < prices[buying_index] else buying_index
            selling_index += 1

        return max_profit


if __name__ == '__main__':
    sol = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    answer = 5
    assert (sol.maxProfit(prices) == answer)
    prices = [7, 6, 4, 3, 1]
    answer = 0
    assert (sol.maxProfit(prices) == answer)
    prices = [7, 6, 4, 3, 5, 1]
    answer = 2
    assert (sol.maxProfit(prices) == answer)
