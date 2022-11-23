class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k >= len(nums):
            return len(set(nums)) < len(nums)
        
        numSet = set(nums[0 : k+1])
        
        if len(numSet) < k+1:
            return True
        
        i = k+1
        while i < len(nums):
            numSet.remove(nums[i-k-1])
            if nums[i] in numSet:
                return True
            else:
                numSet.add(nums[i])
            i += 1
        return False