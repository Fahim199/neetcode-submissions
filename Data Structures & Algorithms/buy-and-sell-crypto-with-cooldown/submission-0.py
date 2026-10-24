class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[-1,-1] for _ in range(len(prices)) ]
        prices.reverse()
        def dfs(i, bought):
            if i <0:
                return 0

            if dp[i][bought] != -1:
                return dp[i][bought]

            take = 0

            if(bought):
                take = prices[i] + dfs(i-2, 0)
            else:
                take = -prices[i] + dfs(i-1, 1)

            notTake = dfs(i-1, bought)

            dp[i][bought] = max(take, notTake)

            return dp[i][bought]


        return dfs(len(prices)-1, 0)
        