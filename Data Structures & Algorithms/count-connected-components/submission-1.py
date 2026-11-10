class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        visited = set()
        graph  = defaultdict(list)
        for x,y  in edges:
            graph[x].append(y)
            graph[y].append(x)

        queue = deque()


        def bfs(node):
            queue.append(i)
            visited.add(node)
            while queue:
                node = queue.popleft()
                for nei in graph.get(node, []):
                    if nei not in visited:
                        queue.append(nei)
                        visited.add(nei)

        cnt =0
        for i in range(n):
            if i not in visited:
                cnt +=1
                bfs(i)

        return cnt
        