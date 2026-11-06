class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        nInt = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            if intervals[i][0]> nInt[1]:
                res.append(nInt)
                nInt = intervals[i]
            else:
                nInt = [min(nInt[0], intervals[i][0]), max(nInt[1], intervals[i][1])]
        
        res.append(nInt)

        return res
                
