class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for i in range(n // 2):
            coordx = [i, n-1-i, n-1-i, i]
            coordy = [n-1-i, n-1-i, i, i]

            for j in range(n - 2*i - 1):
                values = [
                    matrix[coordx[k]][coordy[k]]
                    for k in range(4)
                ]

                for k in range(4):
                    matrix[coordx[(k+1) % 4]][coordy[(k+1) % 4]] = values[k]

                coordx[0] += 1
                coordy[1] -= 1
                coordx[2] -= 1
                coordy[3] += 1