class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        if self.size[px] < self.size[py]:
            px, py = py, px
        self.size[px] += self.size[py]
        self.parent[py] = px

    def getSize(self, x):
        return self.size[self.find(x)]

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dsu = DSU(m*n)
        max_area = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] != 1:
                    continue
                
                for dr, dc in [(0, 1), (1, 0)]:
                    nr, nc = r+dr, c+dc
                    if (0 <= nr < m and 0 <= nc < n
                            and grid[nr][nc] == 1):
                        dsu.union(r*n+c, nr*n+nc)
                max_area = max(max_area, dsu.getSize(r*n+c))
        return max_area
