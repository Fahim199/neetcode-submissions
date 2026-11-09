class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        row = len(grid)
        col  = len(grid[0])

        
        
        def bfs(i,j):
            queue  = deque([(i,j)])

            while queue:
                x,y = queue.popleft()

                if x<0 or y<0 or x>=row or y>=col or grid[x][y]!="1":
                    continue

                grid[x][y]= "0"

                queue.append((x+1,y))
                queue.append((x-1,y))
                queue.append((x,y-1))
                queue.append((x,y+1))

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    cnt+=1
                    bfs(i,j)

        return cnt

        