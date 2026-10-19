class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [-1]*len(s)

        def dfs(i):
            # We successfully used all of s.
            if i == len(s):
                return True

            if dp[i]!=-1:
                return dp[i]

            for word in wordDict:
                end = i + len(word)

                if s[i:end] == word:
                    # This word works if the rest of the string works too.
                    if dfs(end):
                        dp[i] = True
                        return dp[i]

            # No matching word led to a successful segmentation.
            dp[i] = False
            return dp[i]

        return dfs(0)