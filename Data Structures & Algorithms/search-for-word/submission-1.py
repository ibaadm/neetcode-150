class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        start = word[0]

        def dfs(i, r, c, used):
            if i == len(word):
                return True
            
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if (0 <= nr < m and 0 <= nc < n and
                        (nr, nc) not in used and
                        board[nr][nc] == word[i]):
                    used.add((nr, nc))
                    if dfs(i+1, nr, nc, used):
                        return True
                    used.remove((nr, nc))


        for r in range(m):
            for c in range(n):
                if board[r][c] == start and dfs(1, r, c, {(r, c)}):
                    return True
        
        return False