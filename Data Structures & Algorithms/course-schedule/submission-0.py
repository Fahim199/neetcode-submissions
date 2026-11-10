class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adjacencyList = defaultdict(list)

        for u,v in prerequisites:
            adjacencyList[u].append(v)
        
        
        visited = [0] * numCourses

        def dfs(i):
            if visited[i] == -1:
                return False
            if visited[i] == 1:
                return True
            
            visited[i] = 1

            for neighbor in adjacencyList.get(i, []):
                if dfs(neighbor):
                    return True
            
            visited[i] = -1
            return False

        for i in range(numCourses):
            if dfs(i):
                return False
        
        return True
        