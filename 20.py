#  Valid Parentheses

from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        parenthesesDict = {')': '(', '}': '{', ']' :'['}
        stack = deque()
        for c in s:
            if c not in parenthesesDict: stack.append(c)
            elif stack and stack.pop() == parenthesesDict[c]: continue
            else: return False
        return False if stack else True
