class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = [0] * 9
        col_sets = [0] * 9
        square_sets = [0] * 9

        for r in range(9):
            for c in range(9):
                x = board[r][c]
                if x == '.':
                    continue
                mask = 1 << (int(x)-1)

                if mask & row_sets[r]:
                    return False
                row_sets[r] |= mask

                if mask & col_sets[c]:
                    return False
                col_sets[c] |= mask

                square_idx = (r // 3) * 3 + c // 3
                if mask & square_sets[square_idx]:
                    return False
                square_sets[square_idx] |= mask
        
        return True