class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for i in range(len(points)):
            x,y = points[i]
            d = (x**2 + y**2)**0.5
            minHeap.append((d,i))

        heapq.heapify(minHeap)

        res = []
        for i in range(k):
            dist, index = heapq.heappop(minHeap)
            res.append(points[index])

        return res

        