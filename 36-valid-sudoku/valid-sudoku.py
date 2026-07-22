class Solution:
    def isValidSudoku(self, board):
        s = set()
        for i in range(9):
            for j in range(9):
                n = board[i][j]
                if n != ".":
                    if (i,n) in s or (n,j) in s or (i//3,j//3,n) in s:
                        return False
                    s.add((i,n))
                    s.add((n,j))
                    s.add((i//3,j//3,n))
        return True