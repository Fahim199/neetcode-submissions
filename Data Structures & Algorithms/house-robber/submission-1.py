class Solution:
    def rob(self, nums: List[int]) -> int:

        #bottom up
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
        
        #return dfs(len(nums)-1)

        #topDown
        def tab():
            dp = [-1 for x in range(len(nums) +1)]

            dp[0],dp[1] = 0, nums[0]

            for i in range(1, len(nums)):
                take = nums[i] + dp[i-1]
                notTake = dp[i]
                dp[i+1] = max(take, notTake)
            return dp[len(nums)]

        return tab()

