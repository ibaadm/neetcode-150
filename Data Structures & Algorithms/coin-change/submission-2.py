class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        usable = [c for c in coins if c <= amount]
        if not usable:
            return -1

        W = max(usable)
        size = W + 1
        INF = float('inf')

        dp = [INF] * size
        dp[0] = 0

        for i in range(1, amount + 1):
            best = INF
            for c in usable:
                if c <= i:
                    prev = dp[(i - c) % size]
                    if prev + 1 < best:
                        best = prev + 1
            dp[i % size] = best

        res = dp[amount % size]
        return res if res != INF else -1