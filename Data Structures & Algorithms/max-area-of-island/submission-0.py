class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        max_area = 0
        q = deque()

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    area = 0
                    grid[r][c] = 0
                    q.append((r, c))
                    while q:
                        i, j = q.popleft()
                        area += 1
                        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            ni, nj = i+di, j+dj
                            if (0 <= ni < m and 0 <= nj < n
                                    and grid[ni][nj] == 1):
                                grid[ni][nj] = 0
                                q.append((ni, nj))
                    max_area = max(max_area, area)
        return max_area