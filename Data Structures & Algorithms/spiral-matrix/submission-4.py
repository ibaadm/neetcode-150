class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_idx = 0
        i = 0
        j = -1
        m = len(matrix)
        n = len(matrix[0])
        cycles = 0
        res = []
        dir_check = {
            0: lambda i, j: j < n - cycles,
            1: lambda i, j: i < m - cycles,
            2: lambda i, j: j >= cycles,
            3: lambda i, j: i >= cycles,
        }

        while True:
            valid = False
            while True:
                ni, nj = i + dirs[dir_idx][0], j + dirs[dir_idx][1]
                if dir_check[dir_idx](ni, nj):
                    res.append(matrix[ni][nj])
                    i, j = ni, nj
                    valid = True
                else:
                    break

            if not valid:
                break

            dir_idx = (dir_idx + 1) % 4
            if dir_idx == 3:
                cycles += 1
        
        return res
