class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def runner(arr):
            dp = [-1 for x in range(len(arr))]
            def dfs(i):
                if i ==0 :
                    return arr[0]

                if i< 0:
                    return 0

                if dp[i]!=-1:
                    return dp[i]
                dp[i] = max(arr[i] + dfs(i-2), dfs(i-1))
                return dp[i]
            return dfs(len(arr)-1)

        return max(runner(nums[1:]), runner(nums[:-1]))
        