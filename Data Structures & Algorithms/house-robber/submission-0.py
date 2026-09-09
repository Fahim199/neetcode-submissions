class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1 for x in range(len(nums) +1)]

        def dfs(i):
            if i < 0:
                return 0
            
            if dp[i] != -1:
                return dp[i]
                
            take  = nums[i] + dfs(i-2)
            notTake = dfs(i-1)

            dp[i] = max(take, notTake)
            return dp[i]
        
        return dfs(len(nums)-1)
