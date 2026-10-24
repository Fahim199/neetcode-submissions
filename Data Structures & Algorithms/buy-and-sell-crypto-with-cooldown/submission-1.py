class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices.reverse()
        def tab():
            dp = [[0,0] for _ in range(len(prices)+2) ]

            for i in range(len(prices)):
                for j in range(2):
                    if j:
                        take = prices[i] + dp[i][0]
                    else:
                        take = -prices[i] + dp[i+1][1]
                    
                    notTake = dp[i+1][j]

                    dp[i+2][j] = max(take, notTake)

            return dp[len(prices)+1][0]
        return tab()

        dp = [[-1,-1] for _ in range(len(prices)) ]
        

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
        