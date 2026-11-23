"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        startingTime, endingTime = [], []
        n = len(intervals)

        if n <2:
            return n

        for interval in intervals:
            startingTime.append(interval.start)
            endingTime.append(interval.end)
        
        startingTime.sort()
        endingTime.sort()

        firstPtr, secondPtr = 0, 0
        maxRooms, currentRooms = 0, 0

        while firstPtr < n or secondPtr < n:
            if firstPtr == n:
                secondPtr += 1
                continue
            
            if startingTime[firstPtr] < endingTime[secondPtr]:
                currentRooms += 1
                firstPtr += 1
                maxRooms = max(currentRooms, maxRooms)
            else:
                currentRooms -= 1
                secondPtr += 1
        
        return maxRooms



        