class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) <= 1:
            return 0

        maxP = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r

            else:
                maxP = max(maxP, prices[r] - prices[l])
            r+=1
        return maxP 


