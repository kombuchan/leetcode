# 17. Letter Combinations of a Phone Number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "" : return []
        num_map = {
                "2" : "abc", 
                "3" : "def", 
                "4" : "ghi",
                "5" : "jkl",
                "6" : "mno",
                "7" : "pqrs",
                "8" : "tuv",
                "9" : "wxyz",
            }
        
        res = []
        s = ""
        return self.dfs(digits, num_map, [], "")
            
        
    def dfs(self, digits, num_map , res,s):
        if len(digits) == 0: 
            res.append(s)
        else:
            letters = num_map[digits[0]]
            for l in letters:
                self.dfs(digits[1:], num_map, res, s+l)
        return res

            

        
        
    
        