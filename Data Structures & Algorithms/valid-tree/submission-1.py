class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        graph =defaultdict(list)

        for x,y in edges:
            graph[x].append(y)            
            graph[y].append(x)

        visited = set()
        def dfs(i, parent):
            if i in visited:
                return True
            
            visited.add(i)

            for neighbours in graph.get(i,[]):
                if neighbours != parent:
                    if(dfs(neighbours, i)):
                        return True
            
            return False

        
        if(dfs(0, -1)):
            return False
        
        return len(visited) == n

