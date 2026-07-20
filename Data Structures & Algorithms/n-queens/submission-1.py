import copy

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def dfs(queens, curr):
            if len(queens) == n:
                res.append(["".join(row) for row in curr])
                return

            i = len(queens)
            for j in range(n):
                if any(j == c or abs(i-r) == abs(j-c) for r, c in queens):
                    continue     
                queens.append((i, j))
                curr[i][j] = "Q"
                dfs(queens, curr)
                queens.pop()
                curr[i][j] = "."

        dfs([], [["." for _ in range(n)] for _ in range(n)])
        return res
