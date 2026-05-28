class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        d = [0] * len(prices)
        min = prices[0]
        for i in range(1, len(prices)):
            d[i] = prices[i] - min
            if prices[i] < min:
                min = prices[i]
        return max(d)