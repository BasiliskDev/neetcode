class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = []
        for i in range(n):
            board.append(['.'] * n)

        res = []
        self.rec(0, n, board, res)
        return res

    def rec(self, row, n, board, res):
        if row == n:
            copy = []
            for r in board:
                copy.append("".join(r))
            res.append(copy)
            return

        for col in range(n):
            if self.noQueensAttacking(row, col, board, n):
                board[row][col] = 'Q'
                self.rec(row + 1, n, board, res)
                board[row][col] = '.'

    def noQueensAttacking(self, row, col, board, n):
        # check same column above
        for r in range(row):
            if board[r][col] == 'Q':
                return False

        # check upper-left diagonal
        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if board[r][c] == 'Q':
                return False
            r -= 1
            c -= 1

        # check upper-right diagonal
        r, c = row - 1, col + 1
        while r >= 0 and c < n:
            if board[r][c] == 'Q':
                return False
            r -= 1
            c += 1

        return True