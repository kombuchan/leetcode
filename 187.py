# Repeated DNA Sequence
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        i,j = 0,10
        ret = set()
        seen = set()
        while j < len(s)+1:
            substr = s[i:j]
            if substr in seen: ret.add(substr)
            seen.add(substr)
            i+=1
            j+=1
        return list(ret)