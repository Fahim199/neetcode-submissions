class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegreeNodes = set()

        for _,outgoing in edges:
            indegreeNodes.add(outgoing)
        res =[]
        for i in range(n):
            if i not in indegreeNodes:
                res.append(i)
        
        return res