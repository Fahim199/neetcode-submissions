class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        res = []

        for i, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                # Existing interval is completely before newInterval.
                res.append(interval)

            elif interval[0] > newInterval[1]:
                # newInterval belongs here; everything remaining comes after.
                res.append(newInterval)
                return res + intervals[i:]

            else:
                # Overlap: expand newInterval and keep scanning.
                newInterval = [
                    min(newInterval[0], interval[0]),
                    max(newInterval[1], interval[1]),
                ]

        # newInterval reaches the end, or intervals was empty.
        res.append(newInterval)
        return res