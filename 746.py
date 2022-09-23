class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return self.dfs(cost, -1, 0, float("inf"))
        
    def dfs(self, cost, currStep, currCost, minCost):
        if -1 < currStep < len(cost):
            currCost += cost[currStep]
        elif currStep >= len(cost): 
            return currCost
        minCost = min(minCost,
                      self.dfs(cost, currStep+1, currCost, minCost), 
                      self.dfs(cost, currStep+2, currCost, minCost))
        return minCost