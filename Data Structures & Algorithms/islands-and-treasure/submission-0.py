class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])
        def dfs(currx, curry, dist):
            nonlocal grid, n, m
            dirx = [-1,1,0,0]
            diry = [0,0,-1,1]
            if (currx >= n or currx < 0 or curry >= m or curry < 0):
                return
            grid[currx][curry] = dist
            for idx in range(len(dirx)):
                newx = currx + dirx[idx]
                newy = curry + diry[idx]
                if (newx >= n or newx < 0 or newy >= m or newy < 0):
                    continue
                if (grid[newx][newy] == 2147483647 or grid[newx][newy] > dist+1):
                    dfs(newx, newy, dist+1)
        
        for i in range(n):
            for j in range(m):
                if (grid[i][j] == 0):
                    dfs(i, j, 0)
    
        for row in grid:
            print(row)
                


        