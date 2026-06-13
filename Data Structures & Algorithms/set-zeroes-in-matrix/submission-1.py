class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_pos = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (matrix[i][j] == 0):
                    zero_pos.append([i, j])
        for x, y in zero_pos:
            for i in range(len(matrix[0])):
                matrix[x][i] = 0
            for j in range(len(matrix)):
                matrix[j][y] = 0
        
        