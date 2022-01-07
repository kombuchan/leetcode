# Game of Life

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        for m in range(len(board)):
            for n in range(len(board[0])):
                neighbors = self.find_neighbors(board,m,n)
                board[m][n] = self.find_state(board[m][n],neighbors)
        for m in range(len(board)):
            for n in range(len(board[0])):
                if board[m][n] != 0 : 
                    board[m][n] = abs(board[m][n])-1

            
    def find_state(self,value,neighbors):
        if value > 0:
            if neighbors.count(1) == 2 or neighbors.count(1) == 3: return  2
            elif neighbors.count(1) < 2 or neighbors.count(1) > 3: return  1  
        elif  neighbors.count(1) == 3: return -2
        else: return 0 
        
    def find_neighbors(self,board,m,n):
        neighbors = []
        if m > 0 : neighbors.append(int(board[m-1][n] > 0)) 
        if m < len(board)-1: neighbors.append(int(board[m+1][n] > 0))
        if n > 0 : neighbors.append(int(board[m][n-1] > 0))
        if n < len(board[0])-1: neighbors.append(int(board[m][n+1] > 0))
        if m > 0  and n > 0:  neighbors.append(int(board[m-1][n-1] > 0))
        if m > 0  and n < len(board[0])-1: neighbors.append(int(board[m-1][n+1] > 0))
        if m < len(board)-1 and n > 0:  neighbors.append(int(board[m+1][n-1] > 0))
        if m < len(board)-1 and n < len(board[0])-1: neighbors.append(int(board[m+1][n+1] > 0))
        return neighbors