# Top K Frequent Elements
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numDict = {}
        for num in nums:
            numDict[num] = numDict[num] + 1 if num in numDict else 1
        
        numCount = [[] for i in range(len(nums)+1)]
        
        for num in numDict:
            count = numDict[num]
            numCount[count].append(num)
        
        ret = []
        i = len(nums)
        for i in reversed(range(len(numCount))):
            for j in numCount[i]:
                 if len(ret) < k : ret.append(j)

        return ret