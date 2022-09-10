class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0: return 0
        
        numSet = set(nums)
        maxLen, currLen = 0, 0
        
        for n in nums:
            if n-1 not in numSet:
                currLen = 1
                k=n+1
                while(k in numSet):
                    currLen += 1
                    k+=1
            maxLen = max(currLen, maxLen)
        return(maxLen)