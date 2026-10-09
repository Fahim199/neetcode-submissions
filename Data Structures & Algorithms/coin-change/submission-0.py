class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(rem):
            if rem == 0:
                return 0
            
            if rem in memo:
                return memo[rem]

            res = float("+inf")

            for coin in coins:
                if rem - coin >=0:
                    res = min(res, 1+dfs(rem-coin))
                    
            memo[rem]=res

            return res
        

        reqCoins = dfs(amount)
        return -1 if reqCoins>10000 else reqCoins

            

