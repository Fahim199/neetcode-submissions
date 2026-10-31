class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n =len(nums)
        dp = n*[-1]
        def dfs(i):
            if i == (n-1):
                return True
            elif i>=n or nums[i] ==0:
                return False

            if dp[i]!= -1:
                return dp[i]

            for x in range(1, nums[i]+1):
                if(dfs(i+x)):
                    dp[i] = True
                    return dp[i]
            
            dp[i] = False
            return dp[i]
        

        #return dfs(0)


        def greedy():
            goalPost = n -1

            for i in range(n-1, -1, -1):
                if i + nums[i] >= goalPost:
                    goalPost = i
            
            return True if goalPost == 0 else False
        
        return greedy()





        