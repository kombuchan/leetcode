# Generate Parentheses

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self.recurse(n,'(',[])
    def recurse(self,n,s,ret):
        if s.count('(') == n and s.count(')') == n:
            ret.append(s)
            return 0
        if s.count(')') < s.count('(') or s.count('(') == n:
            self.recurse(n,s+')',ret)
        if s.count('(') != n : self.recurse(n,s+'(',ret)
        return ret
            
        