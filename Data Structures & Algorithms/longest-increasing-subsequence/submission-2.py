class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1] * (n + 1) for _ in range(n)]

        def dfs(i, last):
            if i == -1:
                return 0

            if dp[i][last] != -1:
                return dp[i][last]

            notTake = dfs(i - 1, last)

            take = 0
            if last == n or nums[i] < nums[last]:
                take = 1 + dfs(i - 1, i)

            dp[i][last] = max(notTake, take)
            return dp[i][last]

        return dfs(n - 1, n)