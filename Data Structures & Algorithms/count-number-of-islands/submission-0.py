class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] == "1"):
                    self.dfs(i, j, grid)
                    count += 1
        return count
    def dfs(self, posx, posy, grid):
        dirx = [-1,1,0,0]
        diry = [0,0,-1,1]
        for i in range(len(dirx)):
            if (dirx[i]+posx >= 0 and diry[i]+posy >= 0 and dirx[i]+posx < len(grid) and diry[i]+posy < len(grid[0]) and grid[dirx[i]+posx][diry[i]+posy] == "1"):
                grid[dirx[i]+posx][diry[i]+posy] = "0"
                self.dfs(dirx[i]+posx, diry[i]+posy, grid)

    



        