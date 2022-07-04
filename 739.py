# 739. Daily Temperatures
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        for i in range(len(temperatures)):
            l = temperatures[i]
            r = 1
            isFound = 0
            pos = i + 1
            while (isFound != 1 and pos < len(temperatures)):
                curr_temp = temperatures[pos]
                if (l < curr_temp):
                    ans[i] = r
                    isFound = 1
                r+=1
                pos+=1
        return ans