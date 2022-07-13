from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(len(prices) - 1):
            p = prices[i+1] - prices[i]
            if p > 0:
                profit += p

        return profit


INPUT_FILE = 'example-1.txt'

with open(INPUT_FILE, 'r') as f:
    row = f.readline().strip()
    prices = list(map(int, row[1: -1].split(',')))

    solution = Solution()
    profit = solution.maxProfit(prices)

    print(profit)
