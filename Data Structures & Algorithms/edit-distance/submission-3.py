from functools import cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        @cache
        def recurse(i, j):
            if i == n:
                return m - j
            
            if j == m:
                return n - i
            
            if word1[i] == word2[j]:
                res = recurse(i+1, j+1)
            else:
                res = 1 + recurse(i+1, j+1)
            
            res = min(res, 1 + recurse(i, j+1))
            res = min(res, 1 + recurse(i+1, j))

            return res
        
        return recurse(0, 0)