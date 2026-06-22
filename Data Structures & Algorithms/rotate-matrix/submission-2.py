class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]

        for i in range(n-1):
            for j in range(n-i-1):
                matrix[i][j], matrix[-j-1][-i-1] = matrix[-j-1][-i-1], matrix[i][j]
        