# Triangle
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        return self.dfs(triangle,0,0,memo)
    
    def dfs(self,triangle,r,c,memo):
        if r == len(triangle)-1: memo[(r,c)] = triangle[r][c]
        if (r,c) in memo: return memo[(r,c)]
        else: memo[(r,c)] = triangle[r][c] + min(self.dfs(triangle,r+1,c,memo), self.dfs(triangle,r+1,c+1,memo))
        return memo[(r,c)]