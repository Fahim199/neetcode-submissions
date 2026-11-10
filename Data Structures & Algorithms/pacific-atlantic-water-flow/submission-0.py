class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        row = len(heights)
        col = len(heights[0])
        res = []
        alt, pac = set(), set()
        def dfs(i,j, prev, visited):
            if i<0 or j<0 or i>=row or j>=col or heights[i][j]<prev or (i,j) in visited:
                return

            visited.add((i,j))

            dfs(i+1,j, heights[i][j], visited)
            dfs(i-1,j, heights[i][j], visited)
            dfs(i,j+1, heights[i][j], visited)
            dfs(i,j-1, heights[i][j], visited)

            return

        for c in range(col):
            dfs(0, c, heights[0][c], pac)
            dfs(row-1, c, heights[row-1][c], alt) 
    
        for r in range(row):
            dfs(r, 0, heights[r][0], pac)
            dfs(r, col-1, heights[r][col-1], alt)

        for i in range(row):
            for j in range(col):
                if (i,j) in alt and (i,j) in pac:
                    res.append([i,j])
        return res
        