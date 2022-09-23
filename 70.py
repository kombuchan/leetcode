class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.dfs(n, 0, 0, memo)
    
    def dfs(self, n, currSteps, numWays, memo):
        if currSteps in memo:
            return memo[currSteps]
        if currSteps == n:
            return 1
        if currSteps > n:
            return 0
        numWays = self.dfs(n, currSteps+1, numWays, memo) + self.dfs(n, currSteps+2, numWays, memo)
        if currSteps not in memo:
            memo[currSteps] = numWays
        return numWays
        