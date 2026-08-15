from functools import cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def recurse(i, coin, sold_last):
            if i == n:
                return 0

            if coin:
                return max(recurse(i+1, False, True) + prices[i], recurse(i+1, True, False))

            if sold_last:
                return recurse(i+1, False, False)
            
            return max(recurse(i+1, True, False) - prices[i], recurse(i+1, False, False))

        return recurse(0, False, False)
