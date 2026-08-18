class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        dp = [0] * m

        for i in range(n - 1, -1, -1):
            for j in range(m):
                if s[i] == t[j]:
                    dp[j] += dp[j+1] if j != m - 1 else 1
        
        return dp[0]
