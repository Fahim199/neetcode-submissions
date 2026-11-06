class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        nInt = intervals[0]
        cnt = 0
        for i in range(1,len(intervals)):
            if intervals[i][0]>=nInt[1]:
                nInt = intervals[i]
            else:
                nInt = [max(intervals[i][0], nInt[0]), min(intervals[i][1], nInt[1])]
                cnt+=1
        
        return cnt