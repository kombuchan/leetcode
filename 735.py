# Asteroid collision
from collections import deque
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = deque()
        for i in asteroids:
            if not stack: stack.append(i)
            elif stack and stack[-1] > 0 and i < 0:
                while stack and abs(i) > stack[-1] and stack[-1] > 0: stack.pop()
                if stack and abs(i) == stack[-1] and stack[-1] > 0: stack.pop();continue
                if stack and abs(i) < stack[-1] and stack[-1] > 0 : continue
                stack.append(i)
            else: stack.append(i)
        return(list(stack))