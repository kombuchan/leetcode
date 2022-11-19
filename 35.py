class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:  
        
        # if m == target return m
        # if m < target: l = m
        # if m > target: r = m-1
        
        l = 0
        r = len(nums) - 1
        
        while l < r:
            m = l + (r - l + 1) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m
            else:
                return m
        return l
            