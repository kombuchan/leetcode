class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l = 0
        r = l + 1
        res = []
        while r < len(nums):
            prev = l

            while r < len(nums) and nums[prev] + 1 == nums[r]:
                prev = r
                r += 1
            r = prev

            if r == l:
                res.append(f"{nums[l]}")
            else: 
                res.append(f"{nums[l]}->{nums[r]}")

            l = r + 1
            r = l + 1

        if l < len(nums):
            res.append(f"{nums[l]}")

        return res