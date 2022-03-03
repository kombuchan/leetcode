# Brick Wall
from collections import defaultdict
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        cracks = defaultdict(int)
        for row in wall:
            width = 0
            for brick in range(len(row)):
                width += row[brick]
                if brick != len(row)-1:  cracks[width] += 1
        
        return len(wall) - max(cracks.values()) 
    