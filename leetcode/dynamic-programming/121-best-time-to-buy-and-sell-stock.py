# -*- coding: utf-8 -*-
"""
create time : 2018-04-09 19:41:24
author : sk


"""


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) <= 1:
            return 0

        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            if price < min_price:
                min_price = price
            if price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit


if __name__ == '__main__':
    solution = Solution()

    prices = [7, 1, 5, 3, 6, 4]
    # prices = [7, 6, 4, 3, 1]

    result = solution.maxProfit(prices)

    print(result)
