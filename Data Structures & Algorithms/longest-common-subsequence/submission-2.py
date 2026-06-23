class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        memo = [[-1]*n for _ in range(m)]

        def _longestCommonSubsequence(i, j):
            if i >= m: return 0
            if j >= n: return 0

            if memo[i][j] != -1:
                return memo[i][j]

            if text1[i] == text2[j]:
                memo[i][j] = 1 + _longestCommonSubsequence(i+1, j+1)
            else:
                memo[i][j] = max(_longestCommonSubsequence(i+1, j), _longestCommonSubsequence(i, j+1))
            return memo[i][j]
        
        return _longestCommonSubsequence(0, 0)