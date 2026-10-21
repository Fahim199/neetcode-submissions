class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[-1]* (amount+1) for _ in range(len(coins))]

        def dfs(i, target):

            if i<0 or target <= 0:
                if target ==0:
                    return 1
                else:
                    return 0

            if dp[i][target] != -1:
                return dp[i][target]
            
            take1 = dfs(i, target-coins[i])
            notTake = dfs(i-1, target)
            dp[i][target] = take1 +  notTake
            return dp[i][target]

    
        #return dfs(len(coins)-1, amount)



        def tab():
            dp = [[0]* (amount+1) for _ in range(len(coins)+1)]

            #base case
            dp[0][0]=1
            for i in range(1, len(coins)+1):
                for j in range(amount+1):
                    take1=0

                    if j>= coins[i-1]:
                        take1 = dp[i][j-coins[i-1]]
                    notTake = dp[i-1] [j]

                    dp[i][j] = take1 +  notTake
            
            return dp[len(coins)][amount]


        return tab()


        