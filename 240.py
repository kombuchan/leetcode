# Search a 2D Matrix II

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.dfs(matrix,0,0,target,False)
    
    def dfs(self,matrix,r,c,target, result):
        if matrix[r][c] == target: result = True
        
        if r+1 in range(len(matrix)) : result = self.dfs(matrix,r+1,c,target,result)
        if c+1 in range(len(matrix[0])): result = self.dfs(matrix,r,c+1,target,result)
        
        return result