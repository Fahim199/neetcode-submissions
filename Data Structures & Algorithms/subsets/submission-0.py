class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        numsLength = len(nums)

        def dfs(start, path):
            if(len(path)> numsLength):
                return

            for i in range(start, numsLength):
                path.append(nums[i])
                res.append(path[:])
                dfs(i+1, path)
                path.pop()
        
        dfs(0, [])
        return res

        