class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        low = 0
        high = n * m - 1
        idx = (low + high)//2
        while (high >= low):
            print(idx)
            print(matrix[idx//m][idx%m])
            print()
            if (matrix[idx//m][idx%m] == target):
                return True
            if (matrix[idx//m][idx%m] > target):
                high = idx - 1
            if (matrix[idx//m][idx%m] < target):
                low = idx + 1
            idx = (low + high)//2
        return False
            
