class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #rows
        print('rows')
        for row in board:
            arr = set()
            for num in row:
                if num in arr and num != '.':
                    return False
                arr.add(num)
    
        #cols
        print('cols')
        for i in range(len(board)):
            arr = set()
            for j in range(len(board[i])):
                if board[j][i] in arr and board[j][i] != '.':
                    return False
                arr.add(board[j][i])
        
        #squares of 3
        lookup = {}
        print('squares')
        for i in range(len(board)):
            for j in range(len(board[i])):
                if ((i//3, j//3) in lookup):
                    if (board[i][j] in lookup[(i//3, j//3)] and board[i][j] != '.'):
                        return False
                    else:
                        lookup[(i//3, j//3)].add(board[i][j])
                        
                else:
                    lookup[(i//3, j//3)] = set()
                    lookup[(i//3, j//3)].add(board[i][j])
        
        return True


        