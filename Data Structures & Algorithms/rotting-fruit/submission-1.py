class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        for i, row in enumerate(grid):
            for j, banana in enumerate(row):
                if banana == 2:
                    queue.append([i, j, 0])
    
        max_time = 0
        while len(queue) != 0:
            dirx = [-1,1,0,0]
            diry = [0,0,1,-1]

            curr_b = queue.pop(0)
            time = curr_b[2]
        
            for i in range(len(dirx)):
                if (curr_b[0] + dirx[i] >= 0 and curr_b[1] + diry[i] >= 0 and curr_b[0] + dirx[i] < len(grid) and curr_b[1] + diry[i] < len(grid[0]) and grid[curr_b[0] + dirx[i]][curr_b[1] + diry[i]] == 1):
                    grid[curr_b[0] + dirx[i]][curr_b[1] + diry[i]] = 2
                    queue.append([curr_b[0] + dirx[i], curr_b[1] + diry[i], time+1])
            
            max_time = max(max_time, time)
        
        
        for i, row in enumerate(grid):
            for j, banana in enumerate(row):
                if banana == 1:
                    return -1
        
        return max_time
            


        