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
            if i-1 >= 0:
                if s[i] == 'V' and s[i-1] == 'I':
                    num = 4
                    i-=1
                if s[i] == 'X' and s[i-1] == 'I':
                    num = 9
                    i-=1
                if s[i] == 'L' and s[i-1] == 'X':
                    num = 40
                    i-=1
                if s[i] == 'C' and s[i-1] == 'X':
                    num = 90
                    i-=1
                if s[i] == 'D' and s[i-1] == 'C':
                    num = 400
                    i-=1
                if s[i] == 'M' and s[i-1] == 'C':
                    num = 900
                    i-=1
            
            ans += num
            i -= 1
            
        return ans