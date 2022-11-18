class Solution:
    def romanToInt(self, s: str) -> int:
        charDict = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        ans = 0
        
        i=len(s)-1
        while(i>=0):
            num = charDict[s[i]]
            if i-1 >= 0 and charDict[s[i-1]] < num:
                num = num - charDict[s[i-1]]
                i -= 1
            ans += num
            i -= 1
            
        return ans