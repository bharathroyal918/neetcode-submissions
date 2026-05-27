class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = prices[0]
        max_profit = 0

        for price in prices:

            # update minimum buying price
            min_price = min(min_price, price)

            # calculate profit
            profit = price - min_price

            # update maximum profit
            max_profit = max(max_profit, profit)

        return max_profit