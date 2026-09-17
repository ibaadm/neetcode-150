class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            converted_row = False
            for j in range(n):
                if matrix[i][j] == 0:
                    for ni in range(m):
                        if matrix[ni][j] != 0:
                            matrix[ni][j] = None

                    if converted_row:
                        continue

                    for nj in range(n):
                        if matrix[i][nj] != 0:
                            matrix[i][nj] = None
                    converted_row = True
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == None:
                    matrix[i][j] = 0
        