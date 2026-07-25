class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        
        q = deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append((r, c, 0))

        while q:
            r, c, dist = q.popleft()
            dist += 1
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r+dr, c+dc
                if (0 <= nr < m and 0 <= nc < n
                        and dist < grid[nr][nc]):
                    grid[nr][nc] = dist
                    q.append((nr, nc, dist))