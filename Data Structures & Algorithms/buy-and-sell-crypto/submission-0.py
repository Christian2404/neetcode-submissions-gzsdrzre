class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = float('inf')
        best_profit = float('-inf')
        
        for price in prices:

            profit = price - min_price
            best_profit = max(best_profit, profit)

            min_price = min(min_price, price)

        if best_profit > 0:
            return best_profit
        else:
            return 0