class Solution:
    def jump(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [-1] * n

        def dfs(i):
            if i>=n-1:
                return 0
            if dp[i] != -1:
                return dp[i]

            jump = float("inf")
            
            for j in range(1, nums[i]+1):
                jump = min(1 + dfs(i+j), jump)

            dp[i] = jump 
            return dp[i]

        ##return dfs(0) 

        def greedy():
            jumps, l,r = 0,0,0

            while r< n-1:
                farthest = 0
                for i in range(l,r+1):
                    farthest = max(farthest, i+nums[i])
                
                l= r+1
                r= farthest
                jumps+=1
            return jumps

        return greedy()
        