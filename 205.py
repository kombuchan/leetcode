class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        charDict = {}
        charSet = set()
        
        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]
            if s_char not in charDict:
                if t_char in charSet:
                    return False
                charDict[s_char] = t_char
                charSet.add(t_char)
            elif charDict[s_char] != t_char:
                return False
        
        return True