class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        q = deque()
        visited = set()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c, 0))
                    visited.add((r, c))
        
        max_time = 0
        while q:
            r, c, level = q.popleft()
            max_time = max(max_time, level)
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r+dr, c+dc
                if (0 <= nr < m and 0 <= nc < n
                        and grid[nr][nc] == 1
                        and (nr, nc) not in visited):
                    visited.add((nr, nc))
                    q.append((nr, nc, level + 1))

        for r in range(m):
            for c in range(n):
                if (r, c) not in visited and grid[r][c] == 1:
                    return -1
        
        return max_time
