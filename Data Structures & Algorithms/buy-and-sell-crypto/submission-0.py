class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = 100000000
        max_profit = 0
        for i in range(len(prices)):
            curr_min = min(curr_min, prices[i])
            max_profit = max(max_profit, prices[i] - curr_min)
        return max_profit
        
        