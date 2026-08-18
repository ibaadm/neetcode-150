from functools import cache

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        @cache
        def dfs(i, j):
            curr = matrix[i][j]
            longest_path = 1
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = di + i, dj + j
                if (0 <= ni < m and 0 <= nj < n
                        and matrix[ni][nj] > curr):
                    longest_path = max(longest_path, dfs(ni, nj) + 1)
            return longest_path

        return max(dfs(i,j) for j in range(n) for i in range(m))
