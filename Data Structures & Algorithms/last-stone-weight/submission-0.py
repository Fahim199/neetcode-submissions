class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            stoneOne = -heapq.heappop(stones)
            stoneTwo = -heapq.heappop(stones)
            if stoneOne != stoneTwo:
                newWeight = abs(stoneOne-stoneTwo)
                heapq.heappush(stones, -newWeight)

        if stones:
            return -stones[0]
        else:
            return 0


        



        