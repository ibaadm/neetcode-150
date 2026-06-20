class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        i = 0
        j = 1
        while j < len(prices):
            if prices[j] < prices[i]:
                i = j
                j += 1
                continue
            res = max(res, prices[j] - prices[i])
            j += 1
        return res