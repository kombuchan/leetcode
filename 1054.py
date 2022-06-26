# 1054. Distant Barcodes
from collections import defaultdict
import heapq

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        d = {};
        for num in barcodes:
            if num in d: d[num] += 1
            else:d[num] = 1         
        
        maxheap = [(-1 * d[k],k) for k in d]
        heapify(maxheap)
        res = []
        last = -1
        
        while(len(res) != len(barcodes)):
            curr = heappop(maxheap)
            if last == curr[1]: 
                temp = curr
                curr = heappop(maxheap)
                heappush(maxheap,temp)
            res.append(curr[1])
            curr = (curr[0] + 1, curr[1])
            if curr[0] != 0 : heappush(maxheap,curr)
            if len(res) != 0: last = curr[1]
             
        return res
            