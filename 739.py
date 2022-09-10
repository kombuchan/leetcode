# 739. Daily Temperatures
from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        ans = [0]*len(temperatures)
        for i in range(len(temperatures)):
            if i == 0: 
                stack.append((temperatures[i],i))
                continue
            while stack and temperatures[i] > stack[-1][0]:
                temp = stack.pop()
                ans[temp[1]]= i - temp[1]
            stack.append((temperatures[i],i))
        return ans