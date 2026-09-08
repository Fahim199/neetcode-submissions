class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        dp = [-1 for x in range(len(cost))]
        def dfs(i):
            if i < 0:
                return 0
            
            if dp[i] !=-1 : return dp[i]
            right = float("-inf")
            left = cost[i] + dfs(i-1)
            if i>-1:
                right = cost[i] + dfs(i-2)
            dp[i] = min(left,right)
            return dp[i]

            
        return dfs(len(cost)-1)