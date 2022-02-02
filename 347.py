# Top K Frequent Elements

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numDict = {}
        for num in nums:
            if num not in numDict: numDict[num] = 1
            else: numDict[num] += 1
        
        numCount = {}
        for i in range(len(nums)+1): numCount[i] = []
        
        for num in numDict:
            count = numDict[num]
            numCount[count].append(num)
        
        ret = []
        
        i = len(nums)
        while(len(ret)!=k) and i >= 0:
            if len(numCount[i]) > 0:
                j = 0
                while len(ret) < k and j < len(numCount[i]): 
                    ret.append(numCount[i][j])
                    j += 1
            i -= 1
        
        return ret