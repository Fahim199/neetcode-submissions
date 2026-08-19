class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        heapq.heapify(self.minHeap)
        heapq.heapify(self.maxHeap)

    def addNum(self, num: int) -> None:
        if not self.maxHeap or num< -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)
        if  len(self.maxHeap) > len(self.minHeap) +1:
            element = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, element)
        elif len(self.maxHeap) < len(self.minHeap):
            element = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -element)
        

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return -self.maxHeap[0]/2 + self.minHeap[0]/2
        else:
            return -self.maxHeap[0]/1
        
        