class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        checked = set()
        visited = set()

        def dfs(r, c):
            free = False
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r+dr, c+dc
                if (0 <= nr < m and 0 <= nc < n
                        and board[nr][nc] == "O"
                        and (nr, nc) not in visited):
                    visited.add((nr, nc))
                    free = dfs(nr, nc) or free
            return free or r == 0 or r == m-1 or c == 0 or c == n-1
            

        for r in range(m):
            for c in range(n):
                if board[r][c] == "O" and (r, c) not in checked:
                    visited.add((r, c))
                    if dfs(r, c):
                        checked |= visited
                    else:
                        for i, j in visited:
                            board[i][j] = "X"
                    visited.clear()
