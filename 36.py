# Valid Sudoku - Naive Solution
class Solution:
    def check_row(self,board,r):
        numSet = set()
        for num in board[r]:
            if num in numSet: return False
            if num != ".": numSet.add(num)
        return True
    
    def check_col(self,board,c):
        numSet = set()
        for r in range(len(board)):
            if board[r][c] in numSet: return False
            if board[r][c] != ".": numSet.add(board[r][c])
        return True
    
    def check_3x3(self,board,r,c):
        row = r-(r%3)
        col = c-(c%3)
        numSet = set()
        for i in range(row,row+3):
            for j in range(col,col+3):
                print(board[i][j])
                if board[i][j] in numSet: return False
                if board[i][j] != ".": numSet.add(board[i][j])
        return True
        
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(len(board)):
            for c in range(len(board[0])):
                if not self.check_row(board,r) or not self.check_col(board,c) or not self.check_3x3(board,r,c):
                    return False
        return True