class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:


        counter = {}
        for c in tasks:
            counter[c] = counter.get(c,0) + 1
        
        maxHeap = []
        for k,v in counter.items():
            maxHeap.append((-v))
        
        heapq.heapify(maxHeap)

        queue = deque()
        time = 0
        while maxHeap or queue:
            time+=1
            if(maxHeap):
                element = 1 + heapq.heappop(maxHeap)
                if element:
                    t = time + n #time when the task would be available next
                    queue.append([t, element])
            else:
                time = queue[0][0]
            if queue and queue[0][0]==time:
                heapq.heappush(maxHeap, queue.popleft()[1])



        
        return time
        
        
        






        