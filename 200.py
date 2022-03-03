# Number of Islands 
class Solution:
    def bfs(self,i,j,grid):
        m,n=len(grid),len(grid[0])
        direction={(0,1),(0,-1),(-1,0),(1,0)}
        grid[i][j] = "0"
        for x,y in direction:
            if not (i+x<0 or i+x>=m or j+y<0 or  j+y>=n):
                if grid[i+x][j+y]=="1": self.bfs(i+x,j+y,grid)
        return 1
                        
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n=len(grid),len(grid[0])
        ans=0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != "0" and grid[i][j]=="1":
                    ans+=self.bfs(i,j,grid)
        return ans