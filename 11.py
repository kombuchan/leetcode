# Container With Most Water
#
# NAIVE APPROACH - O(N^2)
# 
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         area = -float('inf')
#         for i in range(len(height)):
#             for j in range(i+1, len(height)):
#                 a = (j-i)*min(height[i],height[j])
#                 area = max(area,a)
#         return(area)
#
# LINEAR TIME - O(N)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = -float('inf')
        l = 0
        r = len(height)-1
        while(l<r):
            a = (r-l)*min(height[l],height[r])
            area = max(area,a)
            if height[l] <= height[r]: l+=1
            else: r -= 1
        return(area)
        