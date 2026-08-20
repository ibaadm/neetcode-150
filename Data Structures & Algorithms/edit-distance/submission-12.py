class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        dp = list(range(n, -1, -1))

        for i in range(m - 1, -1, -1):
            prev_diag = dp[n]
            dp[n] = m - i
            for j in range(n - 1, -1, -1):
                temp = dp[j]
                if word1[i] == word2[j]:
                    dp[j] = prev_diag
                else:
                    dp[j] = 1 + min(
                        dp[j+1],
                        dp[j],
                        prev_diag,
                    )
                prev_diag = temp
        
        return dp[0]
