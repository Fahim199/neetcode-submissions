class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.numbers, self.k = nums, k
        heapq.heapify(self.numbers)
        while(len(self.numbers)>k):
            heapq.heappop(self.numbers)

    def add(self, val: int) -> int:
        heapq.heappush(self.numbers, val)
        if(len(self.numbers)>self.k):
            heapq.heappop(self.numbers)
        return self.numbers[0]

        
