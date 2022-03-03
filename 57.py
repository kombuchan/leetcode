# Insert Interval
class Solution:
    def earlier_intervals(self,intervals,newInterval):
        ret = []
        for i in intervals:
            if i[1] < newInterval[0]: ret.append(i)
        return ret
    
    def later_intervals(self,intervals,newInterval):
        ret = []
        for i in intervals:
            if i[0] > newInterval[1]: ret.append(i)
        return ret
    
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        left = self.earlier_intervals(intervals,newInterval)
        right = self.later_intervals(intervals,newInterval)
        
        if left + right == intervals:
            return left + [newInterval] + right
        else:   
            start = min(intervals[len(left)][0], newInterval[0])
            end = max(intervals[-len(right)-1][1], newInterval[1])
            return left+[[start,end]] +right