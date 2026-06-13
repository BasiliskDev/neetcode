class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dirx = [0, 1, 0, -1]
        diry = [1, 0, -1, 0]
        ret = []
        n = len(matrix)
        m = len(matrix[0])
        visited = [[False] * m for i in range(n)]
        x = 0
        y = 0
        idx = 0
        ret.append(matrix[0][0])
        visited[0][0] = True
        while (len(ret) < m*n):
            if (x+dirx[idx%4] >= n or x+dirx[idx%4] < 0 or y+diry[idx%4] >= m or y+diry[idx%4] < 0):
                idx += 1
            new_x = x+dirx[idx%4]
            new_y = y+diry[idx%4]
            if (visited[new_x][new_y]):
                idx += 1
                new_x = x+dirx[idx%4]
                new_y = y+diry[idx%4]
            x = new_x
            y = new_y
            visited[x][y] = True
            ret.append(matrix[x][y])
        return ret
        