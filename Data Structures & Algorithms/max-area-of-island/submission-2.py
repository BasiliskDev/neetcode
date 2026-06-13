class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] == 1):
                    area = self.dfs(i, j, grid)
                    max_area = max(area, max_area)
        return max_area
    def dfs(self, posx, posy, grid):
        dirx = [-1,1,0,0]
        diry = [0,0,-1,1]
        area = 1
        grid[posx][posy] = 0
        for i in range(len(dirx)):
            if (dirx[i]+posx >= 0 and diry[i]+posy >= 0 and dirx[i]+posx < len(grid) and diry[i]+posy < len(grid[0]) and grid[dirx[i]+posx][diry[i]+posy] == 1):
                grid[dirx[i]+posx][diry[i]+posy] = 0
                area += self.dfs(dirx[i]+posx, diry[i]+posy, grid)
        return area

    



        