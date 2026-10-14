class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1] * n for _ in range(m)]


        def rec(i, j):
            if i==0 and j == 0:
                return 1
            if i<0 or j<0:
                return 0
            
            if dp[i][j] !=-1:
                return dp[i][j]

            top = rec(i, j-1)
            left = rec(i-1, j)
        
            dp[i][j] = top+left

            return dp[i][j]

        
        return rec(m-1, n-1)
        