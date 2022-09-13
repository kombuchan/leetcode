#2 Sum
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        
        while(r>l):
            curr_sum = numbers[l] + numbers[r]
            print(curr_sum)
            if curr_sum < target:
                l+=1
            if curr_sum > target:
                r-=1
            elif curr_sum == target: return[l+1,r+1]