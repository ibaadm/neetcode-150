from functools import cache

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        @cache
        def dfs(i, j):
            if j == m:
                return 1
            
            if n - i < m - j:
                return 0
            
            res = dfs(i+1, j)
            if s[i] == t[j]:
                res += dfs(i+1, j+1)
            return res

        return dfs(0, 0)