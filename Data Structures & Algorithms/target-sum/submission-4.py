class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = {}

        def dfs(i, rem):
            #Base Case
            if i == -1:
                if rem==0 :
                    return 1
                else:
                    return 0
            key = (i,rem)
            if key in dp:
                return dp[key]
            
            # recursion steps
            plus =  dfs(i-1, rem - nums[i])
            minus = dfs(i-1,  rem + nums[i])
            dp[key] = plus + minus
            return dp[key]


        return dfs(len(nums)-1,  target)

        