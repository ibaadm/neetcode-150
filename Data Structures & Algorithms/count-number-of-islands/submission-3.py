class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        res = 0
        stack = []
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    res += 1
                    grid[r][c] = "0"
                    stack.append((r, c))
                    while stack:
                        i, j = stack.pop()
                        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            ni, nj = i+di, j+dj
                            if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == "1":
                                grid[ni][nj] = "0"
                                stack.append((ni, nj))
        return res