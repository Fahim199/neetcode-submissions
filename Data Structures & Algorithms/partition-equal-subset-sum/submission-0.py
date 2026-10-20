class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp = {}
        def dfs(i, s1, s2):
            if i== -1:
                return s1 == s2

            key = (i,s1,s2)

            if key in dp:
                return dp[key]


            dp[key] =  dfs(i-1, s1+nums[i], s2) or dfs(i-1, s1, s2 + nums[i])

            return dp[key]
        
        return dfs(len(nums) -1, 0, 0)

        