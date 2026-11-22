class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        pacific = [[False] * m for _ in range(n)]
        atlantic = [[False] * m for _ in range(n)]

        q = deque([])
        for i in range(len(pacific)):
            q.append([i, 0])
        for i in range(len(pacific[0])):
            q.append([0, i])
        
        while (len(q)):
            print(q)
            x, y = q.popleft()
            pacific[x][y] = True
            if (x - 1 >= 0 and not pacific[x-1][y] and heights[x-1][y] >= heights[x][y]):
                q.append([x-1, y])
            if (y - 1 >= 0 and not pacific[x][y-1] and heights[x][y-1] >= heights[x][y]):
                q.append([x, y-1])
            if (x + 1 < n and not pacific[x+1][y] and heights[x+1][y] >= heights[x][y]):
                q.append([x+1, y])
            if (y + 1 < m and not pacific[x][y+1] and heights[x][y+1] >= heights[x][y]):
                q.append([x, y+1])
                
    
        for i in range(len(atlantic)):
            q.append([i, len(atlantic[0])-1])
        for i in range(len(atlantic[0])):
            q.append([len(atlantic)-1, i])
        
        while (len(q)):
            x, y = q.popleft()
            atlantic[x][y] = True
            if (x - 1 >= 0 and not atlantic[x-1][y] and heights[x-1][y] >= heights[x][y]):
                q.append([x-1, y])
            if (y - 1 >= 0 and not atlantic[x][y-1] and heights[x][y-1] >= heights[x][y]):
                q.append([x, y-1])
            if (x + 1 <  n and not atlantic[x+1][y] and heights[x+1][y] >= heights[x][y]):
                q.append([x+1, y])
            if (y + 1 <  m and not atlantic[x][y+1] and heights[x][y+1] >= heights[x][y]):
                q.append([x, y+1])
        
        ret = []
        for i in range(len(atlantic)):
            for j in range(len(atlantic[0])):
                if (atlantic[i][j] and pacific[i][j]):
                    ret.append([i, j])
        
        print(pacific)
        print(atlantic)
        return ret

        
        