class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        square_sets = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                x = board[r][c]
                if x == '.':
                    continue

                if x in row_sets[r]:
                    return False
                row_sets[r].add(x)

                if x in col_sets[c]:
                    return False
                col_sets[c].add(x)

                square_idx = (r // 3) * 3 + c // 3
                if x in square_sets[square_idx]:
                    return False
                square_sets[square_idx].add(x)
        
        return True