class Solution:
    def climbStairs(self, n: int) -> int:
        return self.dfs(n, 0, 0)
    
    def dfs(self, n, currSteps, numWays):
        if currSteps == n:
            return 1
        if currSteps > n:
            return 0
        numWays = self.dfs(n, currSteps+1, numWays) + self.dfs(n, currSteps+2, numWays)
        return numWays
     