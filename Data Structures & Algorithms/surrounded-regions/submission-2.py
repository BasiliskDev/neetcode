class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = [[False] * len(board[0]) for _ in range(len(board))]

        n = len(board)
        m = len(board[0])

        surrounded = True
        cells = []

        def dfs(posx, posy):
            nonlocal visited, board, surrounded
            if (posx == n-1 or posx == 0):
                surrounded = False
                return
            if (posy == m-1 or posy == 0):
                surrounded = False
                return
            visited[posx][posy] = True
            
            dirx = [-1,1,0,0]
            diry = [0,0,-1,1]

            for i in range(len(dirx)):
                if (board[posx + dirx[i]][posy+diry[i]] == 'O' and not visited[posx + dirx[i]][posy + diry[i]]):
                    dfs(posx + dirx[i], posy + diry[i])
            
            cells.append([posx, posy])
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (board[i][j] == 'O' and not visited[i][j]):
                    cells = []
                    surrounded = True
                    dfs(i, j)
                    if (surrounded):
                        for cell in cells:
                            board[cell[0]][cell[1]] = 'X'

        
        