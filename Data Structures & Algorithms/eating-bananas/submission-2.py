import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles) + 1

        def isEatingSpeedValid(k):
            total = 0
            for pile in piles:
                total += math.ceil(pile / k)
            return total <= h

        while l < r:
            mid = l + (r-l) // 2
            if isEatingSpeedValid(mid):
                r = mid
            else:
                l = mid + 1
        return l