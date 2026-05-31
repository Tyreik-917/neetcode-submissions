class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l = profit = best = 0
        r = 1

        while r < len(prices):

            profit = prices[r] - prices[l]
            print(profit)

            if best < profit:
                best = profit

            elif best > profit and profit < 0:
                l+=1
                r-=1

            r+=1

        if best < 0:
            return 0

        return best


