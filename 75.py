# Sort Colors : in-place, O(n) time, O(1) space
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counts = [0]*3
        
        for num in nums:
            counts[num] += 1
        
        i = 0
        for num, count in enumerate(counts):
            while count > 0:
                nums[i] = num
                count -= 1
                i += 1 
  