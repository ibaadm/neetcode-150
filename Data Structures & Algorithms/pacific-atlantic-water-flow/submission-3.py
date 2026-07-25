class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        pac = set()
        atl = set()

        def bfs(ocean):
            while q:
                r, c = q.popleft()
                height = heights[r][c]
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r+dr, c+dc
                    if (0 <= nr < m and 0 <= nc < n
                            and (nr, nc) not in ocean
                            and heights[nr][nc] >= height):
                        q.append((nr, nc))
                        ocean.add((nr, nc))

        q = deque()

        for c in range(n):
            q.append((0, c))
            pac.add((0, c))
        for r in range(1, m):
            q.append((r, 0))
            pac.add((r, 0))
        
        bfs(pac)
        
        for c in range(n):
            q.append((m-1, c))
            atl.add((m-1, c))
        for r in range(m-1):
            q.append((r, n-1))
            atl.add((r, n-1))
        
        bfs(atl)

        return list(pac & atl)
