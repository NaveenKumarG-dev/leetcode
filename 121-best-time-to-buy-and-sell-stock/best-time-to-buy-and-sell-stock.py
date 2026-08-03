class Solution(object):
    def maxProfit(self, prices):
        max_price = 0
        max_profit = 0

        for i in range(len(prices) - 1, -1, -1):
            if prices[i] > max_price:
                max_price = prices[i]

            profit = max_price - prices[i]

            if profit > max_profit:
                max_profit = profit

        return max_profit