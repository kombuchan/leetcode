# Decode Ways
# Naive approach (recursive):

class Solution:
    def numDecodings(self, s: str) -> int:
        ret = self.recurse(s,"",0,set())
        return len(ret)
    
    def recurse(self,s,curr,i,ret):
        valid =  set(['1','2','3','4','5','6','7','8','9','10','11','12','13',
                      '14','15','16','17','18','19','20','21','22','23','24','25','26'])
        
        if sum(c.isdigit() for c in curr) == len(s): 
            ret.add(curr)
        
        if i < len(s) and s[i] in valid: 
            self.recurse(s, curr + " " + s[i],i+1,ret)
        
        if  i+1 < len(s) and s[i:i+2] in valid: 
            self.recurse(s,curr + " " + s[i:i+2],i+2,ret)
    
        return ret