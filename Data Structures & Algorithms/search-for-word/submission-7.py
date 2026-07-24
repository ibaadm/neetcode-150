class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def dfs(i, r, c, used):
            if board[r][c] != word[i] or (r, c) in used:
                return False
            if i == len(word) - 1:
                return True
            
            used.add((r, c))
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if (0 <= nr < m and 0 <= nc < n):
                    if dfs(i+1, nr, nc, used):
                        return True
            used.remove((r, c))
            return False

        return any(dfs(0, r, c, set()) for r in range(m) for c in range(n))

